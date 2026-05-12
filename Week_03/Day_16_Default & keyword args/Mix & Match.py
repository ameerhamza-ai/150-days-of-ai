def process_data_mix(category, *scores, **metadata):
    return f"Category: {category}\nScores: {scores}\nMetadata: {metadata}"

result = process_data_mix("AI Midterms", 85, 92, 78, Instructor="Dr. Zafar", Lab="Room 4")
print(result)