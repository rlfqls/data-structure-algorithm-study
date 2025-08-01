# 세이커 정렬 알고리즘 구현하기

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:  # 셰이커 정렬
    n = len(a)
    ccnt = 0   # 비교 횟수
    scnt = 0   # 교환 횟수
    
    left = 0
    n = len(a)
    right = len(a) - 1
    last = right
    i = 0
    while left < right:
        print(f'패스(스캔 시작 인덱스 {i + 1})')
        i += 1
        for j in range(right, left, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'),
                                     end=' ')
            print(f'{a[n-1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='   ')
        print(f'{a[n - 1]:2}')

        if(left == right):
            break
        print(f'패스(스캔 시작 인덱스 {i + 1})')
        i += 1

        for j in range(left, right):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j else
                                     ' +' if a[j] > a[j + 1] else ' -'),
                    end=' ')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j] > a[j + 1]:
                scnt += 1
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='   ')
        print(f'{a[n - 1]:2}')
    print(f"비교를 {ccnt}번 했습니다.")
    print(f"교환을 {scnt}번 했습니다.")

if __name__ == "__main__":
    n = int(input("몇 개의 값을 정렬할까요?: "))
    a = list(map(int, input("공백으로 구분해서 값을 입력하세요: ").split()))
    if len(a) != n:
        print(f"입력한 값이 {n}개가 아닙니다.")
    else:
        shaker_sort(a)
        print("정렬 결과:", a)


