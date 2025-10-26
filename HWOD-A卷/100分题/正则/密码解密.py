

import re

def main():
    input_str = input()

    for i in range(26,0,-1):
        reg_str = str(i)
        if i > 9:
            reg_str += r"\*"
        replace_char = chr(ord('a') + i - 1)
        input_str = re.sub(reg_str, replace_char, input_str)
    print(input_str)


if __name__ == '__main__':
    main()