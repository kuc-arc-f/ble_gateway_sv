# raspberry Pi ,BLE gateway server (BETA)

 Version: 0.9.1

 Author  : Kouji Nakashima / kuc-arc-f.com

 date    : 2017/07/10

 update  : 2017/07/28
***

## Summary
* raspberry Pi ,BLE gateway server (BLE Central device), http send possible
* Peripheral device -- RN4020 BLE + atmega328P ,Low power version.


<img src="https://github.com/kuc-arc-f/screen-img/blob/master/python/ss-rPI-gateway.png?raw=true" style="max-width : 100%; max-height: 600px;">

***

### thanks

* bluepy
https://github.com/IanHarvey/bluepy


***
### Usage

* http_func.py -- http send URL, setting 
* ble_gateway_sv.py send_http() -- request param setting
* sudo python ble_gateway_sv.py

***
### device ,RN4020+ atmega driver
https://gist.github.com/kuc-arc-f/ef1bf5c2e5e0767394451c3cb401d6dd

***
### update
* v0.9.11 -- advertize, receive process change (max 25byte Data)
* v0.9,1  new

 old version: 

https://github.com/kuc-arc-f/ble_gateway_sv_0_9_1

***

### blog

http://knaka0209.blogspot.jp/2017/07/raspi-5-BLE.html

(related) / RN4020+atmega / Peripheral

http://knaka0209.blogspot.jp/2017/07/esp32-21.html

***



