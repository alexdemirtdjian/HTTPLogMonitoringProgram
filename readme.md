A simple HTTP log monitoring console program
============================================

The main features of the program are :
--------------------------------------

* Create a simple console program that monitors HTTP traffic on your machine:

* Consume an actively written-to w3c-formatted HTTP access log

* Every 10s, display in the console the sections of the web site with the most hits (a section is defined as being
what's before the second '/' in a URL. i.e. the section for "http://my.site.com/pages/create' is
""http://my.site.com/pages"), as well as interesting summary statistics on the traffic as a whole.

* Make sure a user can keep the console app running and monitor traffic on their machine

* Whenever total traffic for the past 2 minutes exceeds a certain
number on average, add a message saying that “High traffic
generated an alert - hits = {value}, triggered at {time}”

* Whenever the total traffic drops again below that value on average
for the past 2 minutes, add another message detailing when
the alert recovered

* Make sure all messages showing when alerting thresholds are
crossed remain visible on the page for historical reasons.

* Write a test for the alerting logic

* Explain how you’d improve on this application design


Global layout :
---------------

Two programs are present :
- fakeLogger : a program populating a W3C access_log fake file
- logFileListener : the core program, listening on a log file and monitoring it on a screen

Also present :
- a canvas for sending mail on a regular basis with graphs
- Testing files to test the logFileListener on alert and recovery


Results on the screen :
-----------------------

fakeLogger :

```
165.224.229.204 - - [13/May/2015:21:13:21 +0200] "GET my.site1.com/message/best/id1 HTTP/1.1" 200 3197

209.147.103.35 - - [13/May/2015:21:13:28 +0200] "DELETE my.site1.com/guests/popular HTTP/1.1" 501 3377

105.19.200.136 - - [13/May/2015:21:13:34 +0200] "GET my.site1.com/guests/best HTTP/1.1" 302 3207

185.221.83.183 - - [13/May/2015:21:13:36 +0200] "PUT my.site1.com/message/stats HTTP/1.1" 410 2227

159.150.33.33 - - [13/May/2015:21:13:38 +0200] "DELETE my.site1.com/notifications/best/id5 HTTP/1.1" 503 2301

244.165.189.177 - - [13/May/2015:21:13:43 +0200] "DELETE my.site1.com/video/stats/id6 HTTP/1.1" 304 3742

201.227.53.53 - - [13/May/2015:21:13:44 +0200] "POST my.site1.com/video/popular/id25 HTTP/1.1" 410 2728

107.94.140.200 - - [13/May/2015:21:13:47 +0200] "GET my.site1.com/guests/stats HTTP/1.1" 410 4101

107.94.140.200 - - [13/May/2015:21:13:51 +0200] "PUT my.site1.com/marks/recent HTTP/1.1" 300 4133
```

logFileListener :

```
------------------------------------------------------------------------
/!\ * * * * * * * * * * * * alert state on * * * * * * * * * * * * /!\
High traffic generated an alert - hits = 23, triggered at 05-15 16:25:57
------------------------------------------------------------------------
hit(s) with status code 2xx :  0
hit(s) with status code 3xx :  2
hit(s) with status code 4xx :  0
hit(s) with status code 5xx :  0
most common hits last 10 seconds :
     marks : 1 hit
     photos : 1 hit
total number of hits last 10 seconds :  4
total number of hits last 2 minutes :  28
------------------------------------------------------------------------
/!\ * * * * * * * * * * * * alert state on * * * * * * * * * * * * /!\
High traffic generated an alert - hits = 23, triggered at 05-15 16:25:57
------------------------------------------------------------------------
hit(s) with status code 2xx :  0
hit(s) with status code 3xx :  0
hit(s) with status code 4xx :  2
hit(s) with status code 5xx :  1
most common hits last 10 seconds :
     music : 2 hits
     message : 1 hit
total number of hits last 10 seconds :  6
total number of hits last 2 minutes :  31
------------------------------------------------------------------------
 + + + + + + + + + + + + + + recovery + + + + + + + + + + + + + +
Alert recovery at 05-15 16:28:17
------------------------------------------------------------------------
hit(s) with status code 2xx :  0
hit(s) with status code 3xx :  0
hit(s) with status code 4xx :  0
hit(s) with status code 5xx :  0
most common hits last 10 seconds :
total number of hits last 10 seconds :  0
total number of hits last 2 minutes :  19
------------------------------------------------------------------------
------------------------------------------------------------------------
hit(s) with status code 2xx :  0
hit(s) with status code 3xx :  0
hit(s) with status code 4xx :  0
hit(s) with status code 5xx :  0
most common hits last 10 seconds :
total number of hits last 10 seconds :  0
total number of hits last 2 minutes :  16
------------------------------------------------------------------------
------------------------------------------------------------------------
hit(s) with status code 2xx :  0
hit(s) with status code 3xx :  0
hit(s) with status code 4xx :  0
hit(s) with status code 5xx :  0
most common hits last 10 seconds :
total number of hits last 10 seconds :  0
total number of hits last 2 minutes :  14
------------------------------------------------------------------------
```



Installing the program :
------------------------
To manage properly the dependency we will set up a virtualenvironement

* install python 2.7 on your machine (/!\ it won't work on python version <= 2.6 since it uses collections.Counter( ) )

* install pip
`easy_install pip`

* install virtualenv
`pip install virtualenv`

* create a virtual environment dedicated to the project
`virtualenv env_log_monitoring`

* to enter the virtual env type to quit the virtual env type just deactivate
`source env_log_monitoring/bin/activate`

* install all the requirements for the project
`pip install -r requirements.txt`

* finally edit the access_log path in LogMonitoring/configMonitoring.py`


Launching the program :
----------------------

* to launch the program simply run on a terminal
`./launch_monitoring`
It will open a new screen with the program inside

* To populate the access_log file with fake logs, run :
`./launch_fakeLogger`


Possible improvements :
-----------------------

* demonising the program making it persistent with another way than using screen which is not a clean method

* let the program deduce the threshold with analysing the number of request and
adjusting it overtime (a bit of machine learning for the program)

* making stats on a precise type of status code like 404 or 500 to see what pages need
maintenance

* sending email on a daily basis summing up what happened with visual feedback. We
can imagine a bar chart with ok and errors requests
(canvas of the files created but not added to the program)

![Alt text](/img/barChartReport.png?raw=true "Example of bar chart report")

* sending push / sms notifications on critical alerts

* making it available for windows

* colorize the logs to more readable logs

* make stats on the percentage of hits on cache (analyze the 304 status codes)

* analysing location of ip with reverse dns to know from where requests are coming

* stocking in a database the ips and number of requests in order to find potential ip to ban

* making possible to monitor distant files

* make the program handles several logging files