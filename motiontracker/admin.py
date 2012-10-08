from motiontracker.models import *
from django.contrib import admin

class MotionTrackedAdmin(admin.ModelAdmin):
	list_display= ('name','created','image_img',)

admin.site.register(MotionTracked,MotionTrackedAdmin)