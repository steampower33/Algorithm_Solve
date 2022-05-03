def solution(sizes):
    # w 가로, h 세로
    less = 0
    better = 0
    for _ in sizes:
        if _[0] <= _[1]:
            if less < _[0]:
                less = _[0]
            if better < _[1]:
                better = _[1]
        elif _[0] >= _[1]:
            if less < _[1]:
                less = _[1]
            if better < _[0]:
                better = _[0]

    return less * better