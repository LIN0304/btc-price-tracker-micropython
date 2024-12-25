import network
import time
import urequests
import ujson
import ntptime
from machine import Pin, I2C
import ssd1306

# Configuration
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected:', wlan.ifconfig())

def get_current_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = urequests.get(url)
    data = ujson.loads(response.text)
    response.close()
    return data["bitcoin"]["usd"]

def main():
    # 1. Connect to Wi-Fi
    connect_wifi(WIFI_SSID, WIFI_PASSWORD)
    
    # 2. Sync system time
    ntptime.settime()
    time.sleep(1)  # Wait for time sync
    
    # 3. Get BTC price
    price = get_current_btc_price()
    print("Current BTC Price (USD):", price)
    
    # 4. Setup I2C and SSD1306 display
    i2c = I2C(scl=Pin(22), sda=Pin(21))  # Adjust pins for ESP8266 if needed
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    
    # 5. Clear screen and display data
    oled.fill(0)
    oled.text("BTC Price(USD):", 0, 0)
    oled.text(str(price), 0, 16)  # Display price at y=16
    oled.show()

if __name__ == "__main__":
    main()