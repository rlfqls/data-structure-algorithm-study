# 버블 정렬 알고리즘 구현하기(알고리즘 개선2)

from typing import MutableSequence

def bubble_sort_verbose3(a: MutableSequence) -> None:
    n = len(a)
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    k = 0
    i = 0
    while k < n - 1:
        print(f"패스(스캔 시작 인덱스): {k+1}")
        i += 1
        last = n - 1
        for j in range(n - 1, k, -1):
            # 상태 출력
            for m in range(0, n-1):
                print(
                    f"{a[m]:2}" + ("  " if m != j - 1 else 
                                   " +" if a[j-1] > a[j] else " -"),
                    end=" "
                )
            print(f"{a[n-1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last   # 갱신

        # 패스 후 리스트 상태 출력
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end='   ')
        print(f"{a[n - 1]:2}")

    print(f"비교를 {ccnt}번 했습니다.")
    print(f"교환을 {scnt}번 했습니다.")
    print("최종 정렬 리스트:", a)

if __name__ == "__main__":
    n = int(input("몇 개의 값을 정렬할까요?: "))
    a = list(map(int, input("공백으로 구분해서 값을 입력하세요: ").split()))
    if len(a) != n:
        print(f"입력한 값이 {n}개가 아닙니다.")
    else:
        bubble_sort_verbose3(a)


