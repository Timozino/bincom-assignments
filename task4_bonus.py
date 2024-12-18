from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']


# Variance of the colors
def color_variance(colors):
    count = Counter(colors)
    frequencies = list(count.values())
    mean_freq = sum(frequencies) / len(frequencies)
    variance = sum((x - mean_freq) ** 2 for x in frequencies) / len(frequencies)
    return variance


print(f"Variance of colors: {color_variance(colors)}")
