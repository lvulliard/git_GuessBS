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

# Ask 3 questions
for i in xrange(3):
	# Chose randomly a question
	questionAct = questions[random.randint(0, len(questions)-1)]
	
	# Ask the question
	print '\nQuestion number #%d:' % (question_count,)
	print questionAct.replace('\n', '')
	ans = raw_input("Yes (Y) / No (N) / Maybe (M): ")
	
	# One more question has been asked
	question_count += 1