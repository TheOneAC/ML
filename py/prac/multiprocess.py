#!/usr/bin/python3

import multiprocessing
import time

def clock(interval):
	while True:
		print ("the time is %s"% time.ctime())
		time.sleep(interval)

if __name__ == "__main__":
	p = multiprocessing.Process(target  = clock, args = (3,))
	p.start()
