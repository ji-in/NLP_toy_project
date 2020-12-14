# Redirect

리다이렉트는 콘솔의 명령줄에서 '>' 혹은 '<' 를 사용한다.

```python
$ python refine.py < refine.regex.txt
```

이 명령의 모양은 'python refine.py' 라는 명령에 대해서 'refine.regex.txt'라는 파일을 넣어주는 모양으로 생겼다. 이것이 리다이렉트이고, 프로그램에 대한 표준입력을 'refine.regex.txt' 파일로 교체하는 것이다. 이제 소스 코드 내의 'input()'은 키보드가 아닌 텍스트 파일로부터 한줄을 읽는 'f.readline()'과 비슷하게 행동한다.

단순히 호출하는 방법을 바꿨을 뿐인데, 파일을 열어서 출력하는 것처럼 동작하게 했다. 우리는 '<' 연산자를 통해서 표준 입력을 파일로 리다이렉트했다. '>' 연산자는 반대 방향을 가리키는 것처럼 보이는데, 그 느낌대로 프로그램에서 출력되는 내용을 리다이렉트하는 것이다.

출력을 리다이렉트하는 예를 살펴보자.

```python
$ python refine.py < refine.regex.txt > review.refined.tsv
```

'> review.refined.tsv'를 붙이면서 표준출력이 파일로 대체되었기 때문에 화면에 출력되는 내용이 없어진다.