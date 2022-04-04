def solution(phone_book):

    answer = True

    #string과 int형의 정렬은 다르다.
    phone_book.sort()

    for _ in range(len(phone_book)-1):
        if str(phone_book[_+1]).startswith(str(phone_book[_])) == True:
            return False

    return answer

if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    phone_book = ["123", "134", "1234", "1925", "340529", "145353241241"]
    print(solution(phone_book))