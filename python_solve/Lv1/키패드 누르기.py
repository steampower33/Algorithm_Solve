import math

def solution(numbers, hand):
    answer = ''

    keypad = {1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (3, 1), 8: (3, 2), 9: (3, 3), 0: (4, 2)}

    dist_l = (4,1)
    dist_r = (4,3)

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            dist_l = keypad[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            dist_r = keypad[num]
        else:
            d_l = math.sqrt((keypad[num][0] - dist_l[0]) ** 2 + abs(keypad[num][1] - dist_l[1]) ** 2)
            d_r = math.sqrt((keypad[num][0] - dist_r[0]) ** 2 + abs(keypad[num][1] - dist_r[1]) ** 2)
            if math.floor(d_l) == d_l:
                d_l = d_l
            else:
                d_l = math.floor(d_l) + 1

            if math.floor(d_r) == d_r:
                d_r = d_r
            else:
                d_r = math.floor(d_r) + 1

            if d_l > d_r:
                answer += 'R'
                dist_r = keypad[num]
            elif d_l < d_r:
                answer += 'L'
                dist_l = keypad[num]
            elif d_l == d_r:
                if hand == "right":
                    answer += 'R'
                    dist_r = keypad[num]
                elif hand == "left":
                    answer += 'L'
                    dist_l = keypad[num]

    return answer

if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))