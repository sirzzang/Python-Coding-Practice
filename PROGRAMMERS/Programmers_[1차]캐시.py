def solution(cacheSize, cities):
    answer = 0
    
    # 예외: Cache 저장 불가
    if cacheSize == 0:
        return len(cities) * 5
    
    q = []
    for city in cities:
        city = city.lower() # 대소문자 구분 제거
        # Cache hit일 때
        if city in q:
            answer += 1
            q.append(q.pop(q.index(city)))
        # Cache miss일 때
        else:          
            answer += 5
            if len(q) < cacheSize: # cache 다 안 찼을 때
                q.append(city)
            else: # cache 다 찼을 때
                q.pop(0)
                q.append(city)
    return answer