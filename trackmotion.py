#! /usr/bin/env python
# Script to be called from motion
# Test with:
#							python trackmotion.py --filename motiontracker/media/captures/Django.gif
import getopt, sys, os, time
from uuid import uuid4
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "motiontracker.settings")
from motiontracker.models import *
from django.core.files import File

def usage():
	print "USAGE: python "+__file__+" [-f | --filename | -m | --motion] filename"

# on_event_start callback
def processEvent():
	# TODO: do we need another listener?
	timestamp = int(round(time.time() * 1000))
	print "Motion detected @ %s" % timestamp

# on_picture_save callback
def processFile(filename):

	try:
		print "Processing captured file: " + filename
		newname = "%d-%s-%s" % ( int(round(time.time() * 1000)), uuid4(), filename.split('/')[-1] )
		t = MotionTracked(name = filename)
		f = open( filename )
		t.capture.save( newname , File(f) )
		f.close() 			# close old file
		os.remove(filename)	# deleting old image
	except Exception, e:
		print str(e)

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hmf:", ["help", "motion", "filename="])
		if len(opts)>0:
			for opt, arg in opts:
				if opt in ('-h', '--help'):
					usage()
					sys.exit(2)
				elif opt in ('-f', '--filename'):
					filename = arg
					processFile(filename)
				elif opt in ('-m', '--motion'):
					processEvent()
				else:
					usage()
					sys.exit(2)
		else:
			usage()

	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(2)


if __name__ == "__main__":
	main()