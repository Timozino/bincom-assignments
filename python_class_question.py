from bs4 import BeautifulSoup
from collections import Counter

# Path to your HTML file
html_file_path = r"C:\Users\Py-Timson\Desktop\Bincom-assignment\python_class_question.html"

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

def extract_colors(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr")[1:]  # Skip header row
    colors = []
    for row in rows:
        day_colors = row.find_all("td")[1].text.strip()  # Second column contains colors
        colors += [color.strip().upper() for color in day_colors.split(",")]
    return colors

def mean_color(colors):
    count = Counter(colors)
    return count.most_common(1)[0][0]

def median_color(colors):
    count = Counter(colors)
    sorted_colors = sorted(count.items(), key=lambda x: x[1], reverse=True)
    mid_index = len(sorted_colors) // 2
    if len(sorted_colors) % 2 == 0:
        return sorted_colors[mid_index - 1][0], sorted_colors[mid_index][0]
    return sorted_colors[mid_index][0]

def most_frequent_color(colors):
    count = Counter(colors)
    return count.most_common(1)[0][0]

def color_variance(colors):
    count = Counter(colors)
    frequencies = list(count.values())
    mean_freq = sum(frequencies) / len(frequencies)
    variance = sum((x - mean_freq) ** 2 for x in frequencies) / len(frequencies)
    return variance

def probability_of_red(colors):
    count = Counter(colors)
    red_count = count.get("RED", 0)
    total_count = len(colors)
    return red_count / total_count if total_count > 0 else 0

def process_binary_sequence(binary_input):
    output = []
    for i in range(len(binary_input)):
        chunk = binary_input[max(0, i - 2):i + 1]  # Get the 3-character chunk
        if chunk.count('1') == 3:
            output.append('1')
        else:
            output.append('0')
    return ''.join(output)

# Main Execution
colors = extract_colors(html_content)
print(f"Mean color: {mean_color(colors)}")
print(f"Median color: {median_color(colors)}")
print(f"Most frequent color: {most_frequent_color(colors)}")
print(f"Variance of colors: {color_variance(colors)}")
print(f"Probability of red: {probability_of_red(colors):.2f}")

binary_input = "0101101011101011011101101000111"
output = process_binary_sequence(binary_input)
print(f"Input: {binary_input}")
print(f"Output: {output}")
