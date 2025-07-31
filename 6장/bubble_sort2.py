from typing import MutableSequence

def bubble_sort_verbose2(a: MutableSequence) -> None:
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n-1):
        print(f'패스 {i + 1}')
        exchng = 0         # 이 위치여야 패스당 교환 개수임.
        for j in range(n-1, i, -1):
            # 정렬 과정 출력(비교 및 교환 표시)
            for m in range(0, n-1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j-1] > a[j] else ' -'),
                                     end=' ')
            print(f'{a[n-1]:2}')
            ccnt += 1

            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                scnt += 1
                exchng += 1
        for m in range(0, n-1):   # 패스별 정렬 결과 출력
            print(f'{a[m]:2}', end='   ')
        print(f'{a[n-1]:2}')
        if exchng == 0:
            break

    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
    print("최종 정렬 리스트:", a)

if __name__ == "__main__":
    n = int(input("몇 개의 값을 정렬할까요?: "))
    a = list(map(int, input("공백으로 구분해서 값을 입력하세요: ").split()))
    if len(a) != n:
        print(f"입력한 값이 {n}개가 아닙니다.")
    else:
        bubble_sort_verbose2(a)
