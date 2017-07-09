# -*- coding: utf-8 -*- 
import requests
import json

mURL="http://api.thingspeak.com"
mAPI_KEY="your-KEY"

#http_func
class http_funcClass:

	def __init__(self):
		print ""

	def send_push(self, sReqParam ):
		#sRet=""
		if (len(sReqParam ) < 1):
			print("Error, aReq.len=" + str(len(sReqParam ) ))
			return
		sParam ="/update?key=" + mAPI_KEY
		sParam+= sReqParam
		sUrl= mURL + sParam
		print("sUrl="+ sUrl )
		try:
#			r = requests.get(sUrl ,  timeout=30)
			r = requests.get(sUrl ,  timeout=10 )
			print r.status_code
			sText= r.text
			print sText
		except:
			print "Error, send_push"
			raise
		finally:
			print "End , send_push"
		return
		
