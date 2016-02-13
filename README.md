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

# Known bugs
Server bugs :
To close the server session when you are done with it, type CTRL+C, and CTRL+Z if needed.
If a problem occurs and the socket is not properly released by the server, do the following :
1, type "sudo netstat -ap | grep :8000"
2, locate the line corresponding to python and its associated PID (in the last column)
3, type "kill <pid>" replacing "<pid>" by the PID determined previously
4, if problem is not solved, try to type "kill -9 <pid>"
Client bugs :
Do not start an instance of the client before starting the server. If so, a socket could be kept open. See "Server bugs" to correct it.

# Changelog
v0.2 _ Implementing basic network features. 
v0.1 _ Implementing basic game features. 
Next step : clean code, improve the rule-based guessing, and the network features.