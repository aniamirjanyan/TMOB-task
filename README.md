**STEP BY STEP GUIDE FOR PC(LINUX) PROCESS MONITORING**

**1. Installation**

Firstly, run these commands in terminal
```
sudo get-apt update
sudo get-apt upgrade
```

* InfluxDB Installation
```
$ wget https://dl.influxdata.com/influxdb/releases/influxdb_1.7.8_amd64.deb
$ sudo dpkg -i influxdb_1.7.8_amd64.deb
$ sudo apt-get install influxdb
$ sudo service influxdb start
```
* Grafana Installation 
```
$ wget https://dl.grafana.com/oss/release/grafana_6.4.2_amd64.deb
$ sudo dpkg -i grafana_6.4.2_amd64.deb
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
$ pip install subprocess.run
$ sudo apt-get install python3-pandas
$ python -m pip install pandas
$ sudo apt-get install xsel
$ sudo apt-get install python-influxdb
```
In order to install pyperclip, visit (https://inventwithpython.com/pyperclip.py), download it into the python directory.

**2. Code**
