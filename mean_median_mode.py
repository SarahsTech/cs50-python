import statistics

data = [23, 29, 20, 32, 23, 21, 33, 25]

# calculate the mean (average)
mean_value = statistics.mean(data)
print(f"Mean: {mean_value}")

# calculate the median (middle value)
median_value = statistics.median(data)
print(f"Median: {median_value}")

# calculate the mode (most frequent value)
mode_value = statistics.mode(data)
print(f"Mode: {mode_value}")