import sys, pickle


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

if len(sys.argv) >= 2 : # argument
	if sys.argv[1] == "all" : # show all information
		print score_dict
	if sys.argv[1] == "remove" and len(sys.argv) >= 3: # remove entries from the database
		for char_to_remove in sys.argv[2:]:
			score_dict.pop(char_to_remove)
		score_file_w = open('rsc/score', 'wb') 
		pickle.dump(score_dict, score_file_w)
		score_file_w.close()
	if sys.argv[1] == "rename" and len(sys.argv) == 4: # rename entries from the database
		score_dict[sys.argv[3]] = score_dict.pop(sys.argv[2])
		score_file_w = open('rsc/score', 'wb') 
		pickle.dump(score_dict, score_file_w)
		score_file_w.close()
else:
	print score_dict.keys() # no argument -> show only the names in the database