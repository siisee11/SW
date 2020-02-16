def solution(cacheSize, cities):
    answer = 0

    cities = [x.lower() for x in cities]

    LRU = []

    if (cacheSize == 0 ):
        return len(cities) * 5

    for city in cities:
        if ( city in LRU ) :
            answer += 1
        else :
            if ( len(LRU) == cacheSize): 
                LRU.pop(0)
            LRU.append(city)
            answer += 5

    return answer


if __name__ == "__main__":
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(3, cities))