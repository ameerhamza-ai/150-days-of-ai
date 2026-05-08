# step 1: Remove extra spaces
sentence = "  hello world from python  ".strip()

# step 2: Capitalize the first letter of every word of sentence
title_sentence = sentence.title()

# step 3: replace (python) with (AI)
rep_words = title_sentence.replace("python","AI")

# step 4: store replace words in new varialbe
final_sentence = rep_words
print(final_sentence)