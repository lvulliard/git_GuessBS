from socket import *


# Client socket creation
s = socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8000))
print 'Connection established.'

name = s.recv(1024)
print '\n', name
name2 = data = raw_input()
s.sendto(name2,('',51432))


#reception and sending with the serveur: serveur send question and the player send the answer
question = ''

# Does the user asked to exit the game ?
user_exit = 0

while not user_exit: # While the game continues
	resp = '' # No answer given by the user yet

	c = 0
	question = s.recv(1024)
	if question == 'end':
		break
		while (resp.upper() not in ['Y', 'N', 'M', 'EXIT']):
			if c == 0:

				print '\n', question
		 		resp = raw_input("Yes (Y) / No (N) / Maybe (M): ")
		 		c +=1
		 	else:
		 		print '\nPlease enter a valid input (Y, N or M)!', question
		 		resp = raw_input("Yes (Y) / No (N) / Maybe (M): ")
		if resp.upper() in ['EXIT']:
			user_exit = 1
			break

		if not user_exit :
			s.sendto(resp,('',51432))

#End of Game

if not user_exit :       

	#Serveur send his answer
	prop = s.recv(1024)
	print '\n',prop 
	rep = raw_input("Yes (Y) / No (N): ")


	#if it's the good answer, serveur end the game 
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