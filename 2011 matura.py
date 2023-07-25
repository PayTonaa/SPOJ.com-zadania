def zadanie1(zwierzęta):
    zwierzęta = zwierzęta.split(";")
    if zwierzęta[3] == "samica":
        return True
    else:
        return False
def zadanie4(zwierzęta):
    zwierzęta = zwierzęta.split(";")
    if "owczarek" in zwierzęta[1]:
        return zwierzęta[5]
os = []
pomoc = []
# # zadanie 1
#
# samice = 0
# samce = 0
# plik = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\psy.txt")
# tab = plik.read().splitlines()
# for zwierzęta in tab:
#     if zadanie1(zwierzęta) == True:
#         samice += 1
#     else:
#         samce += 1
# print(samice, samce)
#
# # zadanie 2

plik = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\osoby.txt")
tab = plik.read().splitlines()
os = []
pomoc = []
for osoby in tab:
    osoby = osoby.split((";"))
    os.append(osoby[0])
    os.append(0)
plik1 = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\psy.txt")
tab1 = plik1.read().splitlines()
for ilosc in tab1:
    ilosc = ilosc.split(";")
    ilosc = ilosc[5]
    for x in range(len(os)):
        if os[x] == ilosc:
            os[x+1] += 1

for x in range(1, len(os), 2):
    if os[x] > 8:
        pomoc.append(x)
    for y in range(len(os)):
        if os[x] == os[y]:
            print(os-1)
# zadanie3
#
# plik = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\osoby.txt")
# tab = plik.read().splitlines()
# os = []
# pomoc = []
# for osoby in tab:
#     osoby = osoby.split((";"))
#     os.append(osoby[0])
#     os.append(0)
# plik1 = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\psy.txt")
# tab1 = plik1.read().splitlines()
# for ilosc in tab1:
#     ilosc = ilosc.split(";")
#     ilosc = ilosc[4:]
#     ilosc[0] = int(ilosc[0])
#     for x in range(len(os)):
#         if ilosc[1] == os[x]:
#             os[x+1] += int(ilosc[0])
# for y in range(1, len(os), 2):
#     pomoc.append(os[y])
# for x in range(0, len(os)):
#     if os[x] == max(pomoc):
#         wynik = os[x-1]
#         wynik1 = os[x]
# for osoby in tab:
#     osoby = osoby.split((";"))
#     if osoby[0] == wynik:
#         print(osoby[1:3], wynik1)
#
# # zadanie4
# plik = open("Z:\\Arkusze maturalne\\2011\\Dane_PR\\psy.txt")
# tab = plik.read().splitlines()
# for zwierzęta in tab:
#     if zadanie4(zwierzęta) != None:
#         if zadanie4(zwierzęta) not in os:
#             os.append(zadanie4(zwierzęta))
# print(os)


