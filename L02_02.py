import statistics

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x_med = statistics.median(x)
x_min = min(x)
x_max = max(x)
x_top = x_max - x_med
x_bot = x_med - x_min
x_ratio = x_top/x_bot

print(x_med)
print(x_min)
print(x_max)
print(x_top)
print(x_bot)
print(x_ratio)