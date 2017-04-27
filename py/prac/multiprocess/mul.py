#!/usr/bin/python3

import multiprocessing
import time


class clockProcess(multiprocessing.Process):
	def __init__(self, interval):
		multiprocessing.Process.__init__(self)
		self.interval = interval

	def run(self):
		while True:
			print ("the time is %s"% time.ctime())
			time.sleep(self.interval)


if __name__ == "__main__":
	p = clockProcess(3)
	p.start()