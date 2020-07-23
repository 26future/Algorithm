N = int(input())
S = []
for i in range(N):
    tmp_s = input().split()
    tmp_s = list(map(lambda x:int(x), tmp_s))
    S.append(tmp_s)

# 각 팀별 선수 조합
from itertools import combinations

player_idx = list(range(N))
team = list(combinations(player_idx, int(N/2)))

team1 = team[0:int(len(team)/2)]
team2 = team[int(len(team)/2):][::-1]


# team1의 능력치 조합
from itertools import permutations

S_team1 = []
for players in team1:
    s = 0
    players_s = list(permutations(players,2))
    for idx in players_s:
        s += (S[idx[0]][idx[1]])
    S_team1.append(s)

# team2의 능력치 조합
S_team2 = []
for players in team2:
    s = 0
    players_s = list(permutations(players,2))
    for idx in players_s:
        s += (S[idx[0]][idx[1]])
    S_team2.append(s)


# team1과 team2의 능력치 차이
S_difference = []
for i in range(len(S_team1)):
    d = abs(S_team1[i]-S_team2[i])
    S_difference.append(d)

print(min(S_difference))
