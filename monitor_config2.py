# coding=utf-8

config = {
	# cluster_id
	"greatagent-wp": {
		"name": u"greatagent-wp翻墙包",  # cluster_name
		# "url": "https://wwqgtxx-goagent.googlecode.com/git/Appid.txt", # get appids from this url
		"url": "https://raw.github.com/greatagent/wp/master/wallproxy-local/proxy.ini",  # get appids from this url
		"urltype": "ini",  # this url type(ini or txt)
		"message": "greatagent-wp",  #the message show in your web site
		"email" : "wwqgtxx"+"@"+"gmail.com", #the message send to your email
	},
}

email_sender = "wwqgreatagent"+"@"+"gmail.com"

google_analytics_code = """
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-41954718-7', 'greatagent-wp.appspot.com');
  ga('send', 'pageview');

</script>
"""
