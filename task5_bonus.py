from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']


###Probability of selecting red
def probability_of_red(colors):
    count = Counter(colors)
    red_count = count.get('red', 0)
    total_count = len(colors)
    return red_count / total_count if total_count > 0 else 0

print(f"Probability of red: {probability_of_red(colors)}")
