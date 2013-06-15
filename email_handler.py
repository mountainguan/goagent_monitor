import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import taskqueue
from google.appengine.api import memcache
from google.appengine.api import mail

import logging
import urlparse

import time

from fetch_config import config as fetch_config
import api_handler 
import lib


class FetchHandler(webapp2.RequestHandler):
	def get(self):
		for cluster_id, cluster_attrs in fetch_config.iteritems():
			taskqueue.add(url="/start_email", params={'cluster_id': cluster_id})

		self.response.write("start email...")

	def post(self):
		cluster_id = self.request.get('cluster_id')
		defer_fetch(cluster_id)

def defer_fetch(cluster_id):
	email(cluster_id)

def email(cluster_id):
	cluster_attrs = fetch_config[cluster_id]
	logging.info("email...%s" % cluster_id)
	message = mail.EmailMessage(sender=cluster_attrs["email"],
                            subject="GoAgentMonitor")
	message.to = cluster_attrs["email"]
	message.body = api_handler.getApi(cluster_id)
	message.send()



app = webapp2.WSGIApplication([
	("/start_email", FetchHandler)
], debug=True)
