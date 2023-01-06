import random
answer = random.sample(range(1, 10), 3)
print("애주가인 다봉이는 환상적인 끝맛을 자랑한다는 돔페리뇽을 사마시기 위해 돈을 모아왔다.")
print("보안을 중요시했던 다봉이은 금고에 돈을 넣어두었다.")
print("이 금고는 비밀번호를 3번 틀리면 금고 안의 내용물을 모두 태워버리는 파괴적인 성능을 자랑한다.")
print("그리고 마침내 다봉이에게 그 날이 찾아왔다 하지만 아뿔싸... 다봉이는 비밀번호를 잊어버리고 말았다...")
print("당신은 다봉이를 도와 금고의 비밀번호를 해제해야 한다.")
print("다봉이는 그토록 그다렸던 돔페리뇽을 마실 것인가... 쉴세없이 흐르는 눈물을 마시게 될 것인가...")
print("(비밀번호의 숫자와 순서가 모두 맞으면 정밀도가 상승하고 비밀번호의 숫자만 맞고 순서가 다르다면 정확도가 증가합니다.)")
count = 0
while (True):
    print("****** 비밀번호 *******")
    precision = 0
    accuracy = 0
    print("첫 번째 비밀번호를 입력해주세요: ", end="")
    first = int(input())
    print("두 번째 비밀번호를 입력해주세요: ", end="")
    second = int(input())
    print("세 번째 비밀번호를 입력해주세요: ", end="")
    third = int(input())
    if (answer[0] == first):
        precision += 1
    elif (answer[0] == second or answer[0] == third):
        accuracy += 1
    if (answer[1] == second):
        precision += 1
    elif (answer[1] == first or answer[1] == third):
        accuracy += 1
    if (answer[2] == third):
        precision += 1
    elif (answer[2] == first or answer[2] == second):
        accuracy += 1
    if (precision == 3):
        print("다봉이의 입가에는 미소가 번집니다.")
        print("다봉이와 당신은 돔페리뇽은 마시며 한껏 흥에 취합니다.")
        break
    count += 1
    print("정밀도: ", precision)
    print("정확도: ", accuracy)
    print("남은 기회: ", 3 - count)
    if (count == 1):
        print("다봉이는 애써 웃음을 보이며 당신에게 자신이 괜찮다는 것을 보입니다.")
        print("하지만 미동도 없는 눈가에서 다봉이가 흔들리고 있다는 걸 느낍니다.")
    if (count == 2):
        print("다봉이는 냉장고에 있던 빨간 뚜겅의 이슬을 꺼내 마시기 시작합니다.")
        print("다봉이는 요정이라도 된 것일까요?")
    if (count == 3):
        print("타닥타닥 다봉이의 꿈과 희망이 타오르기 시작합니다.")
        print("다봉이는 이성을 잃었습니다.")
        print("냐옹 냐옹~")
        print("다봉이는 고양이가 되었습니다...")
        break
