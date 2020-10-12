import keyboard,sys,configparser



ignorekeys = ["shift","control","alt","tab","right","left","up","down","ctrl"]
macroses = [":img",":LI",":import"]
values = ["<img>","Lorem Ipsum und so weiter\nund sofort...........","\\importpackage{}[]"]
keyspressed = []

def Type(word):
    for letter in word:
        keyboard.press_and_release(letter)


def ToString(list):
    ret = ""
    for letter in list:
        ret += letter
    return ret


def ClearString(string,rest):
    pass


def on_press_reaction(event):
    if event.name != "backspace":
        if event.name == "space":
            keyspressed.append(" ")
        else:
            keyspressed.append(event.name)
        for key in keyspressed:
            if key in ignorekeys:
                keyspressed.pop()
    else:
        try:
            keyspressed.pop()
        except Exception as e:
            pass
    if len(keyspressed) > 100:
        keyspressed.clear()
    kp = ToString(keyspressed)
    for macros in macroses:
        if macros in kp:
            mc = values[macroses.index(macros)]
            for b in range(len(macros)):
                keyboard.press_and_release("backspace")
            Type(mc)
            keyspressed.clear()
keyboard.on_press(on_press_reaction)

while True:
    pass
