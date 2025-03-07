from inspect import classify_class_attrs

from pkg_resources import file_ns_handler

print("시작")
try:
    print("^^"%4)
except Exception as e:
    print(str(e))
print("종료")


def calc(values):
    sum = 0
    try:
        sum = values[0]+values[1]+values[2]
    except IndexError as a:
        print("인덱스 에러!!")
    except Exception as a:
        print("어떤 오류도!")
    else:
        print("정상처리 일때만")
    finally:
        print("무조건 처리되는")
        calc([1,2,3])  # else, finally
        calc([1, 2])   # index, finally
        calc(None)     # exception, finally