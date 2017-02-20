# _*_ coding: utf-8 -*-

meni = {}

while True:
    jed = raw_input("Vpišite jed: ")
    cena = raw_input("Vpišite ceno: ")
    meni[jed] = cena
    nadaljevanje = raw_input("Ali želite dodati še kakšno jed da/ne?")

    if nadaljevanje == "ne":
        break

print(meni)

with open("meni.txt", "w+") as meni_file:
    for jed in meni:
        meni_file.write("%s, %s EUR\n" % (jed, meni[jed]))
