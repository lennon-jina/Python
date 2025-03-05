import random

from week1.day1_while_ex import user_lotto


def get_lotto():
    """
    로또 번호 6개 생성
    1 ~ 45 사이의 숫자
    :return: set
    """
    lotto_num = set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1, 45))
    return lotto_num


def krw_to_usd(krw):
    pass
def usd_to_krw(usd):
    pass
# 원화 to 달러
# 달러 to 원화 함수를 만들어주세요
print("로또 잘 생성되나")
print(get_lotto())
print(f"달러 100은 : {usd_to_krw(100)}원")
print(f"원화 20000은 : {krw_to_usd(20000)}달러")

print(user_lotto(1, 2, 3, 4, 5, 6))#
print(user_lotto(99, 2, 3))
print(user_lotto())

test = (1, 14, 15)
# to list
test2 = list(test)[:2]  # :2 <--- 처음부터 2-1 인덱스까지 슬라이싱
print(test2)
my_set = set(test2)  # 해당 데이터가 포함 되어 있는 set 생성
print(my_set, type(my_set))
# user_lotto
# input : 0 ~ n개 (사용자 희망 번호) 가변?!
# output : ture or false, 메세지, 로또 번호(사용자 희망 번호가 포함된) 리턴 여러개!?
# 사용 입력 번호를 포함 시켜서 로또 번호 생성
# 단 사용자 입력은 최대 5개 까지만 포함 슬라이싱?!
# 각 사용자 입력은 1 ~ 45 사이 수만
# 조건을 만족하지 않으면 false, 만족 하면 true
# 메세지는 false 일때 왜 false 인지

