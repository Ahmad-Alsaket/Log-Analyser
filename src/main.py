import pathlib


def read_file(path):
    # Reads the file and returns a list of lines
    return path.read_text().splitlines()


def count_levels(content):
    # Counts how many times each log level appears
    counts = {}

    for line in content:
        if line:
            level = line.split()[0]

            if level in counts:
                counts[level] += 1
            else:
                counts[level] = 1

    return counts


def group_lines_by_level(content):
    # Groups full log lines under their log level
    levels = {}

    for line in content:
        if line:
            level = line.split()[0]

            if level in levels:
                levels[level].append(line)
            else:
                levels[level] = [line]

    return levels


def print_summary(counts):
    # Prints the count for each log level
    for level, count in counts.items():
        print(f"{level}: {count}")


def print_grouped_lines(levels):
    # Prints all lines grouped by their log level
    for level, lines in levels.items():
        print(f"\n{level}:")
        for line in lines:
            print(f"- {line}")


def filter_by_level(level, content):
    # Prints only the log lines that match the chosen level
    levels = group_lines_by_level(content)

    if level in levels:
        for line in levels[level]:
            print(line)
    else:
        print(f"Sorry, no {level} logs found.")


def menu():
    # Shows menu and returns user's choice
    print("\n========= Log Analyzer =========")
    print("1. Show summary")
    print("2. Show lines grouped by level")
    print("3. Filter by level")
    print("4. Exit")

    return input("Choose: ").strip()


def main():
    user_path = input("Add file path: ").strip()
    path = pathlib.Path(user_path)

    content = read_file(path)

    while True:
        choice = menu()

        if choice == "1":
            counts = count_levels(content)
            print_summary(counts)

        elif choice == "2":
            levels = group_lines_by_level(content)
            print_grouped_lines(levels)

        elif choice == "3":
            level = input("What level do you want to search for? ").strip().upper()
            filter_by_level(level, content)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()