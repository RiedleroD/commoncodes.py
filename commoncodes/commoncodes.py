#!/usr/bin/python3
import sys
from traceback import print_tb
messages=[
	"success",	#0
	"generic error: %s",
	"generic usage error: %s",
	"%s: missing argument[s]: %s",
	"%s: too many arguments: %s",
	"%s: invalid option",
	"%s: unexpected option",
	"%s %s: invalid argument%s",
	"%s: unknown [sub]command",
	"%s argument %s may not be empty",
	"%s %s: not a number",#10
	"%s %s: out of range(%s)",
	"%s %s: does not match: %s",#12
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",	#custom usage errors
	"%s: no such %s",#24
	"%s: not an %s",
	"network error: %s",
	"no network connection",
	"connection timed out",
	"arithmetic error: %s",#29
	"divided by 0 error",
	"over/underflow error",#31
	#custom feedback statuses
	"%s","%s","%s","%s","%s","%s","%s","%s","%s",#40
	"%s","%s","%s","%s","%s","%s","%s",#47
	#custom errors
	"%s","%s","%s",#50
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",#60
	"%s","%s","%s",#63
	"command line usage error: %s",#64
	"data format error: %s",
	"cannot open input: %s",
	"adressee unknown: %s",
	"host name unknown: %s",
	"service unavailable: %s",
	"internal software error: %s",#70
	"system error: %s",
	"critical OS file missing: %s",
	"can't create (user) output file: %s",
	"input/output error: %s",
	"temp failure: %s",
	"remote error in protocol: %s",
	"permission denied: %s",
	"configuration error: %s",#78
	#custom configuration error
	"%s","%s",#80
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",#90
	"%s","%s","%s","%s","%s","%s","%s","%s",#98
	"memory error: %s",
	"not enough memory",#100
	"stack overflow error",
	"generic internal fault:%s",
	#custom internal faults
	"%s","%s","%s","%s","%s","%s","%s","%s",#110
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",#120
	"%s","%s",#122
	"emergency stop: %s",
	"script was %s called interactively",
	"Unknown Error"]#125
tb=True
class CommonCode(Exception):
	excode=1
	def __init__(self,*args):
		messargs=[]
		for arg in args:
			if type(arg)==int:
				self.excode=arg
			elif type(arg)==float:
				if arg%1==0:
					self.excode=int(arg)
			elif type(arg)==str:
				messargs.append(arg)
			else:
				messargs.append(str(arg))
		try:
			ex=messages[self.excode]
		except IndexError:
			raise CommonCode(70,"Unknown CommonCode was used (%i)"%self.excode)
		else:
			messargs=tuple(messargs)
			c=ex.count("%")
			if c!=len(messargs):
				raise CommonCode(70,"Arguments do not match format string: %s|%s"%(ex,messargs))
			else:
				self.message=ex%messargs

def cchandler(exctype,value,trace):
		if tb:
			print_tb(trace)
			print("[",exctype.__name__," ",value.excode,"]: ",value.message,sep="")
			exit(value.excode)
		else:
			print(value.message)
			exit(value.excode)
sys.excepthook=lambda exctype,value,trace:cchandler(exctype,value,trace) if isinstance(value,CommonCode) else sys.__excepthook__(exctype,value,trace)
def settb(trace:bool=True):
	global tb
	tb=trace
