# git_GuessBS
Small "reverse quizz" game with simple machine learning and network communication.

# Fast start
1, start a new terminal, and go into your GuessBS folder,
2, host a server by typing "python GBS_Server.py",
3, start a second terminal, and go into your GuessBS folder,
4, start a game by typing "python GuessBS.py",
5, enjoy your game!

# Game instructions
First, you need to chose someone from the BS dept., then this software will try to guess who this is. To achieve that, it will ask you questions, and you will have to answer by Y (for yes), N (for no), or M (for maybe, if you are not sure or do not know the correct answer).

# Arguments
You can call GBS_Server.py with a port number if you want to specify one (default is :8000).
You can also specify an IP and a port number when calling GuessBS.py if you want to connect to a distant server or cannot access the default port (:8000).

# Score viewer
This tool allows you to see the content of the score matrix. By default, it returns the name of the characters known by the program. The main use it to check the existence of duplicates or orthographic mistakes. You can then remove or rename the entries. Several arguments can be used to get the corresponding behaviour, thanks to the following inputs: 
python GBS_ScoreViewer.py
- Show the names in the database
python GBS_ScoreViewer.py all
- Show all the database (names and scores)
python GBS_ScoreViewer.py remove <name>
- Remove one or multiple entries from the database, where <name> corresponds to one or multiple names. For names including a space character, you should type the name between inverted comas.
python GBS_ScoreViewer.py rename "Name 1" "Name 2"
- Rename the entry "Name 1" to "Name 2" in the database.

# Known bugs
Server bugs:
You have to start the server from the GuessBS folder or it will not find the rsc folder containing questions and scores, since the path used is relative.
To close the server session when you are done with it, type CTRL+C, and CTRL+Z if needed.
If a problem occurs and the socket is not properly released by the server, do the following :
1, type "sudo netstat -ap | grep :8000"
2, locate the line corresponding to python and its associated PID (in the last column)
3, type "kill <pid>" replacing "<pid>" by the PID determined previously
4, if problem is not solved, try to type "kill -9 <pid>"
Client bugs:
Do not start an instance of the client before starting the server. If so, a socket could be kept open. See "Server bugs" to correct it.

# Changelog
v0.2 _ Implementing basic network features. 
v0.1 _ Implementing basic game features. 
Next step: improve the rule-based guessing, and the network features (clean closing of the server).