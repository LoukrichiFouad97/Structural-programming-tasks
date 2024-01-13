for i in range(1, 10):
    print('*' * i)

# Pattern (Flipped vertically)
for i in range(9, 0, -1):
    print('*' * i)

# Pattern (Rotated 180 degrees)
for i in range(9, 0, -1):
    print(' ' * (9 - i) + '*' * i)

# Pattern (Rotated horizontally)
for i in range(1, 10):
    print(' ' * (9 - i) + '*' * i)
