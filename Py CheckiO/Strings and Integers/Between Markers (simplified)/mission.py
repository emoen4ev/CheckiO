def between_markers(text: str, start: str, end: str) -> str:
    start_index = text.index(start) + 1
    end_index = text.index(end)

    return text[start_index:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")