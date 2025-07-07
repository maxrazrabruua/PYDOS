print("Создание памяти...")
import ram
mem = ram.Ram(1024)
print("Импорт библиотеки")
import time
import bit2
import os
import binner as ard
print("Создание функциий...")
def h():
    print("Помощь:")
    print("h. Помощь")
    print("0. Выйти")
    print(f"1. Скопировать значение из памяти(64-{l - 1})")
    print("2. Вывести значение из памяти которое скопированное")
    print("3. Записать байт в байт копированния")
    print("4. Записать байт в ОЗУ")
    print("5. Очистка ОЗУ(кроме 0-63)")
    print("6. Запись начала:конца в память")
    print("7. Проверка значений в начале:конце")
    print("8. Чекинг всей памяти(и список[числа] и биннарной строкой)")
    print("9. Записать дамп памяти на диск")
    print("10. Загрузить дамп памяти с диска")
    print("11. Вывод байтов в заданном начале:конце")
    print("12. Вывод текста в кодировке ARD")
    print("13. Прописать в заданный начало:конец строку в кодировке ARD")
    print("14. Создать вирт. диск с файловой системой TFS")
    print("15. Посмотр всех вирт. дисков в формате 'N. D'")
    print("16. Выбрать виртуальный диск")
    print("17. Проверить выделяемый виртуальный диск")
    print("18. Создать новый файл\Редактировать старый в виртуальном диске и его соддержимое в начале:конце")
    print("19. Просмотр соддержимого в виртуальном диске")
    print("20. Читать файл с виртуального диска отправляя его данные в указанный начало:конец")
    print("21. Удалить файл с виртуального диска")
    print("22. Напрямую прочитать диск как текст в кодировке ARD")
print("Подсчёт памяти...")
l = 0
s = time.time()
while True:
    try:
        if l % 64 == 0: print(str(l)  + '\r', end='')
        mem[l]
        l += 1
    except:
        print('\r' + str(l) + ' байт')
        break
print("Подсчёт закончен")
print("Он занял:", time.time() - s, 'секунд')
print("Запуск...")

h()
while True:
    try:
        i = input(">>> ")
        if i == "h":
            h()
        elif i == "0":
            break
        elif i == "1":
            byte = int(input("Выбор байта: "))
            if byte <= 63:
                print("Вы залезли в системные байты")
            elif byte > l - 1:
                print("Вы заграницей")
            else:
                mem[0] = mem[byte]
                print("Байт скопирован")
        elif i == "2":
            print(f"Вывод скопированного байта: {mem[0]}")
        elif i == "3":
            byte = int(input("Запись байта: "))
            if byte > 255:
                print("Данный байт не входит в диапозон байтов 0-255")
            else:
                mem[0] = byte
                print("Байт успешно вставлен в байт копирования")
        elif i == "4":
            byte = int(input("Выбор байта: "))
            if byte <= 63:
                print("Вы залезли в системные байты")
            elif byte > l - 1:
                print("Вы заграницей")
            else:
                mem[byte] = mem[0]
                print("Байт записан")
        elif i == "5":
            print("Настройка...")
            j = 64
            s = time.time()
            while True:
                try:
                    if j % 64 == 0: print(str(j) + "\r", end='')
                    mem[j] = 0
                    j += 1
                except IndexError:
                    print(str(j) + " байт" + "\r", end='')
                    print("\nЗакончено, память очищена")
                    break
            print("Прошло:", time.time() - s, "секунд")
        elif i == "6":
            print("[WARN]: Система 16-битная, количество памяти смотрите в самом верху")
            o = input("Формат число(16-бит):число(16-бит)>> ")
            try:
                b = o.split(":")
                c = int(b[0])
                d = int(b[1])
                if ((c > 1024 * 64) or (c > l - 1) or (c < 64)) or ((d > 1024 * 64) or (d > l - 1) or (d < c)):
                    print("Неверные значения!")
                else:
                    bc = list(bit2.intToBytes2(c))
                    bd = list(bit2.intToBytes2(d))
                    mem[1], mem[2] = bc[0], bc[1]
                    mem[3], mem[4] = bd[0], bd[1]
                    print("Значения успешно вставлены в память чтобы их проверить напишите 7")
            except:
                print("Это не целые числа")
        elif i == "7":
            bc = [mem[1]] + [mem[2]]
            bd = [mem[3]] + [mem[4]]
            c = bit2.bytes2toint(bytes(bc))
            d = bit2.bytes2toint(bytes(bd))
            print(f"Значения в памяти: {c}:{d}")
        elif i == "8":
            print("Настройка...")
            j = 0
            s = time.time()
            a = []
            while True:
                try:
                    if j % 64 == 0: print(str(j) + "\r", end='')
                    a.append(mem[j])
                    j += 1
                except IndexError:
                    print(str(j) + " байт" + "\r", end='')
                    print("\nЗакончено, память проверена")
                    break
            print("Прошло:", time.time() - s, "секунд")
            print("Выводы:")
            print("Список[числа]:", a)
            print("Бинарная строка:", repr(bytes(a)))
        elif i == "9":
            try:
                o = input("Имя дампа памяти: ")
                print("Настройка...")
                j = 0
                s = time.time()
                a = []
                while True:
                    try:
                        if j % 64 == 0: print(str(j) + "\r", end='')
                        a.append(mem[j])
                        j += 1
                    except IndexError:
                        print(str(j) + " байт" + "\r", end='')
                        print("\nЗакончено, память очищена")
                        break
                print("Прошло:", time.time() - s, "секунд")
                with open('dumps/' + o + '.dms', 'wb') as file:
                    file.write(bytes(a))
                print("Дамп был успешно записан на диск")
            except:
                print("Что-то не так, может неверное имя файла?")
        elif i == "10":
            try:
                o = input("Имя дампа памяти: ")
                print("Проверка валидности...")
                if os.path.getsize('dumps/' + o + '.dms') != l:
                    print("Файл слишком большой или маленький")
                else:
                    print("Начинаю загрузку...")
                    print("Чтение файла...")
                    with open('dumps/' + o + '.dms', 'rb') as file:
                        content = file.read()
                    a = list(content)
                    s = time.time()
                    for k, v in zip(range(len(a)), a):
                        if (k % 64 == 0) or len(a) - 1 == k: print(f'Загрузка байта {k}: {v}\r', end='')
                        mem[k] = v
                    print(f"\nДанные загружены за {time.time() - s} секунд!")
                    print('Загрузка завершена!')
            except:
                print("Что-то не так, может неверное имя файла?")
        elif i == "11":
            print("Настройка...")
            j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
            k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
            a = []
            while j <= k:
                try:
                    a.append(mem[j])
                    j += 1
                except IndexError:
                    break
            print('Список[числа]:', a)
            print('Бинарная строка:', repr(bytes(a)))
        elif i == "12":
            j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
            k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
            a = []
            while j <= k:
                try:
                    a.append(mem[j])
                    j += 1
                except IndexError:
                    break
            print(''.join([ard.localChr(x) for x in a]))
        elif i == "13":
            j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
            k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
            text = input("Текст: ")
            if k - j == 0:
                if len(text) == 1:
                    mem[j] = list(ard.Ard(text).encode())[0]
                    print("Сохранено 1 байт")
                else:
                    print("Некорректная длина")
            else:
                if len(text) == k - j + 1:
                    print("Сохраняю в ОЗУ...")
                    s = time.time()
                    a = list(ard.Ard(text).encode())
                    for key, v in zip(range(len(a)), a):
                        print(f'Сохранение байта {key + j}: {v}', end='\r')
                        mem[key + j] = v
                    print(f"\nДанные сохранены в ОЗУ за {time.time() - s} секунд!")
                    print('Сохранение завершено!')
                    print(f'Сохранено {len(a)} байт(-ов)')
                else:
                    print("Некорректная длина")
        elif i == "14":
            nametfs = input('Название виртуального диска: ')
            print('Создаю...')
            with open('tfss/' + nametfs + '.tfs', 'wb') as file:
                file.write(b'')
            print('Виртуальный диск создан!')
            print(f'Номер виртуального диска: {os.listdir('tfss/').index(nametfs + '.tfs')}')
        elif i == "15":
            print("Поиск виртуальных дисков...")
            vds = os.listdir('tfss/')
            print("Формирую таблицу...")
            for k, v in zip(range(len(vds)), vds):
                print(f'{k}. {v[:-4]}')
            if len(vds) == 0:
                print("    Виртуальных дисков нет    ")
        elif i == "16":
            try:
                ndisk = int(input("Номер диска(16-бит): "))
                print("Провека количество виртуальных дисков...")
                if len(os.listdir('tfss/')) - 1 >= ndisk:
                    if ndisk > 65535:
                        print("Слишком большое число, которое не является недоступным для 16-битной системы запоминания чисел")
                    else:
                        n = list(bit2.intToBytes2(ndisk))
                        mem[5], mem[6] = n[0], n[1]
                        print("Сохранено, чтобы проверить номер виртуального диска который вы выделели напишите 17")
                else:
                    print("Данный виртуальный диск не входит в должный спектор количество дисков,\nпроверьте количество виртуальных дисков написавши 15")
            except ValueError:
                print("Ошибка ввода, походу число не является числом!")
        elif i == "17":
            af = [mem[5]] + [mem[6]]
            ab = bit2.bytes2toint(af)
            print(f"Выбран номер: {ab}")
            try:
                print(f"Этот диск: {os.listdir('tfss/')[ab][:-4]}")
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        elif i == "18":
            print("Пробую получить доступ к диску...")
            try:
                af = [mem[5]] + [mem[6]]
                ab = bit2.bytes2toint(af)
                d = os.listdir('tfss/')[ab]
                print(f"Выбран диск: {d[:-4]}")
                d = 'tfss/' + d
                nf = input("Имя файла(Кодировка ARD)(Выход - 0): ")
                if nf != "0":
                    print("Получаю начало:конец...")
                    j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
                    k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
                    bs = []
                    for x in range(k - j + 1):
                        print(f"{j + x} байт", end='\r')
                        bs.append(mem[j + x])
                    print("Загрузка виртуального диска для записи")
                    with open(d, 'rb') as file:
                        content = file.read()
                    print("Парсинг виртуального диска...")
                    bbs = content.split(bytes([221]))
                    sl = {}
                    for kv in bbs:
                        a = kv.split(bytes([222]))
                        if len(a) < 2:
                            continue
                        k, v = a[0], a[1]
                        sl[k] = v
                    print("Парсинг завершён\nНачинается запись файла...")
                    sl[ard.Ard(nf).encode()] = bs
                    print("Запись файла завершена\nНачалась запись виртуального диска(серилизация и запись)")
                    print("Серилизация")
                    kvs = []
                    for k, v in sl.items():
                        kvs.append(bytes([222]).join([k, bytes(v)]))
                    text = bytes([221]).join(kvs)
                    print("Запись")
                    with open(d, 'wb') as file:
                        file.write(text)
                    print("Завершено успешно")
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        elif i == "19":
            print("Пробую получить доступ к диску...")
            try:
                af = [mem[5]] + [mem[6]]
                ab = bit2.bytes2toint(af)
                d = os.listdir('tfss/')[ab]
                print(f"Выбран диск: {d[:-4]}")
                d = 'tfss/' + d
                print("Загрузка виртуального диска(загрузка и парсинг)")
                print("Загрузка...")
                with open(d, 'rb') as file:
                    content = file.read()
                print("Парсинг...")
                bbs = content.split(bytes([221]))
                sl = {}
                for kv in bbs:
                    a = kv.split(bytes([222]))
                    if len(a) < 2:
                        continue
                    k, v = a[0], a[1]
                    sl[k] = v
                print("Формирую таблицу...")
                for k, v in sl.items():
                    print(f'{''.join([ard.localChr(x) for x in list(k)])} ║ {len(v)} байт')
                if len(sl.keys()) == 0:
                    print("Виртуальный диск пуст")
                print(f"Файлов: {len(sl.keys())}")
                print(f"Вес их даннных в байтах: {len(bytes().join([x for x in sl.values()]))}")
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        elif i == "20":
            print("Пробую получить доступ к диску...")
            try:
                af = [mem[5]] + [mem[6]]
                ab = bit2.bytes2toint(af)
                d = os.listdir('tfss/')[ab]
                print(f"Выбран диск: {d[:-4]}")
                d = 'tfss/' + d
                nf = input("Имя файла(Кодировка ARD)(Выход - 0): ")
                if nf != "0":
                    print("Загрузка виртуального диска для чтения")
                    with open(d, 'rb') as file:
                        content = file.read()
                    print("Парсинг виртуального диска...")
                    bbs = content.split(bytes([221]))
                    sl = {}
                    for kv in bbs:
                        a = kv.split(bytes([222]))
                        if len(a) < 2:
                            continue
                        k, v = a[0], a[1]
                        sl[k] = v
                    print("Парсинг завершён\nНачинается чтение файла...")
                    if ard.Ard(nf).encode() in sl.keys():
                        text = sl[ard.Ard(nf).encode()]
                        print("Получаю начало:конец...")
                        j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
                        k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
                        if k - j + 1 == len(text):
                            for x, t in zip(range(k - j + 1), text):
                                print(f"{j + x} байт", end='\r')
                                mem[j + x] = t
                            print("Файл был успешно загружен в ОЗУ")
                        else:
                            print("Слишком большой или маленький файл для такого выделения")
                    else:
                        print("Файл отсуствует в виртуальном диске")
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        elif i == "21":
            print("Пробую получить доступ к диску...")
            try:
                af = [mem[5]] + [mem[6]]
                ab = bit2.bytes2toint(af)
                d = os.listdir('tfss/')[ab]
                print(f"Выбран диск: {d[:-4]}")
                d = 'tfss/' + d
                nf = input("Имя файла(Кодировка ARD)(Выход - 0): ")
                if nf != "0":
                    print("Получаю начало:конец...")
                    j = bit2.bytes2toint(bytes([mem[1]] + [mem[2]]))
                    k = bit2.bytes2toint(bytes([mem[3]] + [mem[4]]))
                    bs = []
                    for x in range(k - j + 1):
                        print(f"{j + x} байт", end='\r')
                        bs.append(mem[j + x])
                    print("Загрузка виртуального диска для записи")
                    with open(d, 'rb') as file:
                        content = file.read()
                    print("Парсинг виртуального диска...")
                    bbs = content.split(bytes([221]))
                    sl = {}
                    for kv in bbs:
                        a = kv.split(bytes([222]))
                        if len(a) < 2:
                            continue
                        k, v = a[0], a[1]
                        sl[k] = v
                    print("Парсинг завершён\nНачинается удаление файла...")
                    try:
                        del sl[ard.Ard(nf).encode()]
                        print("Удаление файла завершено\nНачалась запись виртуального диска(серилизация и запись)")
                        print("Серилизация")
                        kvs = []
                        for k, v in sl.items():
                            kvs.append(bytes([222]).join([k, bytes(v)]))
                        text = bytes([221]).join(kvs)
                        print("Запись")
                        with open(d, 'wb') as file:
                            file.write(text)
                        print("Завершено успешно")
                    except KeyError:
                        print("Файла не существует")
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        elif i == "22":
            print("Пробую получить доступ к диску...")
            try:
                af = [mem[5]] + [mem[6]]
                ab = bit2.bytes2toint(af)
                d = os.listdir('tfss/')[ab]
                print(f"Выбран диск: {d[:-4]}")
                d = 'tfss/' + d
                print('Чтение виртуального диска...')
                with open(d, 'rb') as file:
                    print(repr(''.join([ard.localChr(x) for x in file.read()])))
            except IndexError:
                print("Этот диск недоступный, выберите другой диск")
        else:
            print("Неверный ввод")
    except Exception as e:
        print(f"Произошла ошибка:\n{e.__class__.__name__}: {str(e)}")