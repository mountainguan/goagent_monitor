# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache


import json


from monitor_config import config as monitor_config
from monitor_config import google_analytics_code
import list_handler
import api_handler


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
'''
	PAGE2 = '''
</head>
<body>
<center>
  <p>&nbsp;</p>
  <form action="https://www.google.com/search"><input name="ie" type="hidden" value="UTF-8"><input name="oe" type="hidden" value="UTF-8"><input name="aq" type="hidden" value="t"><input name="rls" type="hidden" value="org.mozilla:zh-CN:official"><input name="client" type="hidden" value="firefox-a"><input name="q" type="text"><input value="谷歌搜索" type="submit"></form>
 

<h1> 
'''
	PAGE3 = ''' 
</h1>
<table width="900" border="1" cellpadding="1" cellspacing="0" bordercolor="#000000">
  <tr>
    <td><table width="
'''
	PAGE4 = '''
%" cellpadding="1" cellspacing="0" bgcolor="#00CC00">
      <tr>
        <td>&nbsp;</td>
      </tr>
    </table></td>
  </tr>
</table>
<p>流量会在<a href="https://zh.wikipedia.org/zh-cn/%E5%A4%AA%E5%B9%B3%E6%B4%8B%E6%97%B6%E5%8C%BA">加州时间</a>每日 0:00 重置</p>
<span>现在的加州时间为：</span><div style="position:relative;width:200px;"><iframe src="https://zh.thetimenow.com/clock/united_states/california/san_francisco?t=n&amp;embed=1&amp;text=16&amp;textdate=15&amp;format=24&amp;digitalclock=36&amp;analogclock=60&amp;letter_spacing=-0&amp;bordersize=0&amp;bordercolor=fffffff&amp;bgcolor=FFFFFF&amp;colorloc=ffffff&amp;colordigital=000000&amp;colordate=000000&amp;styleloc=normal&amp;styledigital=normal&amp;styledate=normal&amp;right=0" width="200" height="80"style="border:none;overflow:hidden;" scrolling="no"></iframe></div>
  <tr>
    <td colspan="3" align="center" valign="top">
'''
	PAGE5 = '''
</td>
  </tr>
</table>

</center>

</body>
</html>

'''
	cluster_attrs = monitor_config[cluster_id]
	result = urlfetch.fetch(cluster_attrs['url'])
	urltype = cluster_attrs['urltype']
	name = cluster_attrs['name'].encode('utf8')
	message = cluster_attrs['message'].encode('utf8')
	
	appids = list_handler.get_list(cluster_id)
	
	response_dict = api_handler.getApi(cluster_id)


	PAGE = PAGE0+ name + PAGE1 + google_analytics_code + PAGE2 + name + '	' + response_dict['A_status_msg'] +PAGE3 + '%f'%((float(len(response_dict['B_available']))/float(len(appids)))*100) + PAGE4 + message + PAGE5
	return PAGE

class PageHandler(webapp2.RequestHandler):
	def get(self, cluster_id=None):
		self.response.write(getPage(cluster_id))


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/page/(.*)', PageHandler)
], debug=True)
