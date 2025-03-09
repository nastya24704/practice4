print('Собака короткошерстной породы?')
answer1=input()
if answer1=='да':
    print('Рост собаки менее 50 см?')
    answer2 = input()
    if answer2 == 'да':
        print('У собаки короткий хвост?')
        answer3 = input()
        if answer3 == 'да':
            print('английский бульдог')
        else:
            print('у собаки длинные уши?')
            answer4 = input()
            if answer4 == 'да':
                print('гончая')
            else:
                print('у собаки короткое тело?')
                answer5 = input()
                if answer5 == 'да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        print('Собака весит более 50 кг?')
        answer3=input()
        if answer3 == 'да':
            print('датский дог')
        else:
            print('фоксхаунд')
else:
    print('Рост собаки менее 50 см?')
    answer2 = input()
    if answer2 == 'да':
        print('У собаки доброжелательный характер?')
        answer3 = input()
        if answer3 == 'да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        print('У собаки рост менее 70 см?')
        answer3 = input()
        if answer3 == 'да':
            print('У собаки длинные уши?')
            answer4 = input()
            if answer4 == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            print('Окрас рыжий с белыми отметинами?')
            answer4=input()
            if answer4=='да':
                print('сенбернар')
            else:
                print('Белоснежный окрас?')
                answer5 = input()
                if answer5 == 'да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')
