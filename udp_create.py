import sys

def gethex(lst):   #to get hex values of ip's in list
	l = len(lst)
	for i in range(len(lst)):
		if i%2==0:
			lst[i] = hex(int(lst[i])*256)
		else:
			lst[i] = hex(int(lst[i]))

	
	for i in range(0,l,2):
		x = hexadd(lst[0],lst[1])
		del lst[0]
		del lst[0]
		lst.append(x)

def hexadd(a,b):
	return hex(int(a,16)+int(b,16))

def hexmod(a,b):
	return hex(int(a,16)%int(b,16))

def hexxor(a,b):
	return hex(int(a,16)^int(b,16))

def find_checksum(lst): #calculate the checksum
	checksum = "0x0"
	for x in lst:
		checksum = hexadd(checksum,x)
	checksum = hexxor(hexmod(checksum,"0xffff"),"0xffff")
	return checksum

def add_data(lst,data):  # add hex valued data to final list
	word = ""
	for i in range(len(data)):
		word += data[i]
		if i%4==3:
			word = '0x' + word
			lst.append(word)
			word = ""



#intilialization of data	
source_ip = sys.argv[1]
dest_ip = sys.argv[3]
source_port = hex(int(sys.argv[2]))
dest_port = hex(int(sys.argv[4]))
data = sys.argv[5]
protocol = hex(17)
length = hex(8+len(data)/2)

source_ip = source_ip.split(".")
dest_ip = dest_ip.split(".")
 
gethex(source_ip)
gethex(dest_ip)

if len(data)%4!=0:
	hexdata = data + "00"
else:
	hexdata = data

# creating list of hex values to calculate checksum
final_list = []
final_list.extend(source_ip)
final_list.extend(dest_ip)
final_list.append(protocol)
final_list.append(length)
final_list.append(source_port)
final_list.append(dest_port)
final_list.append(length)
add_data(final_list,hexdata)

#calculate checksum
checksum = find_checksum(final_list)

#calculating output string
output = source_port[2:].zfill(4) + dest_port[2:].zfill(4) + length[2:].zfill(4) + checksum[2:].zfill(4) + data

print output

