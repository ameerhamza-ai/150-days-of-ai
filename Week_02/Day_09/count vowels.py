sentence = input("Enter sentence: ")
count = 0
for char in sentence.lower():
    if char in "aeiou":
        count += 1
        print(f"Vowels: {count}")