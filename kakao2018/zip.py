import string

def solution(msg):
    dic = dict(zip(string.ascii_uppercase, range(1, 27)))
    answer = []

    i = 0
    while i < len(msg) : 
        next_i = 2
        while True :
            if i + next_i > len(msg) :
                break
            if msg[i:i+next_i] not in dic :
                dic[msg[i:i+next_i]] = len(dic) + 1
                break
            else :
                next_i += 1

        answer.append(dic[msg[i:i+next_i - 1]])
        i += next_i - 1

    print("[ ANSWER : " + str(answer) + " ]")
    return answer


if __name__ == "__main__":
    solution("KAKAO")
    pass