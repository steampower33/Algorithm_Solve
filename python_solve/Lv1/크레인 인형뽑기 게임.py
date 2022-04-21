def solution(board, moves):
    answer = 0

    basket = list()

    for m in moves:

        for idx in range(len(board)):

            if board[idx][m - 1] > 0:
                basket.append(board[idx][m - 1])
                board[idx][m - 1] = 0

                if basket[-1:] == basket[-2:-1]:
                    answer += 2
                    basket = basket[:-2]
                break
    return answer

print(solution([[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[3,3,4,3,3],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

'''
배열에 초기값이 있을지 없을지 모르는 상황에서 list[-2] 처럼 확실한 index를 지정하지말고,
list[-2:-1] 처럼 범위로 지정하면, 값이 없을때는 빈 배열로 나오게된다.
이것으로 index out of range 오류를 피해갈수있음

'''