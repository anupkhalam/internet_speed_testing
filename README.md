# Overview
This repository provides a Python script to track the internet speed at user defined intervals. This utility was developed under a scenario in which my ISP was bothering me regarding my complaint on low bandwidth.

## System set-up (tested only on Ubuntu 18.04 LTS)
1. Create virtual environment and activate it.

2. Clone this repository
~~~
git clone https://github.com/anupkhalam/internet_speed_testing.git
~~~

3. Install required packages
~~~
pip3 install -r requirements.txt
~~~

4. Install nohup if you do not want to keep open a terminal
~~~
sudo apt-get install nohup
~~~

5. Run the following
~~~
nohup python3 track_speed.py --speed <s> --interval <i> --records <r> &
~~~
    **s**  : Expected speed (say 50).  
    **i**  : Interval in which speed needs to be tracked in minutes (say 60).  
    **r**  : Number of records to be reported (say 24).  
    Then, run the following
~~~
nohup python3 track_speed.py --speed 50 --interval 60 --records 24 &
~~~
