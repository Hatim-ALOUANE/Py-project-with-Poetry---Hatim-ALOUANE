def backward_string(val: str) -> str:
    # your code here
    word = ""
    for i in range(len(val)):
        word = word + val[len(val)-1-i]
    return word

print('Example:')
print(backward_string('val'))

assert backward_string('val') == 'lav'
assert backward_string('') == ''
assert backward_string('ohho') == 'ohho'
assert backward_string('123456789') == '987654321'

print("The mission is done! Click 'Check Solution' to earn rewards!")