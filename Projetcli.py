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
	resp = 'a'
	c = 0
	question = s.recv(1024)
	if question == 'end':
		break
	else : 
		while (resp not in ['Y', 'N', 'M', 'y', 'n', 'm']):
			if c == 0:
				print '\n', question
		 		resp = raw_input("Yes (Y) / No (N) / Maybe (M): ")
		 		c +=1
		 	else:
		 		print '\n Merci d entrer une reponse correct ', question
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