

def letterChain(index, letter_list):

    start = letter_list[index]
    final_str = start
    letter_list.pop(start)
    letter_list.sort()

    for item in letter_list:
        if item.startswith(start[-1]):
            final_str += item[1:]
    # for item in letter_list:



if __name__ == '__main__':
    index = int(input())
    count = int(input())
    letter_list = []
    for i in range(count):
        letter_list.append(input())
    print(letterChain(index, letter_list))