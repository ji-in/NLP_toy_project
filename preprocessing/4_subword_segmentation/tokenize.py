import sys
from konlpy.tag import Komoran

if __name__ == "__main__":
    kom = Komoran()
    target_index = int(sys.argv[1]) # 1

    for line in sys.stdin:
        if line.strip() != "":
            columns = line.strip().split('\t')
            columns[target_index] = ' '.join(kom.morphs(columns[target_index]))

        sys.stdout.write(columns[target_index] + "\n")