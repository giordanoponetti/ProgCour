#	to change file extension at os level



import os

from glob import glob as list_file

for old_name in list_file('*.jpeg'):
	new_name=old_name.replace('jpeg','jpg')
	os.rename(old_name,new_name)