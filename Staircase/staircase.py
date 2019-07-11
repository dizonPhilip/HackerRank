# https://www.hackerrank.com/challenges/staircase

def staircase(n):
    for row in range(1,n+1):
        space_chars = " " * (n-row)
        hash_chars = "#" * row
        print(f"{space_chars}{hash_chars}")