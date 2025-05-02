# [문제] 두 수의 나눗셈 (https://school.programmers.co.kr/learn/courses/30/lessons/120806)
# [난이도] 하 | [카테고리] 연산 | [제한] 1초 / 128MB

# [설명] (num1 / num2) * 1000 의 정수 부분을 return
# [제약] 0 < num1, num2 ≤ 100

# [입출력 예]
# 입력: 3 2 → 출력: 1500
# 입력: 7 3 → 출력: 2333
# 입력: 1 16 → 출력: 62

# [접근] float 나눗셈 후 1000 곱하고 int()로 정수 변환
# [복잡도] 시간: O(1), 공간: O(1)

def solution(num1, num2):
    return int((num1 / num2) * 1000)
