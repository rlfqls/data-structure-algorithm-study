#세 정수 입력받아 중앙값 구하기1

def med3(a,b,c):
    if a >= b:
        if b >=c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b
    
print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a,b,c)}입니다. ')