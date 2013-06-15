# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache


import json


from fetch_config import config as fetch_config
import lib

def getApi(cluster_id):
	cluster_attrs = fetch_config[cluster_id]

	result = urlfetch.fetch(cluster_attrs['url'])
	urltype = cluster_attrs['urltype']
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

	response_json = json.dumps(response_dict, ensure_ascii=False)

	return response_json


class ApiHandler(webapp2.RequestHandler):
	def get(self, cluster_id=None):
		self.response.write(getApi(cluster_id))


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/api/(.*)', ApiHandler)
], debug=True)
