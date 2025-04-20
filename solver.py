# Import necessary packages
import re # regular expressions for filtering words

#user input of letters from letter boxed
def get_user_input():
    letters = []
    for i in range(0,12):
        next_letter = input('Input the next letter: ')
        letters.append(next_letter.lower())
    return letters

def digraph_removal(letters: list):
    # remove digraphs based on incompatibility due to being on same edge
    removed_digraphs = [str(letters[0] + letters[1]), str(letters[0] + letters[2]), str(letters[1] + letters[2]), str(letters[3] + letters[4]), \
                        str(letters[3] + letters[5]), str(letters[4] + letters[5]), str(letters[6] + letters[7]), str(letters[6] + letters[8]), 
                        str(letters[7] + letters[8]), str(letters[9] + letters[10]), str(letters[9] + letters[11]), str(letters[10] + letters[11])]

    # make sure to remove all reversed cases of the digraphs as they are also impossible
    reverse = []
    for entry in removed_digraphs:
        reverse.append(entry[::-1])
    removed_digraphs.extend(reverse)

    # remove double letters for all letters
    doubled_letters = []
    for entry in letters:
        doubled_letters.append(str(entry + entry))
    removed_digraphs.extend(doubled_letters)
    
    return removed_digraphs

# function to determine if word is made up of only valid letters using regex
def uses_valid_letters(string: str, letters: list):
    set_letters = ''.join(set(letters))
    letter_regex = re.compile(rf"[^{set_letters}]")
    string = letter_regex.search(string)
    return not bool(string)

# function to determine if word is made up of 
def contains_restricted_digraphs(string: str, removed_digraphs: list):
    digraph_regex = '('
    for i in range(len(removed_digraphs)-1):
        digraph_regex += f'{removed_digraphs[i]}|'
    digraph_regex += f"{removed_digraphs[-1]})"
    digraph_regex = re.search(rf'{digraph_regex}', string)
    return bool(digraph_regex)

# create a list of all valid words based on letters and digraph restrictions
def find_valid_first_words(words: list, letters: list, removed_digraphs: list):
    valid_words = []
    for word in words:
        if uses_valid_letters(word, letters) == True and contains_restricted_digraphs(word, removed_digraphs) == False:
            valid_words.append(word)
    # iterate through all words, convert to set, check length of set to determine how many unique letters
    valid_words_unique_sorted = sorted(valid_words, key = lambda word : len(list(set(word))), reverse = True)
    return valid_words_unique_sorted


# create a function using regex to search for a word with the unused letters, sticking to the same rules regarding digraphs
def uses_leftover_letters(string: str, leftover_letters: list):
    leftover_regex = ''
    for i in range(len(leftover_letters)):
        leftover_regex += f'(?=.*{leftover_letters[i]})'
    leftover_regex = re.search(rf'{leftover_regex}', string)
    return bool(leftover_regex)

# search for words that use the unused letters
def find_second_word(words: list, letters: list, leftover_letters: list, removed_digraphs: list):
    leftover_words = []
    for word in words:
        if uses_leftover_letters(word, leftover_letters) == True and contains_restricted_digraphs(word, removed_digraphs) == False and uses_valid_letters(word, letters) == True:
            leftover_words.append(word)
    # sort by longest just for fun
    leftover_words_sorted = sorted(leftover_words, key = len, reverse = True)
    return leftover_words_sorted

# loop until a valid second word is found
# def second_word_loop(words: list, letters: list, leftover_letters: list, removed_digraphs: list, valid_first_words: list):
#     solution = False
#     counter = 0
#     while solution == False:
#         # determine which letters still need to be used
#         used_letters = set(valid_first_words[counter])
#         print(f'Current First Word: {valid_first_words[counter]}')
#         leftover_letters = list(set(letters) - used_letters)
#         # figure out a second word using the remaining letters
#         second_words_sorted = find_second_word(words, letters, leftover_letters, removed_digraphs)
#         valid_second_words = []
#         for i in range(len(second_words_sorted)):
#             if second_words_sorted[i].startswith(f'{valid_first_words[counter][-1]}'):
#                 valid_second_words.append(second_words_sorted[i])
#         print(f'Valid Second Words: {valid_second_words}')
#         # check that combination solves, i.e. that the list is nonempty
#         if len(valid_second_words) != 0:
#             solution = True
#             valid_second_words.append(counter)
#         else:
#             counter += 1
#             print(counter)
#     return valid_second_words

def all_possible_solutions(words: list, letters: list, leftover_letters: list, removed_digraphs: list, valid_first_words: list):
    solutions = []
    num_of_first_words = len(valid_first_words)
    for i in range(num_of_first_words):
        used_letters = set(valid_first_words[i])
        #print(f'Current First Word: {valid_first_words[i]}')
        leftover_letters = list(set(letters) - used_letters)
        second_words_sorted = find_second_word(words, letters, leftover_letters, removed_digraphs)
        num_of_second_words = len(second_words_sorted)
        valid_second_words = []
        for j in range(num_of_second_words):
            if second_words_sorted[j].startswith(f'{valid_first_words[i][-1]}'):
                valid_second_words.append(second_words_sorted[j])
        num_of_valid_second_words = len(valid_second_words)
        for k in range(num_of_valid_second_words):
            solutions.append([valid_first_words[i], valid_second_words[k]])
    return solutions

def main():
    # get words
    text_file = open("filtered_words.txt", "r")
    words = text_file.read().split('\n')
    print(len(words))
    letters = get_user_input()
    #letters = ['a', 'f', 'n', 'l', 'b', 's', 'e', 'z', 'o', 'i', 'r', 'y']
    # remove words containing invalid digraphs from word list
    removed_digraphs = digraph_removal(letters)
    # sort the valid first words from most unique to least unique letters
    valid_first_words = find_valid_first_words(words, letters, removed_digraphs)
    # determine which letters still need to be used
    used_letters = set(valid_first_words[0])
    leftover_letters = list(set(letters) - used_letters)
    # if the first word contains all letters, just print that word
    if len(leftover_letters) == 0:
        print(f'{valid_first_words[0]} contains every letter!')
    else:
        # figure out a second word using the remaining letters
        solutions = all_possible_solutions(words, letters, leftover_letters, removed_digraphs, valid_first_words)
        # print solutions
        for entry in solutions:
            print(entry)
    
main()