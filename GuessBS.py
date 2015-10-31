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
	
# Ask 3 questions
for i in xrange(3):
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
