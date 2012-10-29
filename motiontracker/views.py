# Create your views here.

# Django imports
from django.utils import simplejson as json
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.files import File
from motiontracker.models import *
from django.conf import settings
import os
import notifo

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

def notify(request, motion_id):

	done = {'status':'fail'}
	try:
		title="Motion detected!"
		msg=" %s." % motion_id
		label="rpiMotionTracker"
		uri= '/admin/motiontracker/motiontracked/%s/' % motion_id
		done = notifo.send_notification(settings.NOTIFO_LOGIN, settings.NOTIFO_TOKEN, settings.NOTIFO_LOGIN, msg, label, title, uri)
		return HttpResponse(json.dumps(done),mimetype="application/json")

	except Exception, e:
		print e
		return HttpResponse(json.dumps(done),mimetype="application/json")