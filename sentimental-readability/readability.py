# define functions
def count_words(text):
    word_count = 1
    for _ in text:
        if _ == " ":
            word_count += 1
    return word_count

def count_sentences(text):
    sentence_count = 0
    for _ in text:
        if _ == "." or _ == "?" or _ == "!":
            sentence_count += 1
    return sentence_count

def count_letters(text):
    letter_count = 0
    for _ in text:
        if _.isalpha():
            letter_count += 1
    return letter_count


# prompt for text input
text = input("Text: ")

# increment word count by counting spaces between words
word_count = count_words(text)
# increment sentence count by counting ending punctuation
sentence_count = count_sentences(text)
# Count number of letters
letter_count = count_letters(text)
# Use algorithm to assign reading level
# Calculate index (<1 = "Before Grade 1"; >=16 = "Grade 16+")

# average letters per 100 words 
x = (letter_count / word_count) * 100
# printf("Average letters per 100 words: %d\n", x);

# average sentences per 100 words
y = (sentence_count / word_count) * 100
# printf("Average sentences per 100 words: %f\n", y);

round_index = round((x * 0.0588) - (y * 0.296) - 15.8)

# Print ouput as "Grade x"
if (round_index < 1):
    print("Before Grade 1")
elif (round_index > 15):
    print("Grade 16+")
else:
    print(f"Grade {round_index}")


