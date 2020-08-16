# Finds the most commmonly cited journal in a References / Citation List
# Sarthak Gupta
# 05/12/2020

fileLocation = input('Input References file (.txt) location: ')
file = open(fileLocation)

# dictionary of academic journals
counts = dict()

for line in file:
    #print(line)

    # finds first instance of " in each line
    firstQindex = line.find("\"")

    # finds second instace of "
    secondQindex = line.find("\"", firstQindex+1)

    # spliced String from second " to end of line
    splicedString = line[secondQindex+2:]

    # for loops finds first instane of numerical digit after second "
    firstNumIndex = secondQindex+2
    for character in splicedString:
        if character.isdigit():
            break
        firstNumIndex = firstNumIndex + 1

    # splices string to find journalName in between second " and first numerical digit
    journalName = line[secondQindex+2:firstNumIndex-1]
    #print(journalName)

    # increments each journal to the dictionary
    counts[journalName] = counts.get(journalName, 0) + 1

# prints the dictionary
for key in counts:
    print(counts[key], ':', key)

# finds the greatest count in the dictionary
bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print()
print('The most cited journal is', bigWord, 'with', bigCount, 'instances.')
print()