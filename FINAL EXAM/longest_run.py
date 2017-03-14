def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here

    longestIncrRun = []

    longestDecrRun = []

    for i in range(len(L)):

        IncrRun=[L[i]]

        for j in range(i+1, len(L)):
            if L[j] >= L[j-1]:
                IncrRun.append(L[j])
            else:
                break

        if len(IncrRun) > len(longestIncrRun):
            longestIncrRun = IncrRun


    for i in range(len(L)):

        DecrRun=[L[i]]

        for j in range(i+1, len(L)):
            if L[j] <= L[j-1]:
                DecrRun.append(L[j])
            else:
                break

        if len(DecrRun) > len(longestDecrRun):
            longestDecrRun = DecrRun


    if len(longestIncrRun) == len(longestDecrRun):
        if L.index(longestIncrRun(0)) < L.index(longestDecrRun(0)):
            longest_run = longestIncrRun
        else:
            longest_run = longestDecrRun

    elif max(len(longestIncrRun), len(longestDecrRun)) == len(longestIncrRun):
        longest_run = longestIncrRun

    else:
        longest_run = longestDecrRun

    zbir = 0

    for x in longest_run:
        zbir += x

    return zbir