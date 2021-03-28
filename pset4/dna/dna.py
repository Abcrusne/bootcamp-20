import csv
from sys import argv, exit

def main():

    if len(argv) != 3:
        print("Missing command-line argument")
        exit(1)

    data = csv.DictReader(open(argv[1]))
    sequence = open(argv[2]).read()

    # print(data)
    # print(sequence)

# with open('small.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    # for row in csv_reader:
    #     print(line)

    # kaip dictionary, prie jo pridesim
    counts = {}
    for subseq in data.fieldnames[1:]:
        # print(subseq)
        counts[subseq] = longest_match(sequence,subseq)

    # print(counts)

    for row in data:
        if all(counts[subseq] == int(row[subseq]) for subseq in counts):
            print(row["name"])
            return

    print("No match")


    # isivesti nauja best = 0 ir count = 0 for'e, nes mes norime kad rast musu subseq is eiles einancias, ju didziausia skaiciu, o ne kiek ju yra apskritai dnr sekoje


def longest_match(sequence,subseq):
    best = 0
    length = len(subseq)

    for i in range(len(sequence)):
        count = 0
        while True:
            start = i + count * length
            end = start + length

            if sequence[start:end] == subseq:
                count += 1
            else:
                break
        best = max(best, count)

    return best

main()