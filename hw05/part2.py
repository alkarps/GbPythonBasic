with open("part2.txt", "r") as file:
    lines = file.readlines()
    print(f"Count lines: {len(lines)}.")
    for ind, line in enumerate(lines):
        print(f"{ind + 1}'s line contain {len(line.split())} words.")
