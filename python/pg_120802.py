# [문제] 두 수의 합 구하기 (https://school.programmers.co.kr/learn/courses/30/lessons/120802)
# [난이도] 하 | [카테고리] 연산 | [제한] 1초 / 128MB

# [설명] 주어진 두 정수 num1, num2의 합을 구해 return
# [제약] -50,000 ≤ num1, num2 ≤ 50,000

# [입출력 예]
# 입력: 2 3 → 출력: 5
# 입력: 100 2 → 출력: 102

# [접근] + 연산자 사용, O(1) 연산
# [복잡도] 시간: O(1), 공간: O(1)

def solution(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    print(solution(num1, num2))
