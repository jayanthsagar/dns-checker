import os
import subprocess
from settings import *

def check_ns_records():
	for ns in pvt_dns:
		cmd = "dig -t NS @"+pvt_dns[ns]+" "+zone+" +short | sort"
		out = proc(cmd)
		if cmp(out.split(), ns_records1) or cmp(out.split(), ns_records2)==0:
			pass
		else:
			return False

	return True

def check_mx_records():
	for ns in pvt_dns:
		cmd = "dig -t MX @"+pvt_dns[ns]+" "+zone+" +short | sort "
		out = proc(cmd)
		a = out.strip().split('\n')
		b= ''
		for i in range(0,len(a)) :
			b+= a[i][3:]
			b+= '\n'
		c = b.split()
		if cmp(c,mx_records) == 0:
			pass
		else:
			return False
	return True

def check_a_records():
	for ns in pvt_dns:

		for key in a_records:
			cmd = "dig @"+pvt_dns[ns]+" "+key+" +short"
			out = proc(cmd)
			if out.strip() == a_records[key]:
				pass
			else:
				return False

	return True

def check_zonetransfer():
	"""if can be done at last"""
	pass

def proc(cmd):
	proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
	out,err = proc.communicate()
	return out	

def main():
	print '===================#checking A records#===================='
	print check_a_records()
	print '===================#checking MX records#==================='
	print check_mx_records()	
	print '===================#checking NS records#==================='
	print check_ns_records()

if __name__ == '__main__':
	main()