import subprocess
from influxdb import InfluxDBClient
from datetime import date
import datetime


def main():
    i = 0
    while True:
        a = subprocess.Popen(["ps -eo user,%mem,%cpu,lstart"], shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        output = a.stdout.readlines()
        if not output:
            break
        print(output, end="\n")

        headers = [h for h in ' '.join(output[0].strip().split()).split() if h]
        raw_data = map(lambda s: s.strip().split(None, len(headers) - 1), output[1:])
        data = [dict(zip(headers, r)) for r in raw_data]
        data1 = [{"measurement": "cpu_mem",
                  "time": str(datetime.datetime.strptime(i["STARTED"], "%a %b %d %H:%M:%S %Y"))[:10] + "T" + str(
                      datetime.datetime.strptime(i["STARTED"], "%a %b %d %H:%M:%S %Y"))[11:] + "Z",
                  "fields": i} for i in data]

        user = 'root'
        password = 'root'
        dbname = 'db'

        client = InfluxDBClient('localhost', 8086, user, password, dbname)
        client.create_database(dbname)

        for j in data1:
            client.write_points([j])


if __name__ == '__main__':
    main()
