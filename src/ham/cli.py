import argparse
from ham.db.utils import count, top

def hello_msg():
    return "hello"

def cmd():
    msg = hello_msg()
    print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount')
    parser.add_argument('-t', '--top', type=int)
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
    

