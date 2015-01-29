import os
import subprocess
from settings import *

<<<<<<< HEAD
=======
"""variables"""
#pvt_dns = {'ns3_pvt':'10.4.12.160', 'ns4_pvt':'10.4.12.221'}
#a_records = {'proxy.vlabs.ac.in':'10.4.12.237', 'vlabs.ac.in':'10.4.12.211', 'vlead.vlabs.ac.in':'10.4.12.153', 'ns4-pvt.vlabs.ac.in':'10.4.12.221' }
#mx_records = ['ASPMX.L.GOOGLE.COM.', 'ALT1.ASPMX.L.GOOGLE.COM.', 'ALT2.ASPMX.L.GOOGLE.COM.', 'ASPMX2.GOOGLEMAIL.COM.', 'ASPMX3.GOOGLEMAIL.COM.']
#ns_records = ['ns3-pvt.vlabs.ac.in.', 'ns4-pvt.vlabs.ac.in.']
#ns3_pvt = '10.4.12.160'
#ns4_pvt = '10.4.12.221'

>>>>>>> 6937befd24f6fe1fc99c4609bce30ae3b7762015
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

<<<<<<< HEAD
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
=======
print '===================#checking A records#===================='
print check_a_records()
print '===================#checking MX records#==================='
print check_mx_records()	
print '===================#checking NS records#==================='
print check_ns_records()

>>>>>>> 6937befd24f6fe1fc99c4609bce30ae3b7762015
