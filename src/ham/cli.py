import argparse

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
    parser.add_argument('-t', '--top')
    parser.add_argument('-d', '--dt')

    args = parser.parse_args()
    print(args.scount, args.top, args.dt)

    if args.scount:
        print(f"-s => {args.scount}")
        #TODO command count
    elif args.top:
        print(f"-t => {args.top}")
        if args.dt:
            print(f"-d => {args.dt}")
            #TODO 특정 날짜의 명령어 TOP N
        else:
            print("TODO - add error message")
            parser.print_help()
    else:
        #TODO - 사용법을 출력한다 
        parser.print_help()
    

