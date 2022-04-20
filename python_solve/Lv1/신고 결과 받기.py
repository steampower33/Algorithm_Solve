def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    cnt = dict()
    rep_id = dict()

    for _ in id_list:
        rep_id[_] = []
        cnt[_] = 0

    for _ in report:
        spl = _.split()
        if spl[0] not in rep_id[spl[1]]:
            rep_id[spl[1]].append(spl[0])

    for _ in id_list:
        if len(rep_id[_]) >= k:
            for _ in rep_id[_]:
                cnt[_] += 1

    for _ in range(len(id_list)):
        answer[_] = cnt[id_list[_]]

    return answer