# enumerate + dictionary 사용한 구현
# 같은 value가 있다면 무조건 index 순서대로 정렬이 되어 버리기 때문에 문제가 된다.

import sys

n, m = map(int, sys.stdin.readline().split())
papers = [int(i) for i in sys.stdin.readline().split()]

papers_dict = {idx:value for (idx, value) in enumerate(papers)} # idx를 key로, value를 value로 하여 dict 생성
print(papers_dict)

papers = sorted(papers_dict.items(), key = lambda item : -item[1]) # 오름차순으로 정렬해야 함.
print(papers)

for paper in papers: # idx가 m인 애의 위치를 뽑으면 됨.
    if paper[0] == m:
        print(papers.index(paper) + 1)