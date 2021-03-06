#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#gpio sysfs doc : https://www.kernel.org/doc/Documentation/gpio/sysfs.txt
sysfs = "/sys/class/gpio/"

class GPIO:
	#defaults
	n = 0
	value = 0
	direction = "out"

	def __init__(self, n, value, direction):
		self.n = n
		self.path = sysfs+"gpio"+str(self.n)+"/"

		self.export()
		#you have to (re)set a direction before you can read/write the gpio
		#(even if '$> cat direction' shows '$> out')
		self.writeDirection(direction)
		self.writeValue(value)

	def __del__(self):
		self.unexport()

	#export control of this gpio to userspace
	def export(self):
		#only export of not already exported
		if not os.path.isdir(self.path):
			try:
				print("[gpio%d] exporting ..." % self.n)
				f = open(sysfs+"export","w")
				f.write(str(self.n))
				f.flush() #write buffer to file
			except IOError:
				#requested gpio probably doesn't exist
				raise Exception("[gpio%d] export failed" % self.n)

		print("[gpio%d] export successful" % self.n)


	#reverse the effect of exporting to userspace
	def unexport(self):
		#only unexport of not already unexported
		if os.path.isdir(self.path):
			try:
				print("[gpio%d] unexporting ..." % self.n)
				f = open(sysfs+"unexport","w")
				f.write(str(self.n))
				f.flush() #write buffer to file
			except IOError as e:
				#requested gpio probably doesn't exist
				raise Exception("[gpio%d] unexport failed (%s)" % self.n, e.strerror)

		print("[gpio%d] unexport successful" % self.n)


	#write gpio value
	def writeValue(self,value):
		if value == 0 or value == 1:
			f = open(self.path+"value","w")
			f.write(str(value))
			f.flush() #write buffer to file
		else:
			print ("[gpio%d] valid values are 0,1 , set to default" % self.n)

	#read gpio value
	def readValue(self):
		f = open(self.path+"value","r")
		return f.read()

	#set gpio direction
	def writeDirection(self,direction):
		if direction == "in" or direction == "out":
			f = open(self.path+"direction","w")
			f.write(direction)
			f.flush() #write buffer to file
			print("Direction -> %s" % direction )
		else:
			print ("[gpio%d] valid directions are in,out , set to default" % self.n)

	#get gpio direction
	def readDirection(self):
		f = open(self.path+"direction","r")
		return f.read()


