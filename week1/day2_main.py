import my_util
from my_util import get_lotto
from my_util import get_lotto as l  # 별칭 사용

print(my_util.get_lotto())
print(get_lotto())
print(l())


# 도움말 같은 거
help(my_util)

# 모듈내 실행
if __name__ == '__main__':
    print("로또 잘 생성되나")
    print(get_lotto())
