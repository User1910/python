
a = int(input())
b = int(input())
c = input()
if c == str('+'):
    print(a + b)
elif c == str('-'):
    print(a - b)
elif c == str('*'):
    print(a * b)
elif c == str('/'):
    if a != 0 and b != 0:
        print(a / b)
    else:
        print('На ноль делить нельзя!')
else:
    print('Неверная операция')
