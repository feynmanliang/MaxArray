A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

def maxCrossing (A, low, mid, high):
    leftsum = -99999
    totsum = 0
    maxleft = mid
    for i in reversed(range(low, mid+1)):
        totsum = totsum + A[i]
        if totsum > leftsum:
            leftsum = totsum
            maxleft = i

    rightsum = -9999999
    totsum = 0
    maxright = mid+1
    for j in range(mid+1, high):
        totsum = totsum + A[j]
        if totsum > rightsum:
            rightsum = totsum
            maxright = j
    return (maxleft, maxright, leftsum + rightsum)

def findMax(A, low, high):
    if high==low:
        return (low, high, A[low])
    else:
        mid = (low + high) / 2
        (leftlow, lefthigh, leftsum) = findMax(A, low, mid)
        (rightlow, righthigh, rightsum) = findMax(A, mid+1, high)
        (crosslow, crosshigh, crosssum) = maxCrossing(A, low, mid, high)
    if leftsum >= rightsum and leftsum >= crosssum:
        return (leftlow, lefthigh, leftsum)
    elif rightsum >= leftsum and rightsum >= crosssum:
        return (rightlow, righthigh, rightsum)
    else:
        return (crosslow, crosshigh, crosssum)

(low, high, sumofsub) = findMax(A, 0, len(A)-1)

print "Low: %d, High: %d, Sum: %d" % (low+1, high+1, sumofsub)
