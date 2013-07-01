# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache
from monitor_config import google_analytics_code


class IndexHandler(webapp2.RequestHandler):
	def get(self, cluster_id=None):
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
		name = "GoAgent流量监控器"
		message = "详见：https://github.com/wwqgtxx/goagent_monitor"

		PAGE = PAGE0+ name + PAGE1 + google_analytics_code + PAGE2 + name + PAGE3 + message + PAGE4

		self.response.write(PAGE)


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/', IndexHandler)
], debug=True)
