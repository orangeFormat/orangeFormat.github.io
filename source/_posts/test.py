def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midPoint = len(alist) // 2  # 整除
        if alist[midPoint] == item:
            return True
        else:
            if item < alist[midPoint]:
                return binarySearch(alist[:midPoint], item)
            else:
                return binarySearch(alist[midPoint+1:], item)