sentence = "AI is the future. AI will change everything. I love AI."

# 1. Count
count_AI = sentence.count("AI")
print(f"AI count: {count_AI}")

# 2. First index
first_index = sentence.find("AI")
print(f"First index: {first_index}")

# 3. Last index
last_index = sentence.rfind("AI")
print(f"Last index: {last_index}")

# 4. Exists check
has_future = "future" in sentence
print(f"Has future: {has_future}")