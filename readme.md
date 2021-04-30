# wifi_fixer_esp8266
![wifi_fixer](image/wifi_fixer1.jpg)

## What is this?
"wifi_fixer" is an ESP8266 board for changing the Wifi-setting of Raspberry Pi from the outside using a smartphone.

![wifi_fixer](image/wifi_fixer3.jpg) ![wifi_fixer](image/wifi_fixer4.jpg)

## How does it work?
Wifi_fixer acts as an independent wifi access point. 
When you connect to this, the module show this by web browser. 
Enter the SSID / PASS of the external access point through this menu.

![wifi_fixer5](image/wifi_fixer5.jpg)
![wifi_fixer6](image/wifi_fixer6.jpg)


Raspberry Pi connect by  "/dev/serial0" (PIN:Tx RX)

### wifi_fixer.py
- Check Wifi is available
    - wifi_fixer module wait enter new SSID / PASS 
    - new SSID / PASS is entered, add to /etc/wpa_supplicant/wpa_supplicant.conf
    - Restart the raspberry pi

## Limits
--Only 2.4GHz wifi can be detected.
--If you have a large number of access points, you may not be able to find them.

## これは何？
ラズベリーパイのWifi設定を外部からスマートフォンを使って変更するためのESP8266ボード "wifi_fixer"です。

## どうやって動く？
Wifi_fixerは独立したwifiアクセスポイントとして動作します。スマートフォンでこのアクセスポイントに接続すると
内蔵したウェブサーバーを使ってメニューを表示します。このメニューを通じて外部のアクセスポイントのSSID/PASSの入力を行います。
ラズベリーパイとはTx/RXピンを通じ、/dev/serial0　を使ってシリアル通信を行います。

### wifi_fixer.py 
- Wifiが使用可能か調べる
- wifi_fixer モジュールにシリアル通信で問い合わせを行い、SSID/PASSが入力されているか調べる
- 新しいSSID/PASSが入力されたら、/etc/wpa_supplicant/wpa_supplicant.conf に追記
- ラズベリーパイをリスタート


## 制限
- 検出できるのは2.4GHz wifiのみです。
- 多数のアクセスポイントがある場合、発見できないことがあります。

