import sys

if __name__ == "__main__":
    target_index = int(sys.argv[1]) # 0

    for line in sys.stdin:
        if line.strip() != "":
            columns = line.strip().split('\t')

        sys.stdout.write(columns[target_index] + "\n")