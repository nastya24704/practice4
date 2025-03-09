score=input()
team1, team2=map(int, score.split(':'))
if team1>team2:
    print(team1)
elif team2>team1:
    print(team2)
else:
    print(0)
