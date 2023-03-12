def checkio(words: str) -> bool:
    # counter = 0
    #
    # for word in words.split():
    #
    #     # counter = (counter + 1) * word.isalpha()
    #
    #     if word.isalpha():
    #         counter += 1
    #     else:
    #         counter = 0
    #
    #     if counter == 3:
    #         return True
    #
    # return False

    sequence = words.split()
    new_seq = ''.join(['Y' if word.isalpha() else 'N' for word in sequence])

    return "YYY" in new_seq


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")