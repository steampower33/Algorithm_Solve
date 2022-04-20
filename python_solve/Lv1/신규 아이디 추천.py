def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    temp = ''
    # 2단계
    for _ in new_id:
        if _.isalnum() or _ in '-_.':
            temp = temp + _

    new_id = temp

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if new_id[0] == '.' and len(new_id) > 1: new_id = new_id[1:]
    if new_id[-1] == '.': new_id = new_id[:-1]

    # 5단계
    if new_id == '': new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        last_char = new_id[-1]
        while len(new_id) < 3:
            new_id += last_char

    return new_id

'''
# 이런게 정규식이다...

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
    


'''