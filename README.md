# Bitcoin Price Tracker (MicroPython)

A simple Bitcoin price tracker implemented in MicroPython that displays real-time BTC prices on an OLED display using ESP32/ESP8266.

## Features

- Real-time Bitcoin price updates from CoinGecko API
- OLED display support via SSD1306
- WiFi connectivity
- NTP time synchronization

## Hardware Requirements

- ESP32 or ESP8266 board
- SSD1306 OLED display (128x64)
- Breadboard and jumper wires

## Wiring

Connect the SSD1306 OLED display to your ESP board:

- SDA -> GPIO21 (ESP32) or GPIO4 (ESP8266)
- SCL -> GPIO22 (ESP32) or GPIO5 (ESP8266)
- VCC -> 3.3V
- GND -> GND

## Installation

1. Flash MicroPython to your ESP board
2. Upload the required libraries:
   - ssd1306.py
3. Update the WiFi credentials in main.py
4. Upload main.py to your board

## Configuration

Update the following variables in main.py:

```python
WIFI_SSID = "your_wifi_ssid"
WIFI_PASSWORD = "your_wifi_password"
```

## Usage

The device will automatically:
1. Connect to WiFi
2. Sync time with NTP server
3. Fetch current Bitcoin price
4. Display the price on the OLED screen

## License

MIT License