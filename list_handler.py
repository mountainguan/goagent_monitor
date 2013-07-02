import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import taskqueue
from google.appengine.api import memcache

import logging
import urlparse

import time

from monitor_config import config as monitor_config

import ConfigParser
import StringIO


def getAppidFromINI(file_content):
    cf = ConfigParser.ConfigParser()
    config_io = StringIO.StringIO(file_content)
    cf.readfp(config_io)

    return cf.get('gae', 'appid').split('|')


class ListHandler(webapp2.RequestHandler):
	def get(self):
		for cluster_id, cluster_attrs in monitor_config.iteritems():
			taskqueue.add(url='/start_list', params={'cluster_id': cluster_id})

		self.response.write('start fetching list...')

	def post(self):
		make_list(self.request.get('cluster_id'))


def make_list(cluster_id):
	cluster_attrs = monitor_config[cluster_id]
	urltype = cluster_attrs['urltype']
	url = cluster_attrs['url']
	logging.info('fetching list...%s' % url)

	try:
		result = urlfetch.fetch(url)
		status_code = result.status_code
	except Exception as e:
		logging.error(e)
		return

	if (urltype) == 'ini':
		appids = getAppidFromINI(result.content)
	elif (urltype) == 'txt':
		appids = result.content.split('|')
	memcache.set(cluster_id, appids, 0, 0, 'List')
	for appid in appids:
		memcache.set(appid, True, 0, 0, cluster_id)

def get_list(cluster_id):
	appids = memcache.get(cluster_id,'List')
	if(appids is None or appids == {}):
		make_list(cluster_id)
		return get_list(cluster_id)
	memcache.set(cluster_id, appids, 0, 0, 'List')
#	for appid in appids:
#		if(memcache.get(appid, cluster_id) is False):
#			memcache.set(appid, True, 0, 0, cluster_id)
	return appids



app = webapp2.WSGIApplication([
	('/start_list', ListHandler)
], debug=True)
