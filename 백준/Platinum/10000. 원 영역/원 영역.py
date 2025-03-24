import sys
import heapq

n = int(sys.stdin.readline())
circles = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    end = x + r
    dist = 2 * r
    circles.append((end,dist))

circles.sort()

h = []
cnt = 1

for i in range(n):
    end, dist = circles[i]
    start = end - dist
    can_fill = False
    last_point = end

    while h:
        e, d = heapq.heappop(h)
        e = -e
        if e <= start:
            heapq.heappush(h, (-e, d))
            break
        if e != last_point and e - d >= start:
            continue
        if e - d >=start:
            last_point = e - d
        if last_point == start:
            can_fill = True

    cnt += 1
    if can_fill:
        cnt += 1
    heapq.heappush(h, (-end, dist))

print(cnt)




