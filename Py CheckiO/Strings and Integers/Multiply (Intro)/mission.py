from operator import mul


def mult_two(a: int, b: int) -> int:
    # your code here
    # return a * b
    return mul(a, b)


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")