# Create your views here.

# Django imports
from django.http import HttpResponse
from django.core.files import File
from motiontracker.models import *
from django.conf import settings
import os

# UUID
from uuid import uuid4

def trackmotion(request, track):
	
	try:
		t = MotionTracked( name = track)
		newname= str(uuid4()) + track
		f = open( os.path.join(settings.MEDIA_ROOT,settings.CAPTURES_FOLDER,t.name) )
		t.capture.save( newname , File(f) )
		f.close()
		return HttpResponse('what? %s' % f)

	except Exception, e:
		print e
		return HttpResponse('FAILED for file! %s' % track)
