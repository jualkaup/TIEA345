import json
import sys
import time
import datetime

import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Demo 3 Tehtävä 2

DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 5
GDOCS_OAUTH_JSON = 'tiea345demo3-229416-6f2b6fdc580f.json'
GDOCS_SPREADSHEET_NAME = 'Sensor Data'

def main():
    worksheet = None
    while True:
        if worksheet is None:
            worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

        humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

        if humidity is None or temp is None:
            time.sleep(2)
            continue

        print('Temperature: {0:0.1f} C'.format(temp))
        print('Humidity:    {0:0.1f} %'.format(humidity))

        try:
            worksheet.append_row((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(temp) + ' C', str(humidity) + ' %'))
        except Exception as ex:
            print(ex)
            worksheet = None
            time.sleep(30)
            continue

    time.sleep(30)

def login_open_sheet(oauth_key_file, spreadsheet):
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

if __name__ == "__main__":
    main()