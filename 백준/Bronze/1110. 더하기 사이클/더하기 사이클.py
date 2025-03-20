import sys

N = int(input().strip())

if N < 10: # N이 10보다 작으면 *10 해서 두 자리 수 만들어
    N *= 10

def 사이클(num, 원래수, count):
    a = num // 10 # 첫 번째 숫자 뽑아
    b = num % 10 # 두번쨰 숫자 뽑아
    s = a + b # 첫 번째 숫자, 두 번째 숫자 더해

    new = (b * 10) + (s % 10) # 이전에 첫번 째 숫자 10보다 작으면 10곱하고 앞자리 현재 숫자의 뒷자리 더해
    
    if new == 원래수:  #원래 수가 맞으면 카운트 1올리고  출력
        return count + 1
    else:
        return 사이클(new, 원래수, count + 1) # 아니면 다시 함수실행 ++++카운트

print(사이클(N, N, 0)) # return 값 count 출력 (이건 맞은 것 같습니다..)
