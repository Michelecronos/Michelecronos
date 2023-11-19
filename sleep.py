import time

s = "Hello, World!"

for char in s:
    print(char, end='', flush=True)
    time.sleep(0.5)  # pause for half a second