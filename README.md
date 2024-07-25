# 파이썬 argparse 를 이용한 히스토리 cli 고도화 

## 사용방법
```bash
my-history -s {카운트할 명령어입력}
my-history -t {숫자입력} -d {날짜입력}
```

## 메인코드 
```python
import argparse
from ham.db.utils import count, top

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('-s', '--scount')
parser.add_argument('-t', '--top', type=int )
parser.add_argument('-d', '--dt')

args = parser.parse_args()

if args.scount:
    r = count(args.scount)
    print(f"{args.scount}의 총 횟수는 {r}회 입니다.")

elif args.top:
     if args.dt:
        print(top(cnt=args.top, dt=args.dt))
     else:
         parser.error("-t 옵션은 -d 옵션과 함께 사용하시오!")
else:
    parser.print_help()
```

## DB코드
```python
import pandas as pd

def read_data(path='~/data/parquet'):
    df = pd.read_parquet(path)
    return df

def top(cnt, dt):
    df = read_data()
    fdf = df[df['dt'] == dt]
    sdf = fdf.sort_values(by='cnt', ascending=False).head(cnt)
    ddf = sdf.drop(columns=['dt'])

    r = ddf.to_string(index=False)

    return r

def count(query):
    df = read_data()
    fdf = df[df['cmd'].str.contains(query)]
    cnt = fdf['cnt'].sum()
    return cnt
```
