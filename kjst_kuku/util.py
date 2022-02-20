import sys
import os
import platform
from functools import wraps


def parse_numbers(s):
    numbers = set()
    for n in s.split("/"):
        new_numbers = [int(_) for _ in n.split("-")]
        if len(new_numbers) > 1:
            new_numbers = list(range(new_numbers[0],  new_numbers[1]+1))
        numbers = numbers.union(new_numbers)
    result = list(numbers)
    result.sort()
    return result


def repr_numbers(x):
    """
    [1, 2, 3, 5, 8] -> "1-3/5/8"
    """
    group = []
    s  =  []
    for i, x_ in enumerate(x):
        if len(group) == 0 or x_ == x[i-1] + 1:
            group.append(x_)
        else:
            if len(group) == 1:
                s.append(str(group[0]))
            else:
                s.append(str(group[0]) + "-" +  str(group[-1]))
            group = [x_]

    if len(group) == 1:
        s.append(str(group[0]))
    else:
        s.append(str(group[0]) + "-" +  str(group[-1]))

    return "/".join(s)


def compress_numbers(x):
    """
    x: list of integers. sorted integers with no duplicate.
    out: string. String representation of numbers.
        eg) [2, 3, 7] -> 0b1000110 -> 70
    """
    y = [0] * x[-1]
    for i in x:
        y[-i] = 1
    return int("0b" + "".join(str(_) for _ in y), 2)


def decompress_numbers(y):
    """
    y: integer. To be decoded.
    out: list of sorted integers.
        eg) 70 -> 0b1000110 -> [2, 3, 7]
    """
    y_ = bin(y)[2:]
    x = []
    for i, v in enumerate(reversed(y_)):
        if v == "1":
            x.append(i + 1)
    return x


def graceful(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            out = func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n\n中断します")
            sys.exit()
        return out
    return wrapper
            

def on_ios():
    """Detect a-Shell"""
    machine = platform.machine()
    return machine.startswith("iPad") or machine.startswith("iPhone")


def default_file():
    if on_ios():
        file = "~/Documents/kuku/record.txt"
    else:
        file = "~/.kuku/record.txt"
    
    dir = os.path.dirname(os.path.expanduser(file))
    try:
        os.makedirs(dir)
    except FileExistsError:
        pass 

    return file

    

