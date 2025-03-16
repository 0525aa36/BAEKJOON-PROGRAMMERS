test = int(input())
for i in range(test):
    nums = list(map(int, input().split())) # 숫자 받음
    avg = sum(nums[1:])/nums[0] #nums[1:] : 점수 num[0] : 학생수
    count = 0 # 평균보다 높은 사람 초기화
    for score in nums[1:]:
        if score > avg:
            count += 1 # 평균보다 높은 사람 수
    A = count/nums[0] * 100 # 평균보다 높은 사람/총원
    print(f'{A:.3f}%')
