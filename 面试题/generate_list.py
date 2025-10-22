# l1 = [1,2,3.[4,5,6,[7],8],9]

from collections.abc import Iterable


result = []

# def append_list(l1):
#     for item in l1:
#         if isinstance(item, int):
#             yield item
#         elif isinstance(item, Iterable):
#             yield from append_list(item)
#     # return result

def flatten_list(l):

    for item in l:
        if isinstance(item, Iterable):
            yield from flatten_list(item)
        else:
            yield item


if __name__ == '__main__':

    l1 = [1,2,3,[4,5,6,[7],8],9]
    l2 = list(flatten_list(l1))
    print(l2)