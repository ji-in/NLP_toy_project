# Simple Neural Text Classification

## Reference

[여기](https://github.com/kh-kim/simple-ntc)를 참조하였다.

## Preparation

Preprocessing 과정은 Window에서 수행하였지만, model을 train, test 하는 과정은 Linux에서 수행하였다.

tokenization에서 만들었던 review.refined.regex.tok.tsv 파일을 corpus.txt로 이름을 바꾸고 data 폴더 안에 넣었다.

1. `wc -l`명령어를 사용하여 corpus.txt 안에 행이 몇개인지 알아낸다. 

   ```
   $ wc -l ./data/corpus.txt
   873 ./data/corpus.txt
   ```

2. data를 shuffle을 하고, 8:2의 비율로 train dataset과 test dataset을 나눈다.

   ```
   $ cat ./data/corpus.txt | shuf > ./data/corpus.shuf.txt
   $ head -n 175 ./data/corpus.shuf.txt > ./data/corpus.test.txt
   $ tail -n 698 ./data/corpus.shuf.txt > ./data/corpus.train.txt
   ```

## Train

```
$ python train.py --model_fn model.pth --train_fn ./data/corpus.train.txt --gpu_id 0 --rnn --cnn
```



## Test

```
$ head ./data/corpus.test.txt | awk -F'\t' '{ print $2 }' | python classify.py --model model.pth --gpu_id -1 --top_k 1
```

```
positive        사회 적 메시지 + 재미
positive        원작 의 분위기 랑 은 다르 지만 . 충분히 좋 았 어요 눈 오 는 날 . 한번더보고싶은~
positive        존 메이 가 삶 으로 그리 ㄴ 한 폭 의 정물화 .
positive        남주혁 의 깊 고 섬세 하 ㄴ 연기 가 마음 이 찡하 아 지 었 다
positive        또 울 었 다 . ... 명작
negative        뭐 ㄴ 내용 이여 . 이 게 ㅡㅡ 막판 에 ㄴ 급 ㅁ ㅓ ㅈ ㅣ
negative        착 짱 죽 짱 착 짱 죽 짱 착 짱 죽 짱
positive        구성은 꽤 불 친절 하 았 지만 영석 의 뒷 모습 에 마음 이 저리 다 . 남주혁 . 10년 후 가 더 더 더 기대 되 는 배우 .
positive        원작 은 바라보 게 되 고 한국판 은 이입 하 게 되 ㄴ다 .
positive        도굴 이 이 라는 어찌 보 면 식상 하 ㄴ 주제 이 ㄴ데 이제훈 의 익살 스럽 ㄴ 연기 가 넘 재미있 고 반전 의 반전 이 재미있 어요
```

