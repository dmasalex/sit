import random


def not_active(desk_3, desk_4, desk_5, desk_6):

    for row in range(0, len(desk_3) - 1):
        if desk_3[row].energy and desk_3[row + 1].energy:
            print('active true desk_3')
            random.shuffle(desk_3)

    for row in range(0, len(desk_4) - 1):
        if desk_4[row].energy and desk_4[row + 1].energy:
            print('active true desk_4')
            random.shuffle(desk_4)

    for row in range(0, len(desk_5) - 1):
        if desk_5[row].energy and desk_5[row + 1].energy:
            print('active true desk_5')
            random.shuffle(desk_5)

    for row in range(0, len(desk_6) - 1):
        if desk_6[row].energy and desk_6[row + 1].energy:
            print('active true desk_6')
            random.shuffle(desk_6)

    return desk_3, desk_4, desk_5, desk_6


def create_lst_boys(
        boys_one, girls_one, boys_one_plus, girls_one_plus,
        boys_two, girls_two, boys_two_plus, girls_two_plus,
        boys_three, girls_three, boys_three_plus, girls_three_plus, boys, girls):
    desk_1, desk_2, desk_3, desk_4, desk_5, desk_6 = [], [], [], [], [], []

    while len(desk_1) < 2:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        boy = random.choice(boys_one)
                                        desk_1.append(boy)
                                        boys_one.remove(boy)
                                        continue
                                    except:
                                        girl = random.choice(girls_one)
                                        desk_1.append(girl)
                                        girls_one.remove(girl)
                                        continue
                                except:
                                    girl = random.choice(girls_two)
                                    desk_1.append(girl)
                                    girls_two.remove(girl)
                                    continue
                            except:
                                boy = random.choice(boys_two)
                                desk_1.append(boy)
                                boys_two.remove(boy)
                                continue
                        except:
                            boy = random.choice(boys_three)
                            desk_1.append(boy)
                            boys_three.remove(boy)
                            continue
                    except:
                        girl = random.choice(girls_three)
                        desk_1.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_1.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_1.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_1) < 4:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                try:
                                                    try:
                                                        try:
                                                            try:
                                                                boy = random.choice(boys_one_plus)
                                                                desk_1.append(boy)
                                                                boys_one_plus.remove(boy)
                                                                continue
                                                            except:
                                                                girl = random.choice(girls_one_plus)
                                                                desk_1.append(girl)
                                                                girls_one_plus.remove(girl)
                                                                continue
                                                        except:
                                                            girl = random.choice(girls_two_plus)
                                                            desk_1.append(girl)
                                                            girls_two_plus.remove(girl)
                                                            continue
                                                    except:
                                                        boy = random.choice(boys_two_plus)
                                                        desk_1.append(boy)
                                                        boys_two_plus.remove(boy)
                                                        continue
                                                except:
                                                    boy = random.choice(boys_three_plus)
                                                    desk_1.append(boy)
                                                    boys_three_plus.remove(boy)
                                                    continue
                                            except:
                                                girl = random.choice(girls_three_plus)
                                                desk_1.append(girl)
                                                girls_three_plus.remove(girl)
                                                continue
                                        except:
                                            boy = random.choice(boys_one)
                                            desk_1.append(boy)
                                            boys_one.remove(boy)
                                            continue
                                    except:
                                        girl = random.choice(girls_one)
                                        desk_1.append(girl)
                                        girls_one.remove(girl)
                                        continue
                                except:
                                    boy = random.choice(boys_two)
                                    desk_1.append(boy)
                                    boys_two.remove(boy)
                                    continue
                            except:
                                girl = random.choice(girls_two)
                                desk_1.append(girl)
                                girls_two.remove(girl)
                                continue
                        except:
                            boy = random.choice(boys_three)
                            desk_1.append(boy)
                            boys_two.remove(boy)
                            continue
                    except:
                        girl = random.choice(girls_three)
                        desk_1.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    girl = random.choice(girls)
                    desk_1.append(girl)
                    girls.remove(girl)
                    continue
            except:
                boy = random.choice(boys)
                desk_1.append(boy)
                boys.remove(boy)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_1) < 6:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        girl = random.choice(girls_one)
                                        desk_1.append(girl)
                                        girls_one.remove(girl)
                                        continue
                                    except:
                                        boy = random.choice(boys_one)
                                        desk_1.append(boy)
                                        boys_one.remove(boy)
                                        continue
                                except:
                                    boy = random.choice(boys_two)
                                    desk_1.append(boy)
                                    boys_two.remove(boy)
                                    continue
                            except:
                                girl = random.choice(girls_two)
                                desk_1.append(girl)
                                girls_two.remove(girl)
                                continue
                        except:
                            girl = random.choice(girls_three)
                            desk_1.append(girl)
                            girls_three.remove(girl)
                            continue
                    except:
                        boy = random.choice(boys_three)
                        desk_1.append(boy)
                        boys_three.remove(boy)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_1.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_1.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_2) < 2:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                girl = random.choice(girls_two)
                                desk_2.append(girl)
                                girls_two.remove(girl)
                                continue
                            except:
                                boy = random.choice(boys_two)
                                desk_2.append(boy)
                                boys_two.remove(boy)
                                continue
                        except:
                            boy = random.choice(boys_three)
                            desk_2.append(boy)
                            boys_three.remove(boy)
                            continue
                    except:
                        girl = random.choice(girls_three)
                        desk_2.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    girl = random.choice(girls)
                    desk_2.append(girl)
                    girls.remove(girl)
                    continue
            except:
                boy = random.choice(boys)
                desk_2.append(boy)
                boys.remove(boy)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_2) < 4:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                try:
                                    try:
                                        try:
                                            try:
                                                boy = random.choice(boys_two_plus)
                                                desk_2.append(boy)
                                                boys_two_plus.remove(boy)
                                                continue
                                            except:
                                                girl = random.choice(girls_two_plus)
                                                desk_2.append(girl)
                                                girls_two_plus.remove(girl)
                                                continue
                                        except:
                                            boy = random.choice(boys_three_plus)
                                            desk_2.append(boy)
                                            boys_three_plus.remove(boy)
                                            continue
                                    except:
                                        girl = random.choice(girls_three_plus)
                                        desk_2.append(girl)
                                        girls_three_plus.remove(girl)
                                        continue
                                except:
                                    girl = random.choice(girls_two)
                                    desk_2.append(girl)
                                    girls_two.remove(girl)
                                    continue
                            except:
                                boy = random.choice(boys_two)
                                desk_2.append(boy)
                                boys_two.remove(boy)
                                continue
                        except:
                            boy = random.choice(boys_three)
                            desk_1.append(boy)
                            boys_three.remove(boy)
                            continue
                    except:
                        girl = random.choice(girls_three)
                        desk_2.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    girl = random.choice(girls)
                    desk_2.append(girl)
                    girls.remove(girl)
                    continue
            except:
                boy = random.choice(boys)
                desk_2.append(boy)
                boys.remove(boy)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_2) < 6:
        try:
            try:
                try:
                    try:
                        try:
                            try:
                                boy = random.choice(boys_two)
                                desk_2.append(boy)
                                boys_two.remove(boy)
                                continue
                            except:
                                girl = random.choice(girls_two)
                                desk_2.append(girl)
                                girls_two.remove(girl)
                                continue
                        except:
                            boy = random.choice(girls_three)
                            desk_2.append(boy)
                            girls_three.remove(boy)
                            continue
                    except:
                        boy = random.choice(boys_three)
                        desk_1.append(boy)
                        boys_three.remove(boy)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_2.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_2.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    # рассаживаем 3 парту
    while len(desk_3) < 2:
        try:
            try:
                try:
                    try:
                        boy = random.choice(boys_three)
                        desk_3.append(boy)
                        boys_three.remove(boy)
                        continue
                    except:
                        girl = random.choice(girls_three)
                        desk_3.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_3.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_3.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_3) < 4:
        try:
            try:
                try:
                    try:
                        boy = random.choice(boys_three_plus)
                        desk_3.append(boy)
                        boys_three_plus.remove(boy)
                        continue
                    except:
                        girl = random.choice(girls_three_plus)
                        desk_3.append(girl)
                        girls_three_plus.remove(girl)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_3.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_3.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    while len(desk_3) < 6:
        try:
            try:
                try:
                    try:
                        boy = random.choice(boys_three)
                        desk_3.append(boy)
                        boys_three.remove(boy)
                        continue
                    except:
                        girl = random.choice(girls_three)
                        desk_3.append(girl)
                        girls_three.remove(girl)
                        continue
                except:
                    boy = random.choice(boys)
                    desk_3.append(boy)
                    boys.remove(boy)
                    continue
            except:
                girl = random.choice(girls)
                desk_3.append(girl)
                girls.remove(girl)
                continue
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    # рассаживаем 4 парту
    if len(girls) + len(boys) != 0:
        while len(desk_4) != 6:
            try:
                try:
                    try:
                        boy = random.choice(boys)
                        desk_4.append(boy)
                        boys.remove(boy)
                        girl = random.choice(girls)
                        desk_4.append(girl)
                        girls.remove(girl)
                    except:
                        boy = random.choice(boys)
                        desk_4.append(boy)
                        boys.remove(boy)
                except:
                    girl = random.choice(girls)
                    desk_4.append(girl)
                    girls.remove(girl)
            except:
                return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    # рассаживаем 5 парту
    while len(desk_5) != 6 and len(girls) + len(boys) != 0:
        try:
            try:
                try:
                    boy = random.choice(boys)
                    desk_5.append(boy)
                    boys.remove(boy)
                    girl = random.choice(girls)
                    desk_5.append(girl)
                    girls.remove(girl)
                except:
                    boy = random.choice(boys)
                    desk_5.append(boy)
                    boys.remove(boy)
            except:
                girl = random.choice(girls)
                desk_5.append(girl)
                girls.remove(girl)
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    # рассаживаем 6 парту
    while len(desk_6) != 6 and len(girls) + len(boys) != 0:
        try:
            try:
                try:
                    boy = random.choice(boys)
                    desk_6.append(boy)
                    boys.remove(boy)
                    girl = random.choice(girls)
                    desk_6.append(girl)
                    girls.remove(girl)
                except:
                    boy = random.choice(boys)
                    desk_6.append(boy)
                    boys.remove(boy)
            except:
                girl = random.choice(girls)
                desk_6.append(girl)
                girls.remove(girl)
        except:
            return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6

    tmp_lst = [desk_1.pop(2), desk_1.pop(2)]
    random.shuffle(tmp_lst)
    random.shuffle(desk_1)
    desk_1 = [desk_1[0], desk_1[1], tmp_lst[0], tmp_lst[1], desk_1[2], desk_1[3]]

    return desk_1, desk_2, desk_3, desk_4, desk_5, desk_6
