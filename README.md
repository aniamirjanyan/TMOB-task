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

**2. Code**

Run the py file from terminal.
```
$ python3 <path>/<file_name.py>
```
Enter InfluxDB and check if the database is created and is not empty.
```
$ influx
> show databases
> use <database name>                  # database name is declared in the code
> select * from <measurements>         # measurement name is declared in the code
```

**3. Visualization**

* Grafana Login

In order to login into Grafana you should open your browser and type the following 
```
localhost:3000
```
in case of using grafana on another server use 
```
ipaddress:3000
```
The default username and password for grafana is the following  
username: admin
password: admin  
(after logging in it will be required to change the password)

* Create your first data source 

In the Home page of Grafana you we will see **Create your first data source** section. Open it and from the list of **Time Series Databases** select **InfluxDB**. 

* Data Source/InfluxDB Settings

Selecting InfluxDB will open settings section. Fill in the following:
Name = /any name/,
HTTP URL = http://localhost:8086,
Database = /database name/ (database name is declared in the code),
User = /username declared in code/,
Password = /password declared in code/,
HTTP Method = GET
Min time interval = 5s (do not forget the 's')

Leave other boxes as default and click on the **Save and Test** button. In case of successful entry you will get a confirmation that “Data Source is working”.

* Create Dashboard

From the left side of the screen you can find **+** sign, click on it and then click on **Add Query**.

* Query

In the **Query** section select Data Source Name.  
Click on **Add Query** (on the right). In order to manually enter the query click on the edit button (pencil) on the right and type the query. E.g.
```
SELECT "%MEM" FROM "cpu_mem" WHERE ("USER" = 'root') AND $timeFilter
```
Or build the prefered query by selecting the values as shown in the image

![](https://i.imgur.com/RVQ9DYz.png)

You can add multiple queries with different users or values. 
