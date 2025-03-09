score=input()
Kirill, Arina, Sergey=map(int, score.split())
if Kirill>Arina and Kirill>Sergey:
    print(Kirill)
elif Kirill>Arina and Kirill<Sergey:
    print(Sergey)
elif Kirill<Arina and Kirill>Sergey:
    print(Arina)
else:
    print(0)
