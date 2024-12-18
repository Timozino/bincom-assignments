
from collections import Counter

### Which color is mostly worn throughout the week?

def most_frequent_color(colors):
    count = Counter(colors)
    most_common_color = count.most_common(1)[0][0]
    return most_common_color

#Test usage:
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(f"Most frequent color: {most_frequent_color(colors)}")
