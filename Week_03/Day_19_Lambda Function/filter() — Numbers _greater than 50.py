scores = [10, 55, 30, 80, 45, 90, 20]
high_scores = list(filter(lambda x: x > 50, scores))
print(f"Numbers > 50: {high_scores}")