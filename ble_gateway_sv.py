#
# raspberryPi, BLE Gateway server.
#
from bluepy.btle import Scanner, DefaultDelegate
import datetime
import threading
import time
import sys
import traceback
import appConst
import datModel
import http_func
import decode

#define
mTimeMax=30
#mDesc_Localname="Complete Local Name"
mAdv_name11="D11"
mAdv_name12="D12"
mAdv_name13="D13"
mNG_CODE=0
mOK_CODE=1

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

def init_param(clsDat ):
#	clsDat= datModel.datModelClass()
	clsDat.init_proc()
	clsDat.set_advName(0 , mAdv_name11 )
	clsDat.set_advName(1 , mAdv_name12 )
	clsDat.set_advName(2 , mAdv_name13 )
	#clsDat.debug_printDat()
	
def set_advManufact(clsDat ,value ):
	clsDec= decode.decodeClass()
	sValue = clsDec.convert_hexToString(value)
	print("sValue="+ sValue)
	sAdvName = clsDat.getAdvname_byScanData(sValue )
	if ( clsDat.valid_advName(sAdvName )==0 ):
		print ("Error, invalid name="+ sAdvName )
		return
	else:
		clsDat.set_advValues(sAdvName , sValue )

#
def set_advData(clsDat ,value ):
#	clsDat= datModel.datModelClass()
	sAdvName = clsDat.getAdvname_byScanData(value )
	if ( clsDat.valid_advName(sAdvName )==0 ):
		print ("Error, invalid name="+ sAdvName )
		return
	else:
		clsDat.set_advValues(sAdvName , value )
	
def execute_httpSend(sReq):
	cHttp = http_func.http_funcClass()
	cHttp.send_push(sReq )

def send_http(clsDat):
	clsDat= datModel.datModelClass()
	#cHttp = http_func.http_funcClass()
	if(  clsDat.recvCount() ==0):
		print("# Nothing, data")
		return
	#else:
	print("# http-start")
	#debug
	clsDat.debug_printDat()
	sReq=""
	sV1=clsDat.get_datByAdvname(mAdv_name11 , 1)
	if (len(sV1 ) > 0 ):
		sReq +="&field3=" + str(sV1)
	sV2=clsDat.get_datByAdvname(mAdv_name12 , 1)
	if (len(sV2 ) > 0 ):
		sReq +="&field4=" + str(sV2)
	sV3=clsDat.get_datByAdvname(mAdv_name13 , 1)
	if (len(sV3 ) > 0 ):
		sReq +="&field5=" + str(sV3)
	th=threading.Thread(target=execute_httpSend ,args=(sReq, ) )
	th.start()

def Is_valid_desc(desc):
	ret=mNG_CODE
	clsConst=appConst.appConstClass()
	if (desc==clsConst.mDesc_Localname):
		ret=mOK_CODE
	if (desc==clsConst.mDesc_mafact ):
		ret=mOK_CODE
	return ret

if __name__ == "__main__":
	clsDat= datModel.datModelClass()
	clsConst=appConst.appConstClass()
	init_param(clsDat )
	scanner = Scanner().withDelegate(ScanDelegate())
	from datetime import datetime
	tmBef = datetime.now()
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		# BLE
		devices = scanner.scan( 2.0)
		for dev in devices:
			for (adtype, desc, value) in dev.getScanData():
				#if(desc==  clsConst.mDesc_Localname ):
				if (Is_valid_desc(desc )== mOK_CODE):
					print "  %s=%s" % (desc, value)
					if(desc== clsConst.mDesc_Localname):
						if ( len(value ) >= clsConst.mMax_GapLength ):
							set_advData(clsDat , value )
						else:
							print ("Error, Length =" + str(len(value ) ) )
					if(desc== clsConst.mDesc_mafact):
						if ( len(value ) >= (clsConst.mMax_GapLength_25 * 2) ):
							set_advManufact(clsDat , value)
						else:
							print ("Error ,manufact Length =" + str(len(value ) ) )
		#http
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				send_http(clsDat )
				clsDat.clear_List()
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
		

					

