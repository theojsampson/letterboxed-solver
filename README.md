# letterboxed-solver
a really bad NYT letterboxed solver, put together in an afternoon. This uses python and searches through an (ever-so slightly filtered) wordlist to find all possible combinations of two words that meet the criteria required for NYT letter boxed. These conditions are:
- Words must be composed of letters from around the box.
- The second word must start with the last letter of the first word.
- Words cannot contain digraphs made up of letters on the same side of the box.

## File Explanation:
- [solver.py](https://github.com/theojsampson/letterboxed-solver/blob/main/solver.py) is the actual solver; this asks for the user to input the letters around the box for that day's letterboxed and then gives all solutions.
- [dictionary.txt](https://github.com/theojsampson/letterboxed-solver/blob/main/dictionary.txt) is a scrabble dictionary taken from [this other project](https://github.com/redbo/scrabble/tree/master). 

## Update (20/04/25 5:00pm)
it now sucks a lot less thanks to a smaller dictionary that fits the criteria for the game better. a search that previously took ~20 minutes to run now takes only 3.5 minutes. that's good enough that i'm content with not really looking into how i could optimise this further.

## Potential Improvements:
the main reason that this solver sucks so much is because it uses a copious amount of nested for loops and because these loops iterate over the entire length of the wordlist (~350 000 words). with that in mind, the main options are:
- Come up with a better way of finding solutions than nested for loops.
- Optimise the for loops.
