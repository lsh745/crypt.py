import sys
def numerizer(inp):
    result = []
    for i in inp.upper():
        if i >= 'A' and i <= 'Z':
            result.append(ord(i) - 65)
    return result

def finder(inp, target, pm):
    inp = numerizer(inp)
    target = numerizer(target)

    result = ""
    for i in range(len(inp)):
        result += chr(abs(eval("(%s %s %s) %% 26 + 65" % (inp[i], pm, target[i]))))

    return result

def caesar(inp):
    mlist = []
    for o in range(26):
        result = "%2d : " % o
        for i in inp:
            if i >= 'A' and i <= 'Z':
                result += chr((ord(i) - 65 + o) % 26 + 65)

            elif i >= 'a' and i <= 'z':
                result += chr((ord(i) - 97 + o) % 26 + 97)

            else:
                result += i
                
        mlist.append(result)

    return mlist

def vigenere(inp, key, pm):
    key = numerizer(key)
    lu = 0
    i, delay = 0, 0
    result = ""

    while i < len(inp):
        tmp = inp[i]
        if tmp >= "A" and tmp <= "Z":
            lu = 65
        elif tmp >= "a" and tmp <= "z":
            lu = 97
        else:
            result += tmp
            delay += 1
            i += 1
            continue

        result += chr(int(eval("(%s %s %s) %% 26 + %s" % ((ord(tmp) - lu), pm, key[(i - delay) % len(key)], lu))))
        i += 1

    return result

def matcher(inp, key, pm, target):
    lkey = len(key)
    visit, tmp = "", ""
    answer = []

    for i in key:
        if i not in visit:
            visit += i

        else:
            tmp += i

            if visit == tmp:
                key = visit * 2

    lv = len(visit)
    for i in range(lv):
        result = vigenere(inp, key[i : i + lv], pm)
        if target in result:
            print("KEY :", key[i : i + lv])
            answer.append(result)

    return answer

if __name__ == "__main__":
    sargv = sys.argv
    pm = "-"
    try:
        for i in range(1, len(sargv)):
            if sargv[i][0] == "-" and sargv[i] != "-":
                if sargv[i] == "-c":
                    cipher = sargv[i + 1]
                    # print("CIPHER :", CIPHER)
                elif sargv[i] == "-k":
                    key = sargv[i + 1]
                    # print("KEY :", key)
                elif sargv[i] == "-g": 
                    guess = sargv[i + 1]
                    # print("GUESS :", guess)
                elif sargv[i] == "-t":
                    target = sargv[i + 1]
                    # print("TARGET :", target)
                elif sargv[i] == "-pm":
                    pm = sargv[i + 1]
                    # print("PLUS/MINUS :", pm)

                else:
                    raise ValueError(sargv[i])

    except ValueError as e:
        print("WRONG INPUT :", e)

    try:
        if ("-c" and "-k") in sargv:
            print(vigenere(cipher, key, pm))

        elif ("-c" and "-t" and "-g") in sargv:
            key = finder(guess, target, pm)
            for i, v in enumerate(matcher(cipher, key, pm, target)):
                print("%02d : %s" % (i, v))

        elif "-c" in sargv:
            for i in caesar(cipher):
                print(i)

        else:
            raise ValueError(sargv)

    except ValueError as e:
        print("NO MATCHING SET :", e)


# ex)
 # -c "Rijvsmysmysmy Itovwyrc! Ns wyy ixsu Glm kq G? wc lkqc sw qwsmdlkkr sr...M ixsu fipi acvp urer iss geld! Md iss mel niastfov rrmq mvwzxmqvyw, cme gyx kcd xfo gmbvcmx yxwuov. qy, jjkk gc LymoADJ{t_tzwi_3vxbd0p3_vff.afy'q_wzoxpq_dp_qfz}" -g "LymoADJ" -t "HackCTF"