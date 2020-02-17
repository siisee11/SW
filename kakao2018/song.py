import re

def trimMelody(song):
	ret=""
	info = re.compile('[A-G]#?').findall(song)
	for i in info:
		if len(i)==2:
			ret+=i[0].lower()
		else:
			ret+=i
	return ret

def timeDiff(stime, ftime):
    stime = int(stime.split(":")[0]) * 60 + int(stime.split(":")[1])
    ftime = int(ftime.split(":")[0]) * 60 + int(ftime.split(":")[1])
    return abs(ftime - stime)

def solution1(m, musicinfos):
    m = trimMelody(m)
    max_t, max_title = 0, "(None)"
    for music in musicinfos:
        played = ''
        musicinfo = music.split(",")
        melody = trimMelody(musicinfo[3])
        duration = timeDiff(musicinfo[0], musicinfo[1])
        title = musicinfo[2]
        for i in range(duration):
            match = 0 
            isFound = False
#            print("Check character start with " + musicinfo[3][i % len(musicinfo[3])])
            for j in range(min(len(m), duration - i)):
                played = melody[(i + j) % len(melody)]
                if played == m[j] :
#                    print("--> Matched! " + played)
                    match += 1
                    if match == len(m) and max_t < duration:
                        max_t, max_title = duration, title
                        isFound = True
                        break
                else :
                    break
            if isFound:
                break

    return max_title

def solution2(m, musicinfos):
    m = trimMelody(m)
    max_t, max_title = 0, "(None)"
    for music in musicinfos:
        played = ''
        musicinfo = music.split(",")
        melody = trimMelody(musicinfo[3])
        duration = timeDiff(musicinfo[0], musicinfo[1])
        title = musicinfo[2]

        for i in range(duration):
            played += melody[i % len(melody)]

        if m in played and max_t < duration:
            max_t, max_title = duration, title
    
    return max_title


def solution(m, musicinfos) :
    return solution1(m, musicinfos)
#    return solution2(m, musicinfos)

if __name__ == "__main__":
    print(solution("CDC#DF", ["12:00,12:05,HELLO,AAAACDC#DFDCDF", "13:00,13:05,WORLD,C#DFCD"]))
    pass