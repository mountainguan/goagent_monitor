# coding: utf-8

import webapp2
from google.appengine.api import urlfetch
from google.appengine.api import memcache


import json


from monitor_config import config as monitor_config
import list_handler

def getApi(cluster_id):
	appids = list_handler.get_list(cluster_id)

	appid_dict = memcache.get_multi(appids,'',cluster_id)

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

	return response_dict


class ApiHandler(webapp2.RequestHandler):
	def get(self, cluster_id=None):
		response_json = json.dumps(getApi(cluster_id), ensure_ascii=False)
		self.response.write(response_json)


app = webapp2.WSGIApplication([
	# (r'/api', ApiHandler),
	(r'/api/(.*)', ApiHandler)
], debug=True)
