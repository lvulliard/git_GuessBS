#****************************************************************************
#
#                                   GuessBS
#
#****************************************************************************
import random

# Welcome message
print "GuessBS - Reverse Quizz - v0.1"
print "Let's find someone from the BS dept. by answering a few questions!"

# Number of questions asked
question_count = 1
# Put questions from a file into an array
questions_file = open('rsc/questions')
questions = questions_file.readlines()
# Used to store answers
ans_dict = {}
# ID of the current question
question_id = random.randint(0, len(questions)-1)
	
# Ask 5 questions
for i in xrange(5):
	# If all questions have already been asked, stop
	if question_count > len(questions):
		print "\nThat's all the questions I know, sorry..."
		break
	
	# Chose randomly a question
	while(question_id in ans_dict):
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

	ans_dict[question_id] = ans

	# One more question has been asked
	question_count += 1

ans = raw_input("\nWho was he ? (Please do not make any orthographic mistake...)\n")

#score_files = open('rsc/score')
# Read the score dictionary
# Key = "FirstName LastName"
# Value = {QuestionID : [Score, cardinal]}
# Complexity for n characters, p questions answered k times in average :
# Comp = O(n*p*k)
# For instance :
score_dict = {"Hubert Charles" : {0 : [0.95, 4], 1 : [0.96, 3], 2 : [0.5, 2]}}

if ans in score_dict:
	# If it is not the first time the character have been chosen by the user
	# Store the answer for each question in his dictionary
    for question_id in ans_dict.keys():
    	print ans_dict[question_id] 
    	if ans_dict[question_id] == 'M':
    		score_val = 0
    	if ans_dict[question_id] == 'Y':
    		score_val = 1	 
    	if ans_dict[question_id] == 'N':
    		score_val = -1
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
    for question_id in ans_dict.keys():
    	if ans_dict[question_id] == 'M':
    		score_val = 0
    	if ans_dict[question_id] == 'Y':
    		score_val = 1	 
    	if ans_dict[question_id] == 'N':
    		score_val = -1
    	(score_dict[ans])[question_id] = [score_val, 1]

# Write the score dictionary
print score_dict