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
    if args.url is None:
        print("ERROR : enter USERNAME list path with -u switch")
        exit()
    urls = []
    url_file = open(f"{args.url}", "r")
    for url in url_file:
        urls.append(url.rstrip())

    total = urls.__len__()
    print("\n****************************************")
    print(F"     START TO Downloading {total} ITEMS")
    print("****************************************\n")
    prog = 0
    for url in urls:
        progress(prog, total, " downloading")
        prog += 1
        req = requests.get(url, allow_redirects=True)
        if req.status_code != 200:
        	req = requests.get(url, allow_redirects=True)
        
        file_name = url.rsplit('/',1)[-1]
        with open(f'{file_name}', 'wb') as f:
        	f.write(req.content)


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '|' * filled_len + '.' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
