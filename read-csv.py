

csv = open("chicago.csv", "r")

data = csv.read()

rows = data.split("\n")

full_data = []
count = 0

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

    count += 1

print()
# print(full_data)
