gpu 머신에서 꺼지지 않도록 학습시키기 위해 백그라운드로 실행한다.

```bash
# background로 실행시키는 방법(창을 종료하면 terminate 됨) 
python [filename].py &

# 창을 종료해도 돌아가게
nohup python [filename].py &

# print문을 바로 보고싶다면 옵션 -u를 사용
nohup python -u filename -u filename.py &

# 프로세스 확인 
ps -ef | grep [filename]

# 프로세스 종료 
kill [process id]
```

