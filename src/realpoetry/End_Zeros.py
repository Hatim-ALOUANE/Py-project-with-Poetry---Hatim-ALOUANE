def end_zeros(a: int) -> int:
    # your code here
    A =str(a)
    i=0
    if A[len(A)-1]!="0":
        return(0)
    else:
        while (i<len(A)) and A[len(A)-1-i]=="0":
            i=i+1
        return(i)

print('Example:')
print(end_zeros(10))

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")