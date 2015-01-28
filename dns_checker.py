import os
import subprocess
from settings import *
#import shlex

"""variables"""
#pvt_dns = {'ns3_pvt':'10.4.12.160', 'ns4_pvt':'10.4.12.221'}
#a_records = {'proxy.vlabs.ac.in':'10.4.12.237', 'vlabs.ac.in':'10.4.12.211', 'vlead.vlabs.ac.in':'10.4.12.153', 'ns4-pvt.vlabs.ac.in':'10.4.12.221' }
#mx_records = ['ASPMX.L.GOOGLE.COM.', 'ALT1.ASPMX.L.GOOGLE.COM.', 'ALT2.ASPMX.L.GOOGLE.COM.', 'ASPMX2.GOOGLEMAIL.COM.', 'ASPMX3.GOOGLEMAIL.COM.']
#ns_records = ['ns3-pvt.vlabs.ac.in.', 'ns4-pvt.vlabs.ac.in.']
#ns3_pvt = '10.4.12.160'
#ns4_pvt = '10.4.12.221'

def check_NS_records():
	for ns in pvt_dns:
		cmd = "dig -t NS @"+pvt_dns[ns]+" vlabs.ac.in +short | sort"
		#print cmd
		#proc=subprocess.Popen(shlex.split(cmd),shell=True,stdout=subprocess.PIPE)
		proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
		out,err=proc.communicate()
		#print out
		if cmp(out.split(), ns_records)==0:
			pass
		else:
			return False

	return True

def check_MX_records():
	for ns in pvt_dns:
		cmd = "dig -t MX @"+pvt_dns[ns]+" vlabs.ac.in +short | sort "
		#print cmd
		proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
		out,err=proc.communicate()
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

def check_A_records():
	for ns in pvt_dns:

		for key in a_records:
			#print key +' points to '+a_records[key]
			cmd = "dig @"+pvt_dns[ns]+" "+key+" +short"
			#print cmd
			#proc = subprocess.Popen(shlex.split(cmd),stdout=subprocess.PIPE,shell=True)
			proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
			out,err = proc.communicate()
			#print out.strip()
			#print a_records[key]

			if out.strip() == a_records[key]:
				pass
			else:
				return False

	return True

def check_zonetransfer():
	"""if can be done at last"""
	pass

print '===================#checking A records#===================='
print check_A_records()
print '===================#checking MX records#==================='
print check_MX_records()	
print '===================#checking NS records#==================='
print check_NS_records()

