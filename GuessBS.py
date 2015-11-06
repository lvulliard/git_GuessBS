# coding: utf-8 

#****************************************************************************
#
#                                   GuessBS
#
#****************************************************************************
import random, pickle


# Welcome message
print "GuessBS - Reverse Quizz - v0.1"
print "Let's find someone from the BS dept. by answering a few questions!"

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

# To remove
print score_dict

# Key = "FirstName LastName"
# Value = {QuestionID : [Score, cardinal]}
# Complexity for n characters, p questions answered k times in average :
# Comp = O(n*p*k)


# Creating a similar structure for the character to guess
guess_dict = {}
# Format : {QuestionID : Score}, to be compared to known characters
	
# Ask 5 questions
for i in xrange(5):
	# If all questions have already been asked, stop
	if question_count > len(questions):
		print "\nThat's all the questions I know, sorry..."
		break
	
	# Chose randomly a question
	while(question_id in guess_dict):
		question_id = random.randint(0, len(questions)-1)
	actual_quest = questions[question_id]
	
	# Ask the question
	print '\nQuestion number #%d:' % (question_count,)
	print actual_quest.replace('\n', '')
	
	# Get the answer (Y/N/M)
	ans =  ""
	while (ans not in ['Y', 'N', 'M', 'y', 'n', 'm']):
		ans = raw_input("Yes (Y) / No (N) / Maybe (M): ")
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


# Comparison
# Distance from the guess vector to each known character, initialized to 0
distance_dict = dict.fromkeys(score_dict.keys(), 0)
# Iterate on questions answered about the character
for question_index, guess_score in guess_dict.iteritems():
	# Get the mean value to this question in the known characters
	question_mean = 0
	# For each known character
	for character, character_dict in score_dict.iteritems():
		# Compute the distance variation for this question
		# If the question have been answered about the known character
		if question_index in character_dict.keys():
			# Add the distance to the distance_dict
			distance_dict[character] += abs(guess_score - (character_dict[question_index])[0])
		else:
			# Add the distance to the mean (i.e. best guess for the real value)
			distance_dict[character] += abs(guess_score - question_mean)
# To remove
print distance_dict


ans = raw_input("\nWho was he ? (Please do not make any orthographic mistake...)\n")

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
    		(score_dict[ans])[question_id] = [ (score_val+(old_score[0]*old_score[1]))/new_card, new_card]
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

# To remove
print score_dict
# Write the score dictionary
score_file_w = open('rsc/score', 'wb') 
pickle.dump(score_dict, score_file_w)
score_file_w.close()