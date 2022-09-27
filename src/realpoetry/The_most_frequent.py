def most_frequent(data: list[str]) -> str:
    # your code here
    k = [0 for k in range(len(data))]
    for i in range(len(data)):
        elt = data[i]
        for j in range(len(data)):
            if data[j] == elt:
                k[i] = k[i] + 1
    d = k.index(max(k))
    return(data[d])
            


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")