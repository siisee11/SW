BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def numToNbase(num, b):
    res = ""
    while num:
        res+=BS[num % b]
        num //= b
    return res[::-1] or "0"

def solution(n, t, m, p):
    answer = ''

    cnt, num = 0, 0

    while True :
        nbase = numToNbase(num, n)
        for c in nbase:
            if cnt % m == p - 1 :
                print(cnt, m, p)
                answer += c
            if len(answer) == t :
                return answer
            cnt += 1
        num += 1

    return answer

if __name__ == "__main__":
    print("[ " + solution(16, 16, 2, 1) + " ]")
    pass