import random
import os
import math

name=input("Введите ваше ИМЯ: ")
print("Добро пожаловать в ИГРУ THE KINGDOM OF AIMS,",name,"!")
Dname= input("Введите название свего КОРОЛЕВСТВА: ")
print("Вы,",name,", необыкновеный и величественный КОРОЛЬ и ПРАВИТЕЛЬ!")
print(Dname,"-ваш дом, родина и отчизна!Ваша цель - максимально выгодно развивать и улучшать ваше государство.")
print("Да начнется же ИГРА!")

def iv1():
    print("---К вам пришел опытный воин.. Он хочет вступиь в ряды вашей армии!")
    print("---Вы с недоумевая смотрите ему в лицо и не знаете что делать.")
    print("1 Принять воина в ряды армии. \n2 Отвергнуть его предложение!")
    choise = int(input())
    if choise == 1:
        lucky = random.randint(0,11)
        if lucky < 5:
            print("ОН ОКАЗАЛСЯ ВРАЖЕСКИМ ЛАЗУТЧИКОМ!!!")
            print("Ваша СИЛА уменьшена на 2 единицы.")
            enter = input()
            return -2
        else:
            print("ДОСТОЙНЕЙШИЙ ВОИН ВСТУПИЛ В ВАШУ АРМИЮ")
            print("Ваша сила увеличена на 2 единицы ")
            enter = input()
            return 2
    return 0
def iv2():
    print("---Соседняя деревня предлагеат вам обмен 60 железа на 120 золота.")
    print("---Вы не знаете что делать.")
    print("1 Совершить сделку \n2 Не совершать сделку")
    choise = int(input())
    if choise == 1:
        print("Вы совершили сделку!")
        enter = input()
        return 60
    if choise == 2:
        print("Сделка отменена!")
        enter = input()
        return 0
    return 0

def iv3():
    print("---Вы замечаете странного инженера, который предлагает вам улучшить стены города за 90 монет!")
    print("---Вы не знаете что делать.")
    print("1 Дать ему денги. \n2 Прогнать его!")
    choise = int(input())
    if choise == 1:
        lucky = random.randint(0,11)
        if lucky <=7:
            print("Стены улучшены! ЗДОРОВЬЕ ПОВЫШЕНО НА 20 ЕДИНИЦ!")
            enter = input()
            return 20
        else:
            print("Этот жалкий трус испорил вашу оборону, забрав деньги!")
            enter = input()
            return -10
    if choise == 2:
        print("Вы его прогнали!")
        return 0
    return 0

def iv4():
    print("---Вы замечаете группу беженцов из другой деревни! Прося у вас помощь они говорят,что потеряли дом в войне!")
    print("---Вы не знаете что делать.")
    print("1 Разрешить жить в вашей деревни,дав немного монет(30). \n2 Прогнать их!")
    choise = int(input())
    if choise == 1:
        lucky = random.randint(0,11)
        if lucky <=5:
            print("Беженцы благодарны вам!.Они оказываются замечательными поселенцами!")
            print("ФЕРМА улучшена на 2 единицы!")
            enter = input()
            return 2
        else:
            print("ОНИ ОБМАНУЛИ ВАС!!! Это оказались наглые воры! Потеряно 50 монет!!!")
            enter = input()
            return -50
    if choise == 2:
        print("Вы их прогнали!")
        return 0
    return 0

def iv5(scales):
      print("---На вас напал ДРАКОН!!!")
      iventt = {'АТАКИ':0,'ЗАЩИТА':scales['ЗДОРОВЬЕ']//20}
      defense(scales, iventt)

def printdata(scales,resource,ivent):
    print(scales)
    print(resource)
    print(ivent)

def save(scales,resource,ivent):
    f = open('saves.txt', 'w')
    f.write(str(scales['СИЛА'])+ '\n')
    f.write(str(scales['ЗДОРОВЬЕ'])+ '\n')
    f.write(str(scales['ФЕРМА'])+ '\n')
    f.write(str(scales['ЛЕСОПИЛКА'])+ '\n')
    f.write(str(scales['ШАХТА'])+ '\n')
    f.write(str(scales['УРОВЕНЬ_ГОРОДА'])+ '\n')
    f.write(str(resource['ДЕНЬГИ'])+ '\n')
    f.write(str(resource['ЕДА'])+ '\n')
    f.write(str(resource['ДЕРЕВО'])+ '\n')
    f.write(str(resource['ЖЕЛЕЗО'])+ '\n')
    f.write(str(ivent['АТАКИ'])+ '\n')
    f.write(str(ivent['ЗАЩИТА'])+ '\n')
    f.close()

def load():
    f = open('saves.txt', 'r')
    l = f.read()
    data = list(map(int, l.strip().split('\n')))
    f.close()
    return data
     
def defense(scales,ivent):
    heal = scales['ЗДОРОВЬЕ']
    lvl = scales['СИЛА'] - ivent['ЗАЩИТА']
    if lvl < 0:
        lvl = 0
    if lvl > 7:
        lvl = 7
    for i in range (10 - lvl):
        print('Здоровье стен',scales['ЗДОРОВЬЕ'])
        lucky = random.randint(0,11)
        if (lucky < 5):
            print('Вы отбили атаку')
        else:
            damage = ivent['ЗАЩИТА'] + 1
            print('Вам нанесли:',damage,'урона!')
            scales['ЗДОРОВЬЕ'] = scales['ЗДОРОВЬЕ'] - damage
            if (scales['ЗДОРОВЬЕ'] <= 0):
                print('ВАШУ ДЕРЕВНЮ УНИЧТОЖИЛИ!!! GAME OVER.')
                enter = input()
                exit(0)
        enter = input()
    print('Поздравляю, вы смогли ЗАЩИТИТЬСЯ!')
    scales['ЗДОРОВЬЕ'] = heal
    
    

def searching():
    m = random.randint(0,31)
    f = random.randint(0,31)
    w = random.randint(0,31)
    i = random.randint(0,31)
    print('ВАША ДОБЫЧА:')
    print(m,'монет.')
    print(f,'еды.')
    print(w,'дерева.')
    print(i,'железа.')
    enter = input()
    res = [m,f,w,i]
    return res

def fighting():
    m = random.randint(50,151)
    f = random.randint(31,71)
    w = random.randint(31,71)
    i = random.randint(31,71)
    print('ВАША ДОБЫЧА:')
    print(m,'монет.')
    print(f,'еды.')
    print(w,'дерева.')
    print(i,'железа.')
    enter = input()
    res = [m,f,w,i]
    return res

def start():
    scales = {'СИЛА': 1,'ЗДОРОВЬЕ': 10,'ФЕРМА': 1,'ЛЕСОПИЛКА': 1,'ШАХТА': 1,'УРОВЕНЬ_ГОРОДА': 1}
    resource = {'ДЕНЬГИ':300,'ЕДА':100,'ДЕРЕВО':100,'ЖЕЛЕЗО':100}
    ivent = {'АТАКИ':0,'ЗАЩИТА':0}
    print('1 Вы хотите начать заново? \n2 Загрузить прошлую игру?')
    choise = int(input())
    if (choise == 2):
        data = load()
        scales['СИЛА'] = data[0]
        scales['ЗДОРОВЬЕ'] = data[1]
        scales['ФЕРМА'] = data[2]
        scales['ЛЕСОПИЛКА'] = data[3]
        scales['ШАХТА'] = data[4]
        scales['УРОВЕНЬ_ГОРОДА'] = data[5]
        resource['ДЕНЬГИ'] = data[6]
        resource['ЕДА'] = data[7]
        resource['ДЕРЕВО'] = data[8]
        resource['ЖЕЛЕЗО'] = data[9]
        ivent['АТАКИ'] = data[10]
        ivent['ЗАЩИТА'] = data[11]
        
    while (True):
        os.system('CLS')
        printdata(scales,resource,ivent)
        while True:
            os.system('CLS')
            printdata(scales,resource,ivent)
            print()
            print('ПОДГОТОВИТЕЛЬНАЯ СТАДИЯ. УЛУЧШЕНИЕ!')
            print()
            print('0 ДАЛЕЕ...')
            print('1 СИЛА. Можно улучшить за',scales['СИЛА']*20,'золота.')
            print('2 ЗДОРОВЬЕ. Можно улучшить за',scales['ЗДОРОВЬЕ']*2,'золота.')
            print('3 ФЕРМА. Можно улучшить за',scales['ФЕРМА']*20,'золота.')
            print('4 ЛЕСОПИЛКА. Можно улучшить за',scales['ЛЕСОПИЛКА']*20,'золота.')
            print('5 ШАХТА. Можно улучшить за',scales['ШАХТА']*20,'золота.')
            print('6 ГОРОД. Можно улучшить за',scales['УРОВЕНЬ_ГОРОДА']*100,'золота.')
            print('7 Сохранить игру.')
            choise = int(input())
            if choise == 1:
                if scales['УРОВЕНЬ_ГОРОДА']*5 >scales['СИЛА']:
                    if resource['ДЕНЬГИ'] >= scales['СИЛА']*20:
                        resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['СИЛА']*20
                        scales['СИЛА'] = scales['СИЛА'] + 1
                        print('Вы улучшили СИЛУ!')
                    else:
                        print('Недостаточно денег!')
                else:
                    print('Вы достигли максимального улучшения, улучшите город!')
            if choise == 2:
                if scales['УРОВЕНЬ_ГОРОДА']*5 > scales['ЗДОРОВЬЕ']/10:
                    if resource['ДЕНЬГИ'] >= scales['ЗДОРОВЬЕ']*2:
                        resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['ЗДОРОВЬЕ']*2
                        scales['ЗДОРОВЬЕ'] = scales['ЗДОРОВЬЕ'] + 10
                        print('Вы улучшили ЗДОРОВЬЕ!')
                    else:
                        print('Недостаточно денег!')
                else:
                    print('Вы достигли максимального улучшения, улучшите город!')
            if choise == 3:
                if scales['УРОВЕНЬ_ГОРОДА']*5 > scales['ФЕРМА']:
                    if resource['ДЕНЬГИ'] >= scales['ФЕРМА']*20:
                        resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['ФЕРМА']*20
                        scales['ФЕРМА'] = scales['ФЕРМА'] + 1
                        print('Вы улучшили ФЕРМУ!')
                    else:
                        print('Недостаточно денег!')
                else:
                    print('Вы достигли максимального улучшения, улучшите город!')
            if choise == 4:
                if scales['УРОВЕНЬ_ГОРОДА']*5 >scales['ЛЕСОПИЛКА']:
                    if resource['ДЕНЬГИ'] >= scales['ЛЕСОПИЛКА']*20:
                        resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['ЛЕСОПИЛКА']*20
                        scales['ЛЕСОПИЛКА'] = scales['ЛЕСОПИЛКА'] + 1
                        print('Вы улучшили ЛЕСОПИЛКУ!')
                    else:
                        print('Недостаточно денег!')
                else:
                    print('Вы достигли максимального улучшения, улучшите город!')
            if choise == 5:
                if scales['УРОВЕНЬ_ГОРОДА']*5 >scales['ШАХТА']:
                    if resource['ДЕНЬГИ'] >= scales['ШАХТА']*20:
                        resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['ШАХТА']*20
                        scales['ШАХТА'] = scales['ШАХТА'] + 1
                        print('Вы улучшили ШАХТУ!')
                    else:
                        print('Недостаточно денег!')
                else:
                    print('Вы достигли максимального улучшения, улучшите город!')
            if choise == 6:
                if resource['ДЕНЬГИ'] >= scales['УРОВЕНЬ_ГОРОДА']*100:
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - scales['УРОВЕНЬ_ГОРОДА']*100
                    scales['УРОВЕНЬ_ГОРОДА'] = scales['УРОВЕНЬ_ГОРОДА'] + 1
                    print('Вы улучшили УРОВЕНЬ ГОРОДА!')
            if choise == 0:
                break
            if choise == 7:
                save(scales,resource,ivent)
                print('Сохранение прошло успешно')
            enter = input()

        print('1 Атаковать соседнюю деревню')
        print('2 Иследовать руины')
        print('3 Обменять ресурсы')
        print('4 Выйти')
        

        choise = int(input())
        if (choise == 1):
            print ('ВЫ АТАКОВАЛИ ДЕРЕВНЮ!!!')
            if scales['СИЛА']> (ivent['АТАКИ']+1)*2:
                print('ПОБЕДА!!!')
                res = fighting()
                resource['ЕДА'] = resource['ЕДА'] + res[1]
                resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + res[2]
                resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + res[3]
                resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + res[0]
                ivent['АТАКИ'] = (ivent['АТАКИ']+1) + 1
            elif 2 * scales['СИЛА']< ivent['АТАКИ']:
                print('ПОРАЖЕНИЕ!!! Потеряно 20 единиц еды и денег!')
                resource['ЕДА'] = resource['ЕДА'] - 20
                resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - 20
                enter = input()
            else:
                lucky = random.randint(0,11)
                if lucky < 5:
                    print('ПОРАЖЕНИЕ!!! Потеряно 20 единиц еды и денег!')
                    resource['ЕДА'] = resource['ЕДА'] - 20
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - 20
                    enter = input()
                else:
                    print('ПОБЕДА!!!')
                    res = fighting()
                    resource['ЕДА'] = resource['ЕДА'] + res[1]
                    resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + res[2]
                    resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + res[3]
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + res[0]
                    ivent['АТАКИ'] = ivent['АТАКИ'] + 1
                
        if (choise == 2):
            print ('Добро пожаловать в ИССЛЕДОВАНИЕ:')
            res = searching()
            resource['ЕДА'] = resource['ЕДА'] + res[1]
            resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + res[2]
            resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + res[3]
            resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + res[0]
        if (choise == 3):
            print('Добро пожаловать на РЫНОК:')
            print("ВНИМАНИЕ: ознакомтесь с условиями! Обмен осуществляется в отношении 5:2 в независимости от товара!")
            print("Если вы предлагаете обменять ресурсов больше чем у вас есть, то рынок автоматически забирает у вас ВЕСЬ товар на продажу!")
            print('Вы можете сделать обмен:')
            print('1 ДЕНЬГИ на дерево 5:2')
            print('2 ДЕНЬГИ на железо 5:2')
            print('3 ДЕНЬГИ на еду 5:2')
            print('4 Дерево на ДЕНЬГИ 5:2')
            print('5 Железо на ДЕНЬГИ 5:2')
            print('6 Еду на ДЕНЬГИ 5:2')
            cho = int(input())
            if cho == 4:
                col = int(input('Сколько Дерева хотите поменять? '))
                if col > resource['ДЕРЕВО']:
                    col = resource['ДЕРЕВО']
                    resource['ДЕРЕВО'] = resource['ДЕРЕВО'] - resource['ДЕРЕВО']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
                else:
                    resource['ДЕРЕВО'] = resource['ДЕРЕВО'] - col
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
            if cho == 5:
                col = int(input('Сколько Железа хотите поменять? '))
                if col > resource['ЖЕЛЕЗО']:
                    col = resource['ЖЕЛЕЗО']
                    resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] - resource['ЖЕЛЕЗО']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
                else:
                    resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] - col
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
            if cho == 6:
                col = int(input('Сколько Еды хотите поменять? '))
                if col > resource['ЕДА']:
                    col = resource['ЕДА']
                    resource['ЕДА'] = resource['ЕДА'] - resource['ЕДА']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
                else:
                    resource['ЕДА'] = resource['ЕДА'] - col
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + math.floor((col / 5)) * 2
            if cho == 1:
                col = int(input('Сколько Денег хотите поменять на дерево? '))
                if col > resource['ДЕНЬГИ']:
                    col = resource['ДЕНЬГИ']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - resource['ДЕНЬГИ']
                    resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + math.floor((col / 5)) * 2
                else:
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - col
                    resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + math.floor((col / 5)) * 2
            if cho == 2:
                col = int(input('Сколько Денег хотите поменять на железо? '))
                if col > resource['ДЕНЬГИ']:
                    col = resource['ДЕНЬГИ']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - resource['ДЕНЬГИ']
                    resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + math.floor((col / 5)) * 2
                else:    
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - col
                    resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + math.floor((col / 5)) * 2
            if cho == 3:
                col = int(input('Сколько Денег хотите поменять на еду? '))
                if col > resource['ДЕНЬГИ']:
                    col = resource['ДЕНЬГИ']
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - resource['ДЕНЬГИ']
                    resource['ЕДА'] = resource['ЕДА'] + math.floor((col / 5)) * 2
                else:
                    resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - col
                    resource['ЕДА'] = resource['ЕДА'] + math.floor((col / 5)) * 2
            print('Обмен произошел УСПЕШНО!')
            enter = input()
        if choise == 4:
            save(scales,resource,ivent)
            exit(0)

        lucky = random.randint(0,18)
        if (lucky <=2):
            scales['СИЛА'] = scales['СИЛА'] + iv1()
        if (lucky > 2  and lucky <= 4):
            event = iv3()
            scales['ЗДОРОВЬЕ'] = scales['ЗДОРОВЬЕ'] + event
            resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - 90
        if (lucky >= 5 and  lucky <=6 and resource['ЖЕЛЕЗО'] >= 60):
            event = iv2()
            resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] - event
            resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + event*2
        if (lucky > 6 and lucky <=8):
            event = iv4()
            resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] - 30
            if event == 2:
                scales['ФЕРМА'] = scales['ФЕРМА'] + event
            else:
                resource['ДЕНЬГИ'] = resource['ДЕНЬГИ'] + event
        if (lucky > 8 and lucky <=10):
            iv5(scales)
            scales['СИЛА'] = scales['СИЛА'] + 3
            print('Вы победили ДРАКОНА, ваша сила увеличена на 3!')
            enter = input()


        lucky = random.randint(0,11)
        if (lucky <= 3):
            print('НА ВАС НАПАЛИ!!! СТАДИЯ ОБОРОНЫ!')
            defense(scales,ivent)
            ivent['ЗАЩИТА'] = ivent['ЗАЩИТА'] + 1 
            enter = input()
        
        resource['ЕДА'] = resource['ЕДА'] + scales['ФЕРМА']*3
        resource['ДЕРЕВО'] = resource['ДЕРЕВО'] + scales['ЛЕСОПИЛКА']*3
        resource['ЖЕЛЕЗО'] = resource['ЖЕЛЕЗО'] + scales['ШАХТА']*3
        print('РЕСУРСЫ ПОЛУЧЕНЫ! ДЕНЬ ЗАКОНЧЕН!')
        enter = input()

start()
