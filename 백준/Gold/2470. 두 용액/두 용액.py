import sys

n = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))
t.sort()

left = 0
right = n - 1

answer = abs(t[left] + t[right])
final = [t[left], t[right]]

while left < right:
    left_val = t[left]
    right_val = t[right]

    sum = left_val + right_val

    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]

        if answer == 0:
            break

    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])
