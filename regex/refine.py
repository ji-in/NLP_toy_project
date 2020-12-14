import sys
import re

def read_regex(fn):
    regexs = []

    f = open(fn, 'r', encoding='utf-8') # txt 파일 열기

    for line in f: # txt 파일 한줄씩 읽기
        if not line.startswith("#"): # "#"으로 시작하는가?
            tokens = line.split('\t') # tab을 기준으로 자른다. tokens[0] : 전각문자, tokens[1] : 반각문자

            if len(tokens) == 1: # 리스트인 tokens 의 길이가 1이면
                tokens += [' '] # tokens의 끝에 공백을 추가한다.

            tokens[0] = tokens[0][:-1] if tokens[0].endswith('\n') else tokens[0]
            tokens[1] = tokens[1][:-1] if tokens[1].endswith('\n') else tokens[1]

            regexs += [(tokens[0], tokens[1])] # regex[0] :전각문자, regex[1] : 반각문자

    f.close()

    return regexs

if __name__ == "__main__":
    fn = sys.argv[1] # refine.regex.txt
    target_index = int(sys.argv[2]) # 1

    regexs = read_regex(fn) # txt 파일 읽기

    for line in sys.stdin: # sys.stdin : 입력받을 때 사용
        if line.strip() != "":
            columns = line.strip().split('\t')
            print(columns)
            for r in regexs:
                columns[target_index] = re.sub(r'%s' % r[0], r[1], columns[target_index].strip())
                # strip() : 문자열 양쪽 끝에 공백 제거
                # re.sub('패턴', '바꿀 문자열', '문자열', 바꿀 횟수)
                # 바꿀 횟수를 넣으면 지정된 횟수만큼 바꾸며, 바꿀 횟수를 생략하면 찾은 문자열을 모두 바꾼다.
                # re.sub(전각문자, 반각문자, 문자열) -> 문자열에서 전각문자를 반각문자로 바꾸기

            sys.stdout.write('\t'.join(columns) + "\n")
        else:
            sys.stdout.write('\n')