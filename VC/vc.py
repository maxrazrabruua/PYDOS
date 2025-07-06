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
                if ((c > 1024 * 64) or (c > l - 1) or (c < 64)) or ((d > 1024 * 64) or (d > l - 1) or (d <= c)):
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
                    print("\nЗакончено, память очищена")
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
                        print(f'Сохранение байта {key + j}: {v}\r', end='')
                        mem[key + j] = v
                    print(f"\nДанные сохранены в ОЗУ за {time.time() - s} секунд!")
                    print('Сохранение завершено!')
                    print(f'Сохранено {len(a)} байт(-ов)')
                else:
                    print("Некорректная длина")
        else:
            print("Неверный ввод")
    except:
        print("Произошла ошибка")