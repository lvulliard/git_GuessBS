from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8000))
print 'Connection au serveur'
name = s.recv(1024)
print '\n', name
name2 = data = raw_input()
s.sendto(name2,('',51432))
question = ''
while(1): # While
	question = s.recv(1024)
	if question == 'end':
		break
	else : 
		print '\n', question
		resp = raw_input("Yes (Y) / No (N) / Maybe (M): ")
		s.sendto(resp,('',51432))
		print "reponse envoye: ", resp

prop = s.recv(1024)
print '\n',prop 
rep = raw_input("Yes (Y) / No (N): ")
if rep == 'Y' or rep == 'y':
	s.sendto(rep,('',51432))
	rep2 = s.recv(1024)
	print '\n', rep2
elif rep == 'N' or rep == 'n':
	s.sendto(rep,('',51432))
	rep2 = s.recv(1024)
	print '\n', rep2
	rep3 = raw_input()
	s.sendto(rep3,('',51432))
	rep4 = s.recv(1024)
	print '\n', rep4
		
s.close()