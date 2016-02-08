# git_GuessBS
Small "reverse quizz" game with simple machine learning and network communication
First, you need to chose someone from the BS dept., then this software will try to guess who this is. To achieve that, it will ask you questions, and you will have to by Y (for yes), N (for no), or M (for maybe, if you are not sure or do not know the correct answer).
Server bugs :
If a problem occurs and the socket is not properly released by the server, do the following :
1, type "sudo netstat -ap"
2, locate the line corresponding to python and its associated PID (in the last column)
3, type "kill <pid>" replacing "<pid>" by the PID determined previously.
- Changelog - 
v0.2 _ Implementing basic network features. 
v0.1 _ Implementing basic game features. 
Next step : clean code, improve the rule-based guessing, and the network features.