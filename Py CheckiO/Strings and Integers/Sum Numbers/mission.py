def sum_numbers(text: str) -> int:
    # result = 0
    #
    # sequences = text.split()
    #
    # for el in sequences:
    #     if el.isdecimal():
    #         result += int(el)
    #
    # return result

    # return sum(map(int, filter(str.isdecimal, text.split())))

    return sum(int(word) for word in text.split() if word.isdecimal())


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
        sum_numbers(
            "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
        )
        == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")