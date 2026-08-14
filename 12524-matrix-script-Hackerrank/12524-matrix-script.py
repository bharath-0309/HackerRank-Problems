import re

rows, cols = map(int, input().split())

matrix = []

for _ in range(rows):
    matrix.append(input())

# Read column by column
decoded = ""

for col in range(cols):
    for row in range(rows):
        decoded += matrix[row][col]

# Replace non-alphanumeric characters between alphanumeric characters
decoded = re.sub(r'(?<=\w)[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded)

print(decoded)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna