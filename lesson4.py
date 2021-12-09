
print('Hello,world!')

word = input("Напишите слово: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

A = int(input())
B = int(input())
if A < B:
  for i in range(A, B + 1):
    print(i)
else:
  for i in reversed(range(B, A + 1)):
    print(i)

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

