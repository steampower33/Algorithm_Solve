# 긴수는 짧은수의 접두사가 될수없다.

def solution(phone_book):

    answer = True

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) < len(phone_book[j]):
                if phone_book[j].startswith(phone_book[i]) == True:
                    return False
            elif len(phone_book[i]) > len(phone_book[j]):
                if phone_book[i].startswith(phone_book[j]) == True:
                    return False
    return answer

if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    phone_book = ["123", "134", "145353", "1925", "340529", "145353241241"]
    print(solution(phone_book))