# [문제] 두 수의 곱 구하기 (https://school.programmers.co.kr/learn/courses/30/lessons/120804)
# [난이도] 하 | [카테고리] 연산 | [제한] 1초 / 128MB

# [설명] 정수 num1, num2를 곱한 값을 return
# [제약] 0 ≤ num1, num2 ≤ 100

# [입출력 예]
# 입력: 3 4 → 출력: 12
# 입력: 27 19 → 출력: 513

# [접근] * 연산자 사용, O(1)
# [복잡도] 시간: O(1), 공간: O(1)

def solution(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    print(solution(num1, num2))
