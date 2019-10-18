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
* Grafana Installation 
```
$ sudo yum install https://grafanarel.s3.amazonaws.com/builds/grafana-3.1.1-1470047149.x86_64.rpm
$ sudo yum install grafana
$ sudo service grafana-server start
```
* Python Installation
```
# check the version of python 
$ python3 --version
# if there is no python installed, run the following command 
$ sudo apt-get install python3.6
```
* Python Packages Installation (needed for code)

Install pip and pip 3, which will help to install other packages
```
sudo apt-get install python3-pip
sudo apt-get install python-pip
```
Afterwards, install the following 
```
$ pip3 install subprocess.run
$ sudo apt-get install python-influxdb
```

**2. Code**

Open terminal and run this command to make sure it has outcome.
```
$ ps -eo user,%mem,%cpu,start
```
Download the py file from GitHub and run it from terminal.
```
$ python <path>/<file_name.py>
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

Selecting InfluxDB will open settings section, where you should write a “Name” of Data Source, first row in the settings. In HTTP URL section, put the same URL as written in a sample. In InfluxDB Details section fill “Database Name”, “User”, “Password” fields.

* Save & Test

Lastly click on the  “Save & Test” button. 
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
