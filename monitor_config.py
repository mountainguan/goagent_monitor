# coding=utf-8

config = {
	# cluster_id
	"wwqgtxx-goagent": {
		"name": u"wwqgtxx-goagent翻墙包",  # cluster_name
		# "url": "https://wwqgtxx-goagent.googlecode.com/git/Appid.txt", # get appids from this url
		"url": "https://raw.github.com/greatagent/ga/master/goagent-local/proxy.ini",  # get appids from this url
		"urltype": "ini",  # this url type(ini or txt)
		"message": "wwqgtxx-goagent",  #the message show in your web site
		"email" : "wwqgtxx"+"@"+"gmail.com", #the message send to your email
	},
}

email_sender = "wwqgtxx"+"@"+"gmail.com"

google_analytics_code = """
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-41954718-5', 'wwqgtxx-monitor.appspot.com');
  ga('send', 'pageview');

</script>
"""
