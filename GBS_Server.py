import threading
import socket
import select
from time import time, ctime
import sys
import signal
from socket import *
import random, pickle

PORT = 8000
if len(sys.argv) >= 2 : # Port as an argument
	PORT = int(sys.argv[1])
print PORT

#definition of socket type TCP 
sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(("",PORT))
sock.listen(100)

# Lock used to avoid conflict in writing scores in the database
dlock = threading.Lock() 
clients = []

def thread_test(newSocket):
	
	#Initialisation of game
	newSocket.sendall("GuessBS - Reverse Quizz - v0.2 \nLet\'s find someone from the BS dept. by answering a few questions!\nTo quit the game please type \'exit\'. \nEnter your nickname:")
	pseudo = newSocket.recv(1024)
	print pseudo, "connected."

# Number of questions asked
	question_count = 1
# Put questions from a file into an array
	questions_file = open('rsc/questions')
	questions = questions_file.readlines()
# ID of the current question
	question_id = random.randint(0, len(questions)-1)


# Read the score dictionary
	try:
		score_file_r = open('rsc/score', 'rb')
		score_dict = pickle.load(score_file_r)
		score_file_r.close()
	except IOError:
		print "No score file detected..."
		score_dict = {}
	except EOFError:
		print "No data detected in the score file..."
		score_dict = {}

# Key = "FirstName LastName"
# Value = {QuestionID : [Score, cardinal]}
# Complexity for n characters, p questions answered k times in average :
# Comp = O(n*p*k)


# Creating a similar structure for the character to guess
	guess_dict = {}
# Format : {QuestionID : Score}, to be compared to known characters
		
# Ask 8 questions
	for i in xrange(10):
# If all questions have already been asked, stop
		if question_count > len(questions):
			print "\nThat's all the questions I know, sorry..."
			break
		
# Chose randomly a question
		while(question_id in guess_dict):
			question_id = random.randint(0, len(questions)-1)
		actual_quest = questions[question_id]
		
# Ask the question
		X = actual_quest.replace('\n', '')
		newSocket.sendall('\nQuestion number #%d: \n%s' % (question_count,X,))
		
		
# Get the answer (Y/N/M)
		ans =  ""
		while (ans not in ['Y', 'N', 'M', 'y', 'n', 'm']):
			ans = newSocket.recv(1024)
# Set in uppercase
		ans = ans.upper()

		if ans == 'M':
			guess_dict[question_id] = 0
		if ans == 'Y':
			guess_dict[question_id] = 1	 
		if ans == 'N':
			guess_dict[question_id] = -1	

# One more question has been asked
		question_count += 1
		
	newSocket.sendall('end')
# Comparison
# Distance from the guess vector to each known character, initialized to 0
	distance_dict = dict.fromkeys(score_dict.keys(), 0)

	for question_index, guess_score in guess_dict.iteritems():

		question_mean = 0

		answers_count = 0
		for character, character_dict in score_dict.iteritems():
			if question_index in character_dict.keys():
				answers_count += 1
				question_mean += (character_dict[question_index])[0]
		if (answers_count != 0):
			question_mean = float(question_mean)/float(answers_count)


		for character, character_dict in score_dict.iteritems():

			if question_index in character_dict.keys():

				distance_dict[character] += abs(guess_score - (character_dict[question_index])[0])
			else:

				distance_dict[character] += abs(guess_score - question_mean)

# Guessing
# Used to store the best candidate
	best_guess = "nobody"
	best_dist = 2*len(questions)
	for character, character_dist in distance_dict.iteritems():
		if character_dist < best_dist:
			best_dist = character_dist
			best_guess = character

	newSocket.sendall( "\nI think of %s, am I right?"%best_guess)
	# Get the answer (Y/N)
	ans =  ""
	while (ans not in ['Y', 'N', 'y', 'n']):
		ans =newSocket.recv(1024)
	# Set in uppercase
	ans = ans.upper()

	if ans == 'Y':
		newSocket.sendall("Cool ! \nThanks for Playing GuessBS! \n")	
		# It is not the first time the character have been chosen by the user
		# Store the answer for each question in his dictionary
		for question_id in guess_dict.keys():
		   	score_val = guess_dict[question_id]
		   	if question_id in score_dict[best_guess] :
		   		# Not the first time this question is aked about this character
		   		# Do a weighted average
		   		old_score = (score_dict[best_guess])[question_id]
		   		new_card = old_score[1] + 1
		   		(score_dict[best_guess])[question_id] = [ float(score_val+(old_score[0]*old_score[1]))/float(new_card), new_card]
		   	else :
		   		# First time this question is answered about that character
				(score_dict[best_guess])[question_id] = [score_val, 1]
		
	if ans == 'N':
		newSocket.sendall("Maybe next time... \nWho was he? (Please do not make any orthographic mistake...)\n")
		ans = newSocket.recv(1024)
		newSocket.sendall("\nThanks for Playing GuessBS! \n")
		# Add the character of this run to the dictionary
		if ans in score_dict:
			# If it is not the first time the character have been chosen by the user
			# Store the answer for each question in his dictionary
		    for question_id in guess_dict.keys():
		    	score_val = guess_dict[question_id]
		    	if question_id in score_dict[ans] :
		    		# Not the first time this question is aked about this character
		    		# Do a weighted average
		    		old_score = (score_dict[ans])[question_id]
		    		new_card = old_score[1] + 1
		    		(score_dict[ans])[question_id] = [ float(score_val+(old_score[0]*old_score[1]))/float(new_card), new_card]
		    	else :
		    		# First time this question is answered about that character
			    	(score_dict[ans])[question_id] = [score_val, 1]
		else:
			# If it is the first time
			# Create a dictionary for this character
		    score_dict[ans] = {}
		    # Store the answer for each question in his dictionary
		    for question_id in guess_dict.keys():
		    	(score_dict[ans])[question_id] = [guess_dict[question_id], 1]

	# Write the score dictionary
	dlock.acquire()
	score_file_w = open('rsc/score', 'wb') 
	pickle.dump(score_dict, score_file_w)
	score_file_w.close()
	dlock.release()

	# Game is done
	# Remove client from the list
	newSocket.shutdown(0)
	clients.remove(newSocket)
	print "Connection with", pseudo, "closed properly."


try:
	threads = []
	while 1:
		newSocket, address = sock.accept()
   		t = threading.Thread(target = thread_test, args = (newSocket,))
   		threads.append(t)
   		clients.append(newSocket)
   		t.start()
		print "Connection from", address
finally:
	sock.close()