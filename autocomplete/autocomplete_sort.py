def overlap(one, two):
    cnt = 0
    for o, t in zip(one, two):
        if o == t :
            cnt += 1
        else :
            break
    return cnt


def solution(words):
    answer = 0

    words.sort()

    prev = 0
    for i in range(len(words)-1):
        current, nxt = words[i], words[i + 1]
        print("current: ", current, "next: ", nxt)
        ovl = overlap(current, nxt)
        answer += min(max(prev + 1 , ovl + 1), len(current))
        prev = ovl
    
    answer += min(prev + 1, len(words[-1]))

    print("[ " + str(answer) + " ]")
    return answer


if __name__ == "__main__":
    words = ["go", "gone", "guild"]
    answer = 7
    if solution(words) == answer:
        print("PASS")
    else:
        print("FAIL")