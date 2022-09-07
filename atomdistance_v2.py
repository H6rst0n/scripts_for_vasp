#!/usr/bin/env python3
import sys
import numpy as np
import modules.mathBetweenAtoms as mathbetweenatoms

#read file
file_name=sys.argv[1:]
with open(file_name[0],"r") as f:
    file=[x.split() for x in f]

# Get lattice vector
lattice_vector=float(file[1][0])*np.array(np.float_([file[2],file[3],file[4]]))

# Selectoiondynamic or not
selection=file[7][0]
if selection[0]=="S" or selection[0]=="s":
    coor=file[8][0]
    start_num=9
else:
    coor=file[7][0]
    start_num=8

# Print the number of atoms
atoms_num=sum([int(x) for x in file[6]])        
atom2num={}
print("\nThe system have "+str(atoms_num)+' atoms.')
for i in range(len(file[5])):
    atom2num[str(file[5][i])]=int(file[6][i])
print(atom2num)

# Select the atoms wanna measure
atom=input("\nWhitch atom you wanna see ? (e.x. C 1 C 2) :\n").split()
while atom[0] not in file[5] and atom[2] not in file[5]:
    print("\nError!!\n")
    atom=input("\nWhitch atom you wanna see ? (e.x. c 1 C 2) :\n").split()

column=0
row=0
while atom[0] != file[5][column]:
    row+=int(file[6][column])
    column+=1
else:
    row+=int(atom[1])
numberofatom1 = start_num + row - 1

column=0
row=0
while atom[2] != file[5][column]:
    row+=int(file[6][column])
    column+=1
else:
    row+=int(atom[3])
numberofatom2 = start_num + row - 1

atom1=file[numberofatom1][0:3]
atom2=file[numberofatom2][0:3]

# Make sure coor in dire
if coor[0]=="C" or coor[0]=="c":
    atom1=mathbetweenatoms.C2D(lattice_vector,atom1)
    atom2=mathbetweenatoms.C2D(lattice_vector,atom2)

# Get vector between atoms
vector=np.float_(atom1)-np.float_(atom2)

# Periodic judgment
for j in range (0,3):
    if vector[j] > 0.5:
        vector[j]-=1
    elif vector[j] < -0.5:
        vector[j]+=1

# Get the distance
diste=mathbetweenatoms.lengthOfVector_dire(lattice_vector,vector)

# Print the distance
print("Distance between "+atom[0]+atom[1]+" and "+atom[2]+atom[3]+" = "+str('%f'%diste)+" A.")