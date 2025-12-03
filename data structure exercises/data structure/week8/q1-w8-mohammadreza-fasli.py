def binary_search_exists(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    # خواندن خط اول: لیست مرتب از اعداد
    line = input().strip()
    if line == "":
        nums = []
    else:
        nums = list(map(int, line.split()))

    # خواندن خط دوم: عدد هدف
    target = int(input().strip())

    # اجرای جستجوی دودویی و چاپ نتیجه
    exists = binary_search_exists(nums, target)
    print(exists)
