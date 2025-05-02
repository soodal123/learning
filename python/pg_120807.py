# 숫자 비교하기
# 문제 설명: 두 정수 num1과 num2가 같으면 1, 다르면 -1을 반환한다.
# 제한사항: 0 ≤ num1, num2 ≤ 10,000

# 내가 쓴 답
def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1

# 더 나은 답
def solution(num1, num2):
    return 1 if num1 == num2 else -1