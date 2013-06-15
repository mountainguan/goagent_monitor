# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache


import json


from fetch_config import config as fetch_config
import lib


def getPage(cluster_id):
	PAGE0 = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>
'''
	PAGE1 = '''
</title>
<style type="text/css">
<!--
.title {
        color: #9F0000;
        font-weight: bold;
}
.content {font-size: 15px}
body {
        /*background-image: url(images/night.jpg);
        background-repeat: no-repeat;
        background-attachment: fixed;*/
}
-->
</style>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-36190186-3', 'goagentmonitor.appspot.com');
  ga('send', 'pageview');

</script>
</head>
<body>
<center>
  <p>&nbsp;</p>
  <form action="https://www.google.com/search"><input name="ie" type="hidden" value="UTF-8"><input name="oe" type="hidden" value="UTF-8"><input name="aq" type="hidden" value="t"><input name="rls" type="hidden" value="org.mozilla:zh-CN:official"><input name="client" type="hidden" value="firefox-a"><input name="q" type="text"><input value="谷歌搜索" type="submit"></form>
 

<h1> 
'''
	PAGE2 = ''' 
</h1>
<table width="900" border="1" cellpadding="1" cellspacing="0" bordercolor="#000000">
  <tr>
    <td><table width="
'''
	PAGE3 = '''
%" cellpadding="1" cellspacing="0" bgcolor="#00CC00">
      <tr>
        <td>&nbsp;</td>
      </tr>
    </table></td>
  </tr>
</table>
  <tr>
    <td colspan="3" align="center" valign="top">
'''
	PAGE4 = '''
</td>
  </tr>
</table>

</center>

</body>
</html>

'''
	cluster_attrs = fetch_config[cluster_id]

	result = urlfetch.fetch(cluster_attrs['url'])
	urltype = cluster_attrs['urltype']
	name = cluster_attrs['name'].encode('utf8')
	message = cluster_attrs['message'].encode('utf8')
	if (urltype) == 'ini':
		appids = lib.getAppidFromINI(result.content)
	elif (urltype) == 'txt':
		appids = result.content.split('|')


	appid_dict = memcache.get_multi(appids)

	response_dict = {
		"B_available": [],
		"C_over_quota": [],
	}

	for appid, val in appid_dict.iteritems():
		if val is True:
			response_dict['B_available'].append(appid)
		elif val is False:
			response_dict['C_over_quota'].append(appid)

	response_dict['A_status_msg'] = "今日还剩 %dGB/%dGB 流量" % (len(response_dict['B_available']), len(appids))

	PAGE = PAGE0+ name + PAGE1 + name + '	' + response_dict['A_status_msg'] + PAGE2 + '%f'%((float(len(response_dict['B_available']))/float(len(appids)))*100) + PAGE3 + message + PAGE4
	return PAGE

class PageHandler(webapp2.RequestHandler):
	def get(self, cluster_id=None):
		self.response.write(getPage(cluster_id))


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/page/(.*)', PageHandler)
], debug=True)
