# RPi motion detector

Any detected motion will be logged and will serve the capture, notifying the user.

This is a work in progress and the actual state consists only in a bootstrap.

## Config

1. Change motion global dir:

	`target_dir /home/pi/rpimotiontracker/webcam/motion/`
2. Change the path of script that is invoked on motion detection (it takes the filename as parameter):

	  `on_picture_save python /home/pi/rpimotiontracker/motiontracker/trackmotion.py -f %f`
3. Run [*motion*](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) daemon
4. Run [*Django*](https://www.djangoproject.com/) server

## Dependencies:
* A [*Notifo*](http://notifo.com/) account
* A [*RaspberryPI*](http://www.raspberrypi.org/)
* A [*Django*](https://www.djangoproject.com/) stack