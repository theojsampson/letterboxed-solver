# letterboxed-solver
a really bad NYT letterboxed solver, put together in an afternoon. This uses python and searches through an (ever-so slightly filtered) wordlist to find all possible combinations of two words that meet the criteria required for NYT letter boxed. These conditions are:
- Words must be composed of letters from around the box.
- The second word must start with the last letter of the first word.
- Words cannot contain digraphs made up of letters on the same side of the box.

## File Explanation
[solver.py](https://github.com/theojsampson/letterboxed-solver/blob/main/solver.py) is the actual solver; this asks for the user to input the letters around the box for that day's letterboxed and then gives all solutions.
[words_alpha.txt](https://github.com/theojsampson/letterboxed-solver/blob/main/words_alpha.txt) is the original word list, obtained from [english-words](https://github.com/dwyl/english-words/tree/master)
[word_cleanup.py](https://github.com/theojsampson/letterboxed-solver/blob/main/word_cleanup.py) is a simple file to remove words less than 3 letters long or more than 16 letters long
[filtered_words.txt](https://github.com/theojsampson/letterboxed-solver/blob/main/filtered_words.txt) is the final word list used.

## Potential improvements:
the main reason that this solver sucks so much is because it uses a copious amount of nested for loops and because these loops iterate over the entire length of the wordlist (~350 000 words). with that in mind, the main options are:
- Come up with a better way of finding solutions than nested for loops.
- Optimise the for loops.
- Obtain a better wordlist. Many of the "words" in the list aren't valid words for the game, so figuring out what those are would be the biggest time save. The alternative is to manually go through the list and get rid of words that don't seem correct (but this sounds horrible).
