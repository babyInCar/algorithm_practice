


import re


if __name__ == '__main__':
    source = input().strip()
    target = input().strip()
    match = re.search(target, source)
    print(match.start() if match else -1)
