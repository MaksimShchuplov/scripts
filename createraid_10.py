_author__ = 'max'

from time import sleep
import os


enclosure_mass = {}
os.system("/usr/MegaCli/MegaCli64 -PDList -a0 > pdlist.txt")
file = open('pdlist.txt', "r")
f = 0
encnum = 0
for i in file:

    if "Enclosure Device ID" in i:
        encnum = int(i.split(":")[1])
        if encnum not in enclosure_mass:
            mass = []
            enclosure_mass[encnum] = mass
        f = 1

    if "Slot Number" in i and f == 1:
        pdnum = int(i.split(":")[1])
        pdlist = []
        pdlist = enclosure_mass[encnum]
        pdlist.append(pdnum)
        enclosure_mass[encnum] = pdlist

file.close()
print enclosure_mass

pdlist_mass = []
for enc in enclosure_mass:
    for pd in enclosure_mass[enc]:
        pdlist_mass.append(str(enc) + ":" + str(pd))

print pdlist_mass[0:16]
print pdlist_mass[16:32]
print len(pdlist_mass)

os.system("/usr/MegaCli/MegaCli64  -CfgSpanAdd -r10 -Array0" +
          str(pdlist_mass[0:16]) +
          " -Array1" +
          str(pdlist_mass[16:32]) +
          " -sz70000 -a0")
sleep(5)
os.system("/usr/MegaCli/MegaCli64  -CfgSpanAdd -r10 -Array0" +
          str(pdlist_mass[0:16]) + " -Array1" + str(pdlist_mass[16:32]) + "  -a0")
sleep(5)
os.system(
    "/usr/MegaCli/MegaCli64 -PDHSP -Set -PhysDrv[" + str(pdlist_mass[32]) + "] -a0")
