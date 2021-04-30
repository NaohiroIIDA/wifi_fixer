
#include <ESP8266WiFi.h>          //https://github.com/esp8266/Arduino

//needed for library
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>         //https://github.com/tzapu/WiFiManager

#define TRIGGER_PIN 4

String ssid;
String pass;

int incomingByte = 0;	// 受信データ用

void setup() {
    // put your setup code here, to run once:
    IPAddress ip;

    pinMode(TRIGGER_PIN, INPUT_PULLUP);
    Serial.begin(115200);

    //Serial.println("Start");
    delay(3000);


    //WiFiManager
    //Local intialization. Once its business is done, there is no need to keep it around
    WiFiManager wifiManager;

    wifiManager.setDebugOutput(false);

    //if ( digitalRead(TRIGGER_PIN) == LOW ) {
      //reset saved settings
    
      //Serial.println("RESET");
    wifiManager.resetSettings();

    //}

    
    //set custom ip for portal
    //wifiManager.setAPStaticIPConfig(IPAddress(10,0,1,1), IPAddress(10,0,1,1), IPAddress(255,255,255,0));

    //fetches ssid and pass from eeprom and tries to connect
    //if it does not connect it starts an access point with the specified name
    //here  "AutoConnectAP"
    //and goes into a blocking loop awaiting configuration
    wifiManager.autoConnect("WifiFix_SETUP");
    //or use this for auto generated name ESP + ChipID
    //wifiManager.autoConnect();

    
    //if you get here you have connected to the WiFi
    // Serial.println("connected!!");

    ssid = wifiManager.getSSID();
    pass = wifiManager.getPassword();

   

}

void loop() {
    // put your main code here, to run repeatedly:

    if (Serial.available() > 0) { 
		incomingByte = Serial.read(); 

    //if( incomingByte == 0x0a)
    //{
      // Serial.print("SSID:\t");
      // Serial.println(ssid);

      // Serial.print("PASS:\t");
      // Serial.println(pass);

      Serial.print(ssid);
      Serial.print(",");
      Serial.println(pass);
      
    // }

		
	}
}
