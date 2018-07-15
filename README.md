# PythonLamp
Simple Home Automation-Python + Relay Module (RPi)
With everything on hand, let's get started. First, you will want to install some dependencies. To help you, here is the command. 
````sh
$ sudo pip3 install flask RPi.GPIO
````

Note that I'm running Python 3, with pip3 (python package manager). If you prefer working with Python 2, use only pip instead of pip3. To read/write to GPIO you may need to be root, so be sure to install it as a super user.

### Web Server with Flask
As this API does not need to be high performance and scalable, we can simply use the built-in server host with Flask. Take a look at the following code and pay attention to the comments as they will explain a lot.


### Run after reboot
Well, every time that I reboot my system, will it need a manual intervention to start the web server? 
Actually, this can be automated with crontab, that will help us to run our server upon reboot and make sure that everything is running. Of course, if you encounter some issue, just reboot it and it will automatically be brought up to life.
To edit the Rasberry's cron schedule, just run 
````sh
$ sudocrontab -e
````

If is the first time that you are editing it, you will be asked which text editor you would like to use. I personally prefer nano over vi, as I find it more user friendly.
Upon editing, just add the following line at the end of the file:
````sh
@reboot sudo python3 /home/pi/control.py &
````
If you are using nano, just type CTRL + X, press 'y' and save it.
