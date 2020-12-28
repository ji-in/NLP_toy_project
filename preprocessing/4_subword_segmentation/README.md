# Subword segmentation

------

단어보다 더 작은 의미 단위로 분절한다.

Subword segmentation 을 위해 [여기](https://github.com/kh-kim/subword-nmt.git)

에서 코드를 클론받아 사용했다.

### Implementation

1. review.refined.regex.tsv 파일을 형태소 분석을 하고, data 부분만 잘라서 저장한다.

```python
$ python tokenize.py 1 < review.refined.regex.tsv > review.refined.regex.tsv.txt
```

2. review.refined.regex.tsv.txt 파일에서 토큰화 되어있는 부분 앞뒤로 '_'를 붙인다.

```python
$ python post_tokenize.py review.refined.regex.tsv.txt < review.refined.regex.tsv.txt > review.regined.regex.tsv.post
```

3. 2에서 후처리 한 파일을 사용하여 bpe 모델을 학습한다.

```python
$ python ./subword-nmt/learn_bpe.py --input ./review.refined.regex.tsv.post --output ./model --symbols 30000
```

4. 3에서 만든 모델을 review.refined.regex.tsv.post 파일에 적용한다.

```python
$ python ./subword-nmt/apply_bpe.py --codes ./model < review.refined.regex.tsv.post > review.refined.regex.tsv.post.bpe
```

5. review.refined.regex.tsv 파일에서 label만 따로 저장한다.

```python
$ python cut_label.py 0 < review.refined.regex.tsv > review.refined.regex.tsv.label
```

6. label과 review.refined.regex.tsv.post.bpe 파일을 하나로 합친다.

```python
$ python merge.py review.refined.regex.tsv.label.txt review.refined.regex.tsv.post.bpe > final.txt
```