# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diff = 0
    for index in range(len(arr)):
        diff += arr[index][index] - arr[index][-1-index]
        
    return abs(diff)