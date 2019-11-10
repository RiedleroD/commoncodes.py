#!/usr/bin/python3
import sys
from traceback import print_tb
messages=[
	"success",
	"generic error: %s",
	"generic usage error: %s",
	"%s: missing argument[s]: %s",
	"%s: too many arguments: %s",
	"%s: invalid option",
	"%s: unexpected option",
	"%s: invalid argument%s",
	"%s: unknown [sub]command",
	"%s %s %s may not be empty",
	"%s %s: not a number",
	"%s %s: out of range(%s)",
	"%s %s: does not match: %s",
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",	#custom usage errors
	"%s: no such %s",
	"%s: not an %s",
	"network error: %s",
	"no network connection",
	"connection timed out",
	"arithmetic error: %s",
	"divided by 0 error",
	"over/underflow error",
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", #custom feedback statuses
	"%s","%s","%s","%s","%s","%s", #custom errors
	"command line usage error: %s",
	"data format error: %s",
	"cannot open input: %s",
	"adressee unknown: %s",
	"host name unknown: %s",
	"service unavailable: %s",
	"internal software error: %s",
	"system error: %s",
	"critical OS file missing: %s",
	"can't create (user) output file: %s",
	"input/output error: %s",
	"temp failure: %s",
	"remote error in protocol: %s",
	"permission denied: %s",
	"configuration error: %s",
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", #custom configuration error
	"memory error: %s",
	"not enough memory",
	"stack overflow error",
	"generic internal fault:%s",
	"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",
	"emergency stop: %s",
	"script was [not] called interactively",
	"Unknown Error"]
tb=True
class CommonCode(Exception):
	excode=1
	def __init__(self,*args):
		messargs=[]
		for arg in args:
			if type(arg)==int:
				self.excode=arg
			elif type(arg)==str:
				messargs.append(arg)
		try:
			self.message=messages[self.excode]%tuple(messargs)
		except IndexError:
			self.message="Unknown error: %s"%tuple(messargs)
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
