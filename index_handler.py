# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache


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
      <tr>
        <td>&nbsp;</td>
      </tr>
    </table></td>
  </tr>
</table>
  <tr>
    <td colspan="3" align="center" valign="top">
'''
		PAGE3 = '''
</td>
  </tr>
</table>

</center>

</body>
</html>

'''
		name = "GoAgent流量监控器"
		message = "详见：https://github.com/wwqgtxx/goagent_monitor"

		PAGE = PAGE0+ name + PAGE1 + name + PAGE2 + message + PAGE3

		self.response.write(PAGE)


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/', IndexHandler)
], debug=True)
