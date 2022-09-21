import music21

txt = input("Words Here: ")
streams = music21.stream.Stream()
lists = []

def duodecimal(n, q):
    rebs = ''

    while n > 0:
        n, mod = divmod(n, q)
        rebs += str(mod)

    return rebs[::-1]

def Convertt(list):
    extraclist = ""
    for k in list:
        extraclist += k + ""
    return extraclist.strip()

for i in txt:
    re = hex(ord(i))
    deci = int(re, 16)
    duo = duodecimal(int(re, 16), 12)
    final = duo.replace("01", "A").replace("11", "B")
    lists.append(final)

extraclist = Convertt(lists)

list = list(extraclist)

for j in list:
    transer = j.replace("0", "C").replace("1", "C#").replace("2", "D").replace("3", "D#").replace("4", "E").replace(
        "5", "F").replace("6", "F#").replace("7", "G").replace("8", "G#").replace("9", "F").replace("A", "F#").replace(
        "B", "B")
    inte = transer + "4"
    print(inte)
    note = music21.note.Note(inte)
    streams.append(note)

streams.show('midi')