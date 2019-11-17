from itertools import combinations

n,m = map(int,input().split())
cards_list = list(map(int,input().split()))
biggest_sum = 0

for cards in combinations(cards_list, 3):
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= m:
        biggest_sum = temp_sum

print(biggest_sum)
