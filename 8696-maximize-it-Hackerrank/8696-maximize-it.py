def maximize_it(lists, m):
    values = {0}

    for arr in lists:
        new_values = set()

        for total in values:
            for x in arr:
                new_values.add((total + x * x) % m)

        values = new_values

    return max(values)
k, m = map(int, input().split())

lists = []

for _ in range(k):
    data = list(map(int, input().split()))
    lists.append(data[1:])

print(maximize_it(lists, m))    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna