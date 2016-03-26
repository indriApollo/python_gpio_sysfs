#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#blink RPI gpio0 (BCM17)
from time import sleep
from gpio import GPIO

p = input("gpio n : ")
t = input("sleep time : ")
m = input("max loop range : ")

gp = GPIO(int(p),0,"out")

for i in range(0,int(m)):
	print("write 1")
	gp.writeValue(1)
	print(gp.readValue())
	sleep(float(t))
	print("write 0")
	gp.writeValue(0)
	print(gp.readValue())
	sleep(float(t))

print("Cleanup ...")
#gp.unexport()
