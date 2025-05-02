# 숫자 비교하기
# 문제 설명: 두 정수 num1과 num2가 같으면 1, 다르면 -1을 반환한다.
# 제한사항: 0 ≤ num1, num2 ≤ 10,000

def solution(num1, num2):
    return 1 if num1 == num2 else -1

# 예시 실행
if __name__ == "__main__":
    print(solution(2, 3))    # -1
    print(solution(11, 11))  # 1
    print(solution(7, 99))   # -1