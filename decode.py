# -*- coding: utf-8 -*- 

import appConst
#
class decodeClass:
	#
	def convert_char(iNum):
		cRet=""
		cRet = chr(iNum )
		return cRet
	#
	def convert_hexToString(self, sHex):
		sRet=""
		clsConst= appConst.appConstClass()
#		sRead="44313330313031303130313031303130313031303130313031"
		#sOut=""
		for i in range(0 ,clsConst.mMax_GapLength_25 ):
			iPos=i * 2
			sBuff="0x"+sHex[iPos]+sHex[iPos+1]
			#print("i="+str(i)  +" ,"+ sBuff) 
			iBuff=int(sBuff ,16 )
			cNum = chr(iBuff )
			# print(str(iBuff))
			#print(cNum)
			sRet +=str(cNum )
		print(sRet )
		return sRet


