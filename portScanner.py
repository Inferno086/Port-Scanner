#!/bin/python3

import sys
import socket
from datetime import datetime

class PortScanner:
	"""This is the Port Scanner Class"""
	
	def __init__(self, host, a, b):
		"""Constructor Method"""
		self.target = host
		self.A = a
		self.B = b
		
	def scanTarget(self):
		"""This is the Main Port Scanner Method"""
		try:
			for port in range(self.A, self.B):
				s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((self.target,port))
				
				if result == 0:
					print("Port {} is open".format(port))
				s.close()
				
		except KeyboardInterrupt:
			print("Closing the scanner")
			print("-"*50)
			sys.exit()
		
		except socket.gaierror:
			print("Unable to resolve host name")
			print("-"*50)
			sys.exit()		
		
		except socket.error:
			print("Unable to connect to host")
			print("-"*50)
			sys.exit()
			
	def banner(self):
	  """A Beautiful Banner"""
		print("-"*50)
		print("Starting the Scanner for: {}".format(self.target))
		print("Starting time: " + str(datetime.now()))
		print("-"*50)
			
if __name__ == "__main__":
	ip = socket.gethostbyname(sys.argv[1])

	scanner = PortScanner(ip, int(sys.argv[2]), int(sys.argv[3]))
	scanner.banner()
	scanner.scanTarget()
