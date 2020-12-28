import sys

# review.refined.regex.tsv.label.txt 와 review.refined.regex.tsv.post.bpe 합치기
if __name__ == "__main__":
    label = sys.argv[1]
    data = sys.argv[2]

    label_fp = open(label, 'r', encoding='utf-8')
    data_fp = open(data, 'r', encoding='utf-8')

    label_lines = label_fp.readlines()
    data_lines = data_fp.readlines()

    label_fp.close()
    data_fp.close()

    for i in range(len(label_lines)):
        line = label_lines[i].rstrip('\n') + '\t' + data_lines[i]
        sys.stdout.write(line + "\n")