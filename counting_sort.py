def counting_sort(arr):

    # creating a base list "count" containing 10 0's (0-9  )

    c = [0]*10

    for i in range(len(arr)):

        # incrementing counts of each digit

        c[arr[i]] += 1

    for i in range(1, 10):

        # no we are added the no. of counts at i with the one before it

        c[i] += c[i-1]

    # time to traverse the list in opposite direction
    i = len(arr)-1

    # creating another array which will store the result
    res = [0]*len(arr)

    while i >= 0:

        # basically first we get the element we need to place with arr[i]
        # then we check it count with c[arr[i]-1] , -1 for decrement from position value to index value
        # then we assign the value "arr[i]" to the index value we derived in res

        res[c[arr[i]]-1] = arr[i]

        # decrementing no. of counts
        c[arr[i]] -= 1
        i -= 1

    return res


print(counting_sort([2, 1, 2, 6, 0, 4, 3, 3]))
