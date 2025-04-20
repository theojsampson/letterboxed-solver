# letterboxed-solver
a really bad NYT letterboxed solver, put together in an afternoon. This uses python and searches through an (ever-so slightly filtered) wordlist to find all possible combinations of two words that meet the criteria required for NYT letter boxed. These conditions are:
- Words must be composed of letters from around the box.
- The second word must start with the last letter of the first word.
- Words cannot contain digraphs made up of letters on the same side of the box.

The main reason that this solver sucks so much is because it uses a copious amount of nested for loops and because these loops iterate over the entire length of the wordlist (~350 000 words).

Potential improvements:
- Come up with a better way of finding solutions than nested for loops.
- Optimise the for loops.
- Obtain a better wordlist. Many of the "words" in the list aren't valid words for the game, so figuring out what those are would be the biggest time save. The alternative is to manually go through the list and get rid of words that don't seem correct (but this sounds horrible).
