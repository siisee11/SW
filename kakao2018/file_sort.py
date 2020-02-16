def split(word):
    head, digit, tail = '', '', ''
    isNumber, isTail = False, False
    for c in word:
        if c.isdigit() and not isTail:
            isNumber = True
            digit += c
        elif not isNumber :
            head += c
        else :
            if isNumber :
                isTail = True
            tail += c
    return head, digit, tail

def solution(files):
    answer = []

    splited = [ split(x) for x in files ]
    answer = sorted(splited, key= lambda x: (x[0].lower(), int(x[1])))
    answer = list(''.join(x) for x in answer)

    return answer

if __name__ == "__main__":
    input = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "img2-20.jpg"]
    print(solution(input))
    
