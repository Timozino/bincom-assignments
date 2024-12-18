from collections import Counter


#### Which color of shirt is the mean color?

def mean_color(colors):
    count = Counter(colors)
    most_common_color = count.most_common(1)[0][0]
    return most_common_color

#test usage
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
print(f"Mean color: {mean_color(colors)}")
