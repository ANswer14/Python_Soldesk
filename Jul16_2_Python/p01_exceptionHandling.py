# -*- coding:utf-8 -*-

# Java : 강제 => 언제 해야하는지 몰라도 됨
#        하기 싫은데도 해야하는...
#        직접 : try - catch - finally
#        미루기 : throws 

# Python : 하기 싫으면 안해도 됨
#        직접 : try - except - else - finally


# error : 컴파일할때(소스를 기계어로 바꿀때) 컴파일작업을 실행하지 못하는 상황
# warning : 정리가 안된 소스(ex: 쓸모없는 변수 설정, close();를 안한 상황)
# exception : 실행하다가 예외적인 상황이 발생해서 정상적으로 돌아가지 않는 상황

# 인터프리터 방식 : 실행하면 그 때부터 한줄씩 기계어로 바꿔서 실행
# error ? exception ? 경계가 모호함
######################################################
    

try:
    # 정수 2개 입력받아서 앞의 숫자를 뒤에 숫자로 나눴을 때 그 몫을 출력
    x = int(input('정수 입력 : '))
    y = int(input('정수 입력 : '))
    ans = x // y
    print(ans)
    
    l = [1, 23, 456]
    print(l[y])
except Exception as asdf:   # 일괄적으로
    print(asdf)             # 무슨 내용인지 알고 싶을 때
# except ZeroDivisionError:
    # print("y에 0")
# except ValueError:
    # print("공백")
# except IndexError:
    # print("y값이 0보다 작거나 2보다 큼 or 실수")

# try문에서 else를 사용하는 이유는, 단순 성능적인 부분이 아니라
# 에러가 발생할 가능성이 있는 부분과 그렇지 않은 부분을 정확히 구분지어
# 작성자의 의도를 명확하게 하기 위함
else:
    print('문제가 없으면 실행')
finally:
    print('문제가 있든 없든 무조건 실행(return 보다 먼저 실행)')


















































