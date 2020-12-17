import sys

# review.refined.regex.tsv.label.txt 와 review.refined.regex.tsv.post.bpe 합치기
if __name__ == "__main__":
    label = sys.argv[1]
    data = sys.argv[2]

    label_fp = open(label, 'r', encoding='utf-8')
    data_fp = open(data, 'r', encoding='utf-8')
    
    
    
    for line in sys.stdin:
        if line.strip() != "":
            columns = line.strip().split('\t')

        sys.stdout.write(columns[target_index] + "\n")