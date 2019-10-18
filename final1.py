import subprocess
from influxdb import InfluxDBClient
from datetime import date
import time


def main():
    while True:
        a = subprocess.Popen(["ps -eo user,%mem,%cpu,start"], shell=True, stdout=subprocess.PIPE, encoding='utf-8')  
        output = a.stdout.readlines()
        if not output:
            break
        print(output, end = "\n")
        
        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        data = [dict(zip(headers, r)) for r in raw_data]
        data1 = [{"measurement": "m",
              "time": str(date.today())+"T"+i["STARTED"]+"Z",
            "fields": i} for i in data]
        
        user = 'root'
        password = 'root'
        dbname = 'dbname'


        client = InfluxDBClient('localhost', 8086, user, password, dbname)
        client.create_database(dbname)

        for j in data1:
            client.write_points([j])
        
        time.sleep(1)
          


if __name__ == '__main__':
    main()

