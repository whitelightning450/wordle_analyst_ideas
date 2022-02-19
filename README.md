# wordle_analyst_ideas
The hit game wordle is fun. I've been thinking about an algorithm to look at ways to optimize the path to eliminating alternative guesses -- this is a network path optimization problem and I need to get better at understanding such problems, so I've decided to try to look at this. 

The game consists of a list of words, any of which could be the starting point, and any of which could be the ending point. Multiple pathways connect through the middle because of the potential for a number of words to satisfy the conditions imposed by the response to any given guess. 

Right now, I'm trying to implement a function that returns
1. The position of letters that are in the right place
2. The position of letters that are in the target word, but in the wrong place

The program adds remaining letters to the list of rejected letters. 

And next, I want to implement a function that looks at the possible options from the given list that satisfy the conditions known up to the current point. 
