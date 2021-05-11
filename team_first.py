import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

def What_team():
    a= input('야구 팀을 입력하세요>>>')
    if a in Xteam_names:
        for team1 in win_number:
            if a==team1:
             N=win_number[team1]
            else:
                pass
        for team2 in win_rate:
            if a == team2:
                R = win_rate[team2]
            else:
                pass
        return print('{}의 승률은 {}, 승리한 횟수는 {} 입니다.'.format(a, R, N))
    else:
        return print("존재하지 않는 야구팀 입니다")


# 데이터 수집
html=urlopen('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo&year=2021')

soup=BeautifulSoup(html, "lxml")
kbo_table = soup.find_all('tbody', {"id" : "regularTeamRecordList_table"})

# 리스트 제작 시작
kbo_table_tbody=kbo_table[0].find_all("tr")
team_data=[]

for team in kbo_table_tbody:
    td=team.find_all('td')
    such_data=[]
    for content in td:
        a=content.get_text().strip()
        such_data.append(a)
    team_data.append(such_data)

#print(team_data)

# 승률과 팀명 딕셔너리와 승수와 팀명으로 재생성
win_rate={}
win_number={}

#이때 각각을 리스트로 변환: 그래프 그리기 쉽게 만듬
Xteam_names=[]
Ywin_rate=[]
Ywin_number=[]
for team in team_data:
    team_name=team[0]
    Xteam_names.append(team_name)
    team_winRate=team[5]
    Ywin_rate.append(team_winRate)
    team_winNumber=team[2]
    Ywin_number.append(team_winNumber)
    win_rate[team_name]=team_winRate
    win_number[team_name]=team_winNumber

# 팀의 순위를 저장한다
ranking={}
for key in win_rate:
    Rate=win_rate[key]
    rank=1
    if True:
        pass

What_team()