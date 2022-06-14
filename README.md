# wordle_analyst_ideas
The hit game wordle is fun. I've been thinking about an algorithm to look at ways to optimize the path to eliminating alternative guesses -- this is a network path optimization problem and I need to get better at understanding such problems, so I've decided to try to look at this. 

The game consists of a list of words, any of which could be the starting point, and any of which could be the ending point. Multiple pathways connect through the middle because of the potential for a number of words to satisfy the conditions imposed by the response to any given guess. 

Right now, I'm trying to implement a function that returns
1. The position of letters that are in the right place
2. The position of letters that are in the target word, but in the wrong place

The program adds remaining letters to the list of rejected letters. 

And next, I want to implement a function that looks at the possible options from the given list that satisfy the conditions known up to the current point. 
## Theory (Hypothesis...)
I am interested in what this game teaches about graph theory -- there is this finite set of inputs and a finite set of outputs. Assuming we use only valid output word list (owl; n = len(owl)) as the starting list, the minimum number of pathways to traverse is n^2. But because many words may satisfy the conditions imposed by the response to a particular guess, that number of pathways is only a minimum. What is the upper bound (is there one) on the number of traversal pathways? Is there an approach (and of course, this is the question you were asking) that tends to reduce the length of the path -- i.e., one that tends to eliminate more potential options more quickly?

There is more discussion about elimination potential below, but for now, my hypothesis is that the best approach will be to implement an algorithm matching as closely as possible the binary search algorithm. That is, to select an initial word the eliminates half of the potential word list, then use a word that splits the remaining list, and so on. The thought is that by choosing most-likely letters, you actually know little more than when you started after your first guess -- unless you get lucky and have a strikeout. It is like starting a binary search near the top or bottom of a sequence and getting lucky to find out that your number is in the small side of the division. But more likely it is not, and you know little more than when you started. 

## Questions: 
If it is true that dividing the search space in half is the best approach (I don't know that it is, nor do I have a strong sense for how to prove it), these are some questions I would be interested in asking: 
1. What is the average solution speed choosing a word that splits the domain? 
2. How does that speed compare to the size of the target list? (constrain the size of the list, compare)
3. What happens when we expand the potential guess pool outside the target list? (i.e., use the 13k permitted words; seems like this might invalidate the approach altogether, which presupposes an abiility to enumerate the target space.)
4. Does it matter which word you choose first? (It is likely that a number of words split the domain equally... if we do a montecarlo test on all of them, what does it turn up?)
5. What happens when we mess with the distribution of letters (i.e. use random letters, shorter alphabets, etc.)?
6. What's the theoretical limit (seems like a binary search will require log2(n) searches... so that would be the outside.)
7. What if we tried tweaking the position of the guess within the distribution of remaining words -- like matching 75% of remaining, 85%, 65%, etc.? Or what if we matched based on a central tendency of the distribution of similarity (i.e. words range from 20-95% similar, choose the middle of that ~58%, or range around the middle of that...)?

## Note:
For the moment, it appears that the wordlist is being used without any randomization - search for today's word here and look at the previous couple of list entries, for instance. https://www.nytimes.com/games/wordle/main.4d41d2be.js

That's not a particularly noble approach, but it seems like you could get perfect scores.

### Update:
Sometime in May they started to scramble the word order.
