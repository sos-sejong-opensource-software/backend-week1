import random

random_number=random.randint(1,100)

game_count=1

while True:
    try:
        my_num=int(input("1~100 사이의 숫자를 입력하시요:"))

        if my_num>random_number:
            print("다운")
        elif my_num<random_number:
            print("업")
        elif my_num==random_number:
            print(f"축하합니다. 랜덤수는 {random_number}이며 {game_count}회 만에 맞췄습니다")
            break 
    
        game_count+=1
    except:
        print("Error 발생, 숫자를 입력하시오")