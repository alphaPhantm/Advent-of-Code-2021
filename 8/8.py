with open("8data.in") as d:
    raw_data = d.read().strip().split("\n")

input_data = [[sorted(line[:line.index("|") - 1].split(" ")), line[line.index("|") + 2:].split(" ")] for line in raw_data]

digits_key = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]
digits = tuple(sorted(digits_key))

for line in input_data:
    pass

print("")
