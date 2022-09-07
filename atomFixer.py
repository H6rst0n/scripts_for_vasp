#!/usr/bin/env python3
# This scrip is for fixing atoms of POSCAR of VASP!!

import sys

fileName=sys.argv[1:]

with open(fileName[0], mode="r") as F:
    lines=[x.split() for x in F]
    atomsNumber=0
    for i in range(len(lines[6])):
        atomsNumber=atomsNumber+int(lines[6][i])
    print("\n# of atoms = "+str(atomsNumber)+"\n")
    
    
    selectiondynamic=lines[7][0]
    if selectiondynamic[0]!="S" and selectiondynamic[0]!="s":
        lines.insert(7,["Selectiondynamic"])

    
    if len(lines[9])==6:
        for i in range(9,atomsNumber+9):
            lines[i][3:6]=[]

    
    for i in range(9,atomsNumber+9):
        lines[i]=lines[i]+["T   T   T"]

    
    fixAtomRange=input("Atomic range to be fixed (1 64):").split()
    for i in range(int(fixAtomRange[0])+8,int(fixAtomRange[1])+9):
        lines[i][3]="F   F   F"


with open(str(fileName[0])+".fix",mode="w")as new:
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            new.write("%-9s     " % lines[i][j])
        new.write("\n")