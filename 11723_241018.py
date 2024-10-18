# 11723 (집합)

stack = set()

def add(x):
    return stack.add(x)

def remove(x):
    return stack.discard(x)

def check(x):
    if x in stack:
        return print(1)
    else:
        return print(0)

def toggle(x):
    if x in stack:
        return stack.remove(x)
    else:
        return stack.add(x)

N = int(input())

for _ in range(N):
    sen = input()
    if 'add' in sen:
        add(int(sen[4:]))
    elif 'remove' in sen:
        remove(int(sen[7:]))
    elif 'check' in sen:
        check(int(sen[6:]))
    elif 'toggle' in sen:
        toggle(int(sen[7:]))
    elif 'all' in sen:
        stack = set(range(1,21))
    else:
        stack = set()