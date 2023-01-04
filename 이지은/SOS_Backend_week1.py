import math

print("넓이를 구하고자 하는 원의 개수를 입력해주세요.")
n = int(input())
arr_R = [0] * n
arr_S = [0.0] * n

flag = 0
for i in range(n):
    print("넓이를 구할 원의 반지름을 입력해주세요. (0이 입력될 경우, 값이 출력되지 않고 프로그램이 종료됩니다.)")
    r = int(input())
    if (r == 0):
        flag = 1
        break
    s = r * r * math.pi
    arr_R[i] = r
    arr_S[i] = s

if (flag == 1):
    print("프로그램이 종료되었습니다.")
else:
    for i in range(n):
        print("반지름이 %d 일 때, 원의 넓이는 %.2f입니다." %(arr_R[i], arr_S[i]))
