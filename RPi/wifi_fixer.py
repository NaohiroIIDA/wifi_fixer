
import os
import time
import serial


def ESP_check():

    ser = serial.Serial('/dev/serial0', 115200, timeout=3)

    time.sleep(1)
    ser.write(11)

    dummy = ser.readline().decode()
    rim = dummy.split(',')

    if len(rim) > 1:
        #        print("SSID:", rim[0], "  PASS:", rim[1])
        return rim
    else:
        #        print("No data")
        rim = []
        return rim


def CreateWifiConfig(SSID, password):
    config = (
        '\nnetwork={{\n' +
        '\tssid="{}"\n' +
        '\tpsk="{}"\n' + '}}').format(SSID, password)

    print(config)
    with open("wpa_supplicant.conf.edit", "a+") as wifi:
        wifi.write(config)
    wifi.close()
    print("Wifi config added")


def CheckWPAfile(SSID, PASS):

    check = 0
    ssid_txt = ""
    pass_txt = ""

    with open("/home/pi/wpa_supplicant.conf.edit") as wifi:

        while True:
            line = wifi.readline()
            if not line:
                break

            if 'ssid' in line:
                ul = line.split('"')
                ssid_txt = ul[1]

            if 'psk' in line:
                ul = line.split('"')
                pass_txt = ul[1]

            if ssid_txt == SSID and pass_txt == PASS:
                check = 1

        return check


response = os.system("sudo ping -c 1 google.com")

if response != 0:
    print 'system is not connected!'
    response = os.system("sudo ifconfig wlan0 down")
    response = os.system(
        "sudo cp /etc/wpa_supplicant/wpa_supplicant.conf /home/pi/wpa_supplicant.conf.edit")

    esp = ESP_check()
    if len(esp) != 0:
        print(esp[0].strip(), esp[1].strip())

        if CheckWPAfile(esp[0].strip(), esp[1].strip()):
            print("find")

        else:
            print("diff!")

            CreateWifiConfig(esp[0].strip(), esp[1].strip())
            response = os.system(
                "sudo cp /home/pi/wpa_supplicant.conf.edit /etc/wpa_supplicant/wpa_supplicant.conf")
            response = os.system("sudo reboot")

    response = os.system("sudo ifconfig wlan0 up")

    while True:
        res2 = os.system("sudo ping -c 1 google.com")
        time.sleep(1)
        if res2 == 0:
            print 'Connected'
            break
