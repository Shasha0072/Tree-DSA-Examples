

def willPrint(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        summ = arr[left] + arr[right]
        if summ == 0:
            print(arr)
            return
        elif summ > 0:
            right -= 1
        elif summ < 0:
            left += 1
    print("no")


arr = [0, 44, 10, 5, 7, 8, 20,-10, -11]
willPrint(arr)

