text_file = open("words_alpha.txt", "r")
words = text_file.read().split('\n')
filtered_words = open("filtered_words.txt", 'w')
print(f'Original Length: {len(words)}')

for word in words:
    if 3 <= len(word) <= 15:
        filtered_words.write(f'{word}\n')

short_words_open = open("filtered_words.txt", 'r')
short_words = short_words_open.read().split('\n')

print(f'New Length: {len(short_words)}')