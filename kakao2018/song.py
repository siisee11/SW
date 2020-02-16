def timeDiff(stime, ftime):
    stime = int(stime.split(":")[0]) * 60 + int(stime.split(":")[1])
    ftime = int(ftime.split(":")[0]) * 60 + int(ftime.split(":")[1])
    return ftime - stime

def solution(m, musicinfos):
    max_t, max_title = 0, '(NONE)'
    for music in musicinfos:
        played = ''
        musicinfo = music.split(",")
        duration = timeDiff(musicinfo[0], musicinfo[1])
        for i in range(duration):
            played += musicinfo[3][i % len(musicinfo[3])]
        if played.find(m) != -1 and (played.find(m) + len(m) < len(played) and played[played.find(m) + len(m)] != '#'):
            if (max_t < duration):
                max_t, max_title = duration, max_title

    return max_title

if __name__ == "__main__":
    print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    pass