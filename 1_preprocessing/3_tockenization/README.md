# 형태소 분석(Tokenization)

------

mecab를 사용하여 형태소 분석을 하려고 했으나, 이것은 mac os에만 잘 작동한다. 나는 window를 쓰고 있어서 mecab를 사용하지 않았다.

------

cmd창에서 `pip install knolpy`를 통해 knolpy 패키지를 다운받았다.

knolpy 패키지에는 Hannanum, Kkma, Komoran, Mecab, Okt(Twitter) 등의 클래스들이 있다. 나는 Komoran 클래스를 사용해서 형태소를 분석하였다. (Kormoran을 사용한 특별한 이유는 없다.)

##### Implementation

```
$ python tokenize.py 1 < review.refined.regex.tsv > review.refined.regex.tok.tsv
```

