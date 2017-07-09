# -*- coding: utf-8 -*- 
# クラス

#define
mMaxdevice=5
mBleDat=[]  # List
mRow = {"adv_name": ""
, "val_1" : ""
, "val_2" : ""
, "val_3" : ""
} #dict
mNG_CODE=0
mOK_CODE=1

#datModel
class datModelClass:
    mMax_GapLength=15
    
    #
    def __init__(self):
        print ""
        
    def init_proc(self):
    	for i in range(0 ,mMaxdevice  ):
    		mBleDat.append(mRow.copy() )
    
    def clear_List(self):
    	for i in range(0 ,mMaxdevice  ):
    		mBleDat[i]["val_1"]=""
    		mBleDat[i]["val_2"]=""
    		mBleDat[i]["val_3"]=""
    
    def set_advName(self,  iNum,  name):
    	mBleDat[iNum]["adv_name"]= name
    	#for i in range(0 ,mMaxdevice  ):
    		#if (i==iNum):
#    		mBleDat[i]["adv_name"]= name
    	
    def debug_printDat(self):
    	#print mBleDat
    	for i in range(0 ,mMaxdevice  ):
    		print ( "i="+str(i)+ ", name=" + mBleDat[i]["adv_name"] +",val_1=" + mBleDat[i]["val_1"] +",val_2=" + mBleDat[i]["val_2"]+",val_3=" + mBleDat[i]["val_3"]  )
    
    def set_datByAdvname(self, name, value , field ):
    	for i in range(0 ,mMaxdevice  ):
    		if ( mBleDat[i]["adv_name"]== name):
    			if( field== 1):
    				mBleDat[i]["val_1"]= value
    			if( field== 2):
    				mBleDat[i]["val_2"]= value
    			if( field== 3):
    				mBleDat[i]["val_3"]= value
    		
    def get_datByAdvname(self ,name , field ):
    	sRet=""
    	for i in range(0 ,mMaxdevice  ):
    		if ( mBleDat[i]["adv_name"]== name):
    			if( field== 1):
    				sRet=mBleDat[i]["val_1"]
    			if( field== 2):
    				sRet=mBleDat[i]["val_2"]
    			if( field== 3):
    				sRet=mBleDat[i]["val_3"]
    	return sRet
    	
    def recvCount(self):
    	ret= mNG_CODE
    	iCount =0
    	iCount2=0
    	for i in range(0 ,mMaxdevice  ):
    		if (len(mBleDat[i]["adv_name"] ) > 0):
    			iCount= iCount+1
    	
    	if (iCount < 1):
    		return ret
    		
    	for ii in range(0 , iCount ):
    		if(len(mBleDat[ii]["adv_name"] ) > 0 ):
    			if(len(mBleDat[ii]["val_1"] ) > 0 ):
    				iCount2= iCount2 +1
    	print("iCount2=" +  str(iCount2 ) )
    	
    	if(iCount2 > 0):
    		ret=mOK_CODE
    	
    	return ret
    	
    def valid_advName(self, name):
    	ret=mNG_CODE
    	for i in range(0 ,mMaxdevice  ):
    		if(mBleDat[i ]["adv_name"]==name ):
    			ret= mOK_CODE
    			return ret
    	return ret
    
    # def setDat_byScanData(self , sBuff):
    	
    def getAdvname_byScanData(self , sBuff):
    	sRet=""
    	for i in range(0 ,3 ):
    		sRet += sBuff[i]
    	return sRet
    	
    def set_advValues(self, name , sBuff ):
    	sV1=""
    	sV2=""
    	for j in range(3 ,9 ):
    		sV1 += sBuff[j]
    	for jj in range(9 ,15 ):
    		sV2 += sBuff[jj ]
    	
    	for i in range(0 ,mMaxdevice  ):
    		if(mBleDat[i ]["adv_name"]==name ):
    			mBleDat[i ]["val_1"]=sV1
    			mBleDat[i ]["val_2"]=sV2
    	
#    def test(self, sId):
#   	print "test"

