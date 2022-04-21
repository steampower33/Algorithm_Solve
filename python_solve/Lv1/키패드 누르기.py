import math

def solution(numbers, hand):
    answer = ''

    keypad = {1: (0,0), 2: (0,1), 3: (0,2),
              4: (1,0), 5: (1,1), 6: (1,2),
              7: (2,0), 8: (2,1), 9: (2,2),
              '*': (3,0), 0: (3,1), '#': (3,2)}

    lhand = keypad['*']
    rhand = keypad['#']

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            lhand = keypad[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            rhand = keypad[num]
        else:
            d_l = abs(keypad[num][0] - lhand[0]) + abs(keypad[num][1] - lhand[1])
            d_r = abs(keypad[num][0] - rhand[0]) + abs(keypad[num][1] - rhand[1])

            if d_l > d_r:
                answer += 'R'
                rhand = keypad[num]
            elif d_l < d_r:
                answer += 'L'
                lhand = keypad[num]
            elif d_l == d_r:
                if hand == "right":
                    answer += 'R'
                    rhand = keypad[num]
                elif hand == "left":
                    answer += 'L'
                    lhand = keypad[num]

    return answer

if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))