import sys

def calculate_sum(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i+1])
    return total

def generate_permutations(arr, start, end):
    global max_value

    if start == end:
        total = calculate_sum(arr)
        if total > max_value:
            max_value = total

    else:
        for i in range(start, end+1):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutations(arr, start+1, end)
            arr[start], arr[i] = arr[i], arr[start]

def main():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))

    global max_value
    max_value = 0
    generate_permutations(arr, 0, n-1)
    print(max_value)

if __name__ == '__main__':
    main()