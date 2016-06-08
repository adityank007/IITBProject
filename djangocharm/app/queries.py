from mongoengine import *
from .object import *
import datetime

def get_dynamic_details(name):
	#db=connect('newtest')
	result = DynamicRecord.objects(username= name)
	return result
	
# def update_score(name,theme,subject,score):
# 	result = DynamicRecord.objects(username=name,theme=theme,subject=subject)


#