a = int(input())
b = int(input())
c = int(input())

if a == b and b == c:
    print("3")
elif (a == b and a != c) or (b == c and a != c) or (a == c and a != b):
    print("2")
else:
    print("0")