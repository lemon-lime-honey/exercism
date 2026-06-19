def find(search_list, value):
    low = 0
    mid = 0
    high = len(search_list) - 1
    while(low <= high):
        mid = round(low + high)
        if value == search_list[mid]:
            return mid
        elif search_list[mid] > value:
            high = mid - 1
        elif search_list[mid] < value:
            low = mid + 1
    raise ValueError("value not in array")
