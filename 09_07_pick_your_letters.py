# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers"

# Construct the sentence using string indexing and concatenation
sentence = word[1] + word[5:6] + " " + word[7] + word[2:4] + " " + word[0] + word[6] + word[2:4] + word[7]

# Print the sentence
print(sentence)

