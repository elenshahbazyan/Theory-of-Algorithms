arr = [2, 2, 1, 2, 4, 4, 4]
hachaxakanutyun = {}

for num in arr:
    if num in hachaxakanutyun:
        hachaxakanutyun[num] += 1
    else:
        hachaxakanutyun[num] = 1

for key, value in hachaxakanutyun.items():
    if value == 1:
        print(key)
