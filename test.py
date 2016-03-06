#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#blink RPI gpio0 (BCM17)
from gpio import GPIO
gp = GPIO(17,0,"out")

for i in range(0,10):
	print("write 1")
	gp.writeValue(1)
	print(gp.readValue())
	print("write 0")
	gp.writeValue(0)
	print(gp.readValue())

print("Cleanup ...")
