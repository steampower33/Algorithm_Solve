def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

'''

["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"]

index 1의 값이 신고당한 사람이고, 신고당한 횟수가 k 이상이면, 그 사람을 신고한 사람들에게 메일이 발송된다.

받은 메일의 수를 알아내는것

근데 신고 당한 횟수 사전을 {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2} 이렇게 설정했는데

이제 2 이상인 친구들에게서 신고한 사람들에게 메일을 보내야한다.

report를 다시 돌면서 사전에서 2이상인 키의 값에서 index 0의 값이 신고한 사람이다.

이 사람의 이름을 알았으니, 이제 answer에다가 카운트를 해줘야하는데, 이는 id_list에서 순서를 그대로 가져온것이기

index를 통해서 id_list에 index 0번째 값의 배열상 위치를 구하고, 그곳에 값을 1 증가시켜준다.

'''