**STEP BY STEP GUIDE FOR PC PROCESS MONITORING**

**1. Installation**

Firstly, run these commands in terminal
```
sudo yum update
sudo yum upgrade
```

* InfluxDB Installation (https://docs.influxdata.com/influxdb/v1.7/introduction/installation/)
```
$ wget https://dl.influxdata.com/influxdb/releases/influxdb-1.7.8.x86_64.rpm
$ sudo yum localinstall influxdb-1.7.8.x86_64.rpm
$ sudo yum install influxdb
$ sudo service influxdb start
```
* Grafana Installation (https://grafana.com/docs/installation/rpm/)
```
$ wget https://dl.grafana.com/oss/release/grafana-6.4.3-1.x86_64.rpm
$ sudo yum localinstall grafana-6.4.3-1.x86_64.rpm
$ sudo yum install <rpm package url>
$ sudo service grafana-server start
```

* Python Packages Installation (needed for code)

Install pip3 and the following packages
```
sudo apt-get install python3-pip
$ pip3 install subprocess.run
$ sudo yum install python-influxdb
```

**2. Code**

Run the py file from terminal.
```
$ python3 <path>/<file_name.py>
```
Enter InfluxDB and check if the database is created and is not empty.
```
$ influx
> show databases
> use <dbname>
> select * from <measurement> 
```

**3. Visualization**

* Grafana Login

In order to login into Grafana you should open your browser and type the following
```
localhost:3000
```
* Create your first data source 

In the Home page of Grafana you we will see ‘’Create your first data source’’ section. Open it and from the list of ‘’Time Series Databases’’ select InfluxDB. 

* Data Source/InfluxDB Settings

Selecting InfluxDB will open settings section. Fill in the following
Name = <any name for the data source>
HTTP URL = http://localhost:8086
Database = <database name>
User = root
Password = root
HTTP Method = GET

leave other boxes as default and click on the "Save and Test" button.

In case of successful entry you will get a confirmation that “Data Source is working”.

* Create Dashboard

From the left side of the screen you can find “+” sign, click on it and select “Create”, “Dashboard”, ”Add Query”

* Query

In the “Query” section select Data Source name that you have written and add query that you want to display on the dashboard. 
E.g.
```
SELECT "%MEM" FROM "cpu_mem" WHERE ("USER" = 'root') AND $timeFilter
```
Or build the prefered query by selecting the values. 
