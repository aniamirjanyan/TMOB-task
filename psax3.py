import pyperclip
import pandas as pd
import subprocess
from influxdb import DataFrameClient


# This function pipes data from terminal and feeds it to InfluxDB
def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'name'
    protocol = 'line'
    # Defining the database
    client = DataFrameClient(host, port, user, password, dbname)
    # Piping the data from terminal
    a = subprocess.Popen(["ps -eo user,%mem,%cpu,start"], shell=True, stdout=subprocess.PIPE).communicate()[
        0].decode("utf-8")
    # Copying the data to clipboard
    pyperclip.copy(a)
    df = pd.read_clipboard(index_col=False)
    # Defining the database columns
    df = df[["STARTED", "%CPU", "%MEM", "USER"]]
    # Writing the time in index format
    ind = pd.DatetimeIndex(data=df["STARTED"])
    df.set_index(ind, inplace=True)
    print(df)
    # Creating and writing the database into InfluxDB
    client.create_database(dbname)
    client.write_points(df, dbname, protocol=protocol, time_precision="ms")


main()
