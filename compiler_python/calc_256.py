BASE = 256

arr = [0, 255]
orig = 258

res = arr[0]
for i, a in enumerate(arr):
    res += a * (BASE * i)
print(f"{arr} = {res}")

a = orig
arr = []
while a >= BASE:
    arr.append(a // BASE)
    a = a % BASE
arr.append(a)
arr.reverse()
print(f"{orig} = {arr}")
