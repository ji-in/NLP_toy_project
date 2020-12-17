import sys

STR = '▁'

if __name__ == "__main__":
    # python post_tokenize.py ${FN}.text > ${FN}.text.tok
    # python post_tokenize.py < review.refined.regex.tok.tsv > review.refined.regex.tok.subword.tsv
    # 예진 이 누나 ... 미소 가 너무 아름답습니다ㅜㅜ --> txt 파일이라고 가정
    ref_fn = sys.argv[1]

    f = open(ref_fn, 'r', encoding='utf-8')

    for ref in f: # ref : 예진 이 누나 ... 미소 가 너무 아름답습니다ㅜㅜ
        ref_tokens = ref.strip().split(' ') # strip() : 공백 제거
        # ref_tokens = ['예진', '이', '누나', '...', '미소', '가', '너무', '아름답습니다ㅜㅜ']
        input_line = sys.stdin.readline().strip()
        # input_line = [

        if input_line != "":
            tokens = input_line.split(' ') # tokens = 형태소가 들어있는 list

            idx = 0
            buf = []

            # We assume that stdin has more tokens than reference input.
            # stdin 이 reference input 보다 더 많은 tokens 를 가지고 있다고 가정한다.
            for ref_token in ref_tokens:
                tmp_buf = []

                while idx < len(tokens):
                    if tokens[idx].strip() == '':
                        # idx번째 token에 아무것도 없으면 idx만 증가시키고 계속 진행한다.
                        idx += 1
                        continue

                    tmp_buf += [tokens[idx]]
                    idx += 1

                    if ''.join(tmp_buf) == ref_token:
                        break

                if len(tmp_buf) > 0:
                    buf += [STR + tmp_buf[0].strip()] + tmp_buf[1:]
                    # _tmp_buf[0]tmp_buf[1:]

            sys.stdout.write(' '.join(buf) + '\n')
        else:
            sys.stdout.write('\n')

    f.close()
