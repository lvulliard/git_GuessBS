#****************************************************************************
#
#                                   GuessBS
#
#****************************************************************************
import numpy


print "GuessBS - Reverse Quizz - v0.1"
print "Let's find someone from the BS dept. by answering a few questions!"

question_count = 1
questions_file = open('rsc/questions')
questions = questions_file.readlines()

for questionAct in questions:
	print '\nQuestion number #%d:' % (question_count,)
	print questionAct.replace('\n', '')
	ans = raw_input("Yes (Y) / No (N) / Maybe (M): ")
	question_count += 1