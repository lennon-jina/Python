import random

# 업다운 게임
# 3번의 기회
# 사용자 입력이 맞으면 '정답', 작으면 '업', 크면 '다운' 출력
# 틀릴 때마다 몇번의 기회가 있는지 출력
# computer의 랜덤 값은 1 ~ 10 사이의 정수

random_nm = (random.randint(1, 10))
print(random_nm)

number = int(input("숫자를 입력하세요:"))

cnt = 0
while cnt == 3:
    if(number > random_nm):
        print("다운 !")
        cnt += 1
    elif(number < random_nm):
        print("업 !")
        cnt += 1
    elif(number == random_nm):
        print("정답입니다 !")
        print("시도 횟수:" + cnt)
    else:
        print("다음 기회에... 정답은:" + random_nm)
