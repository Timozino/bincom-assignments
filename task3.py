from collections import Counter

import numpy as np

colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']

### Which color is the median?
def median_color(colors):
    count = Counter(colors)
    frequency_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)
    mid_index = len(frequency_sorted) // 2
    if len(frequency_sorted) % 2 == 0:
        # Even case, taking the average of the two middle
        return (frequency_sorted[mid_index - 1][0], frequency_sorted[mid_index][0])
    else:
        return frequency_sorted[mid_index][0]


print(f"Median color: {median_color(colors)}")
