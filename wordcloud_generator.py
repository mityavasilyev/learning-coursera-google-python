"""
Coursera-python script
Type: wordcloud
Author: doowybbob
"""
import operator     # importing needed stuff
import wordcloud
import getpass  # library for username retrieval

user_name = getpass.getuser()   # retrieving user name
try:
    with open(f"C:\\Users\\{user_name}\\Desktop\\book.txt") as book_file:  # Reading text file
        word_dictionary = {}    # Placeholder for future dictionary
        banned_fragments = [",", ".", "!", "?", "(", ")", "_", "\n", ":", " ", '"']   # An array of banned chars for later check
        banned_words = ["the", "", "and", "of", "to", "in", "a", "or", "with", "is", "for", "not", "be", "by", "at",
                        "gutenberg-tm"]     # An array of banned words for later check
        word_array = []     # Placeholder for future words array
        book = book_file.read().split(" ")      # Creating an array of words from file with " " (space) splitter
except FileNotFoundError:
    print("Error: There's no book.txt at your desktop!")


for word in book:
    for fragment in banned_fragments:      # Checking if banned chars in word
        if fragment in word:        # Checking word for banned fragments
            word = word.replace(fragment, '')   # Replacing word fragment with pure emptiness
    word_array.append(word.lower())     # Adding word to an array

for word in word_array:        # Running through words in our array
    if word in word_dictionary:
        word_dictionary[word] = word_dictionary[word] + 1   # Increasing value if word repeats
    else:
        word_dictionary[word] = 1   # Creating new entry if word is new
for banned_word in banned_words:       # Wiping out banned words
    while banned_word in word_dictionary:
        word_dictionary.pop(banned_word)

# Turning dictionary into sorted list for TOP-10 preview
preview_word_dictionary_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

# Making and displaying TOP-10 preview
header = "Top 10 Words"
print(f"! {header:=^33} !")
for item in preview_word_dictionary_list[:10]:
    print(f"word: {item[0]:<15} | frequency: {item[1]} ")
# print(preview_word_dictionary_list)

# Proceeding with wordcloud generation
cloud = wordcloud.WordCloud(width=1000, height=800, max_font_size=150, background_color="white")
cloud.generate_from_frequencies(word_dictionary)
cloud.to_file(f"C:\\Users\\{user_name}\\Desktop\\myfile.jpg")
print(f"Saved new wordcloud to C:\\Users\\{user_name}\\Desktop\\myfile.jpg")
