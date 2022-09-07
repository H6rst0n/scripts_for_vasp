# import zone
from os import linesep
import sys
import math
import numpy as np

# distance between A(x1, y1, z1) and B(x2, y2, z2)
def distance(x1, y1, z1, x2, y2, z2):
    return ((float(x1)-float(x2))**2+(float(y1)-float(y2))**2+(float(z1)-float(z2))**2)**0.5

# The length of the vector
def lengthOfVector(vec_x, vec_y, vec_z):
    return (float(vec_x)**2+float(vec_y)**2+float(vec_z)**2)**0.5

# Convert cartesian coordiation to direc
def C2D(lattice_vector, coor_in_dire):
    coor_in_cartesian = np.float_(coor_in_dire).dot(np.linalg.inv(np.float_(lattice_vector)))
    return (coor_in_cartesian)
    
# vector in dire to cartesian
def lengthOfVector_dire(lattice_vector, vector_in_dire):
    vector_in_cartesian=np.float_(vector_in_dire.dot(np.float_(lattice_vector)))
    return (lengthOfVector(vector_in_cartesian[0],vector_in_cartesian[1],vector_in_cartesian[2]))

# Convert direc coordiation to cartesian
def D2C(coor_in_cartesian):
    line = coor_in_cartesian

    a1 = float(line[2][0])
    a2 = float(line[3][0])
    a3 = float(line[4][0])
    b1 = float(line[2][1])
    b2 = float(line[3][1])
    b3 = float(line[4][1])
    z1 = float(line[2][2])
    z2 = float(line[3][2])
    z3 = float(line[4][2])

    num_atoms = sum([int(x) for x in line[6]])

    def convert():
        x_cartesian = float(line[i][0])*a1 + float(line[i][1])*a2 + float(line[i][2])*a3
        y_cartesian = float(line[i][0])*b1 + float(line[i][1])*b2 + float(line[i][2])*b3
        z_cartesian = float(line[i][0])*z1 + float(line[i][1])*z2 + float(line[i][2])*z3
        return x_cartesian, y_cartesian, z_cartesian
            
    selectiondynamic=line[7][0]
    if selectiondynamic[0]=="S" or selectiondynamic[0]=="s":
        start_num=9
    else:
        start_num=8

    for i in range(start_num,start_num+num_atoms):
        x_cartesian, y_cartesian, z_cartesian = convert()
        line[i][0] = str(x_cartesian)
        line[i][1] = str(y_cartesian)
        line[i][2] = str(z_cartesian)

    return line
    
# Center of gravity of molecular
def massXposition(massOfAtom, atom_x, atom_y, atom_z):
    return (float(massOfAtom)*float(atom_x)), (float(massOfAtom)*float(atom_y)), (float(massOfAtom)*float(atom_z))

# atomic mass data
def massDataOfatom(atom):
    massData={"H":1.00794, "He":4.002602, "Li":6.941, "Be":9.0121831, "B":10.811, "C":12.0107, "N":14.0067, "O":15.9994, "F":18.998403163, "Ne":20.1797, "Na":22.98976928, "Mg":24.3050, "Al":26.9815385, "Si":28.0855, "P":30.973761998, "S":32.065, "Cl":35.453, "Ar":39.948, "K":39.0983, "Ca":40.078, "Sc":44.955908, "Ti":47.867, "V":50.9415, "Cr":51.9961, "Mn":54.938044, "Fe":55.845, "Co":58.933194, "Ni":58.6934, "Cu":63.546, "Zn":65.38, "Ga":69.723, "Ge":72.64, "As":74.921595, "Se":78.971, "Br":79.904, "Kr":83.798, "Rb":85.4678, "Sr":87.62, "Y":88.90584, "Zr":91.224, "Nb":92.90637, "Mo":95.95, "Tc":98.90, "Ru":101.07, "Rh":102.90550, "Pd":106.42, "Ag":107.8682, "Cd":112.414, "In":114.818, "Sn":118.710, "Sb":121.760, "Te":127.60, "I":126.90447, "Xe":131.293, "Cs":132.90545196, "Ba":137.327, "La":138.90547, "Ce":140.116, "Pr":140.90766, "Nd":144.242, "Pm":144.9, "Sm":150.36, "Eu":151.964, "Gd":157.25, "Tb":158.92535, "Dy":162.500, "Ho":164.93033, "Er":167.259, "Tm":168.93422, "Yb":173.054, "Lu":174.9668, "Hf":178.49, "Ta":180.94788, "W":183.84, "Re":186.207, "Os":190.23, "Ir":192.217, "Pt":195.084, "Au":196.966569, "Hg":200.59, "Tl":204.3833, "Pb":207.2, "Bi":208.98040, "Po":208.98, "At":209.98, "Rn":222.01, "Fr":223.01, "Ra":226.02, "Ac":227.02, "Th":232.0377, "Pa":231.03588, "U":238.02891, "Np":237.0482, "Pu":239.0642, "Am":243.0614, "Cm":247.0704, "Bk":247.0703, "Cf":251.0796, "Es":252.0830, "Fm":257.0591, "Md":258.0984, "No":259.1010, "Lr":262.1097, "Rf":267.1218, "Db":268.1257, "Sg":269.1286, "Bh":274.1436, "Hs":277.1519, "Mt":278, "Ds":281, "Rg":282, "Cn":285, "Nh":284, "Fl":289, "Mc":288, "Lv":292, "Ts":294, "Og":295}
    return massData[atom]
    
# Correction of atomic coordinates into the cell
def gointothebox(VECa, VECb, VECc, gamma ,x, y, z):
    VEC1=[float(VECa), float(0.0), float(0.0)]
    VEC2=[float(VECb)*math.cos(math.pi*float(gamma)/180), float(VECb)*math.sin(math.pi*float(gamma)/180), float(0.0)]
    VEC3=[float(0.0), float(0.0), float(VECc)]
    atomposition=[float(x), float(y), float(z)]

    # Correction of Z-coordinate
    while atomposition[2] < 0:
        atomposition[2]=round(atomposition[2]+VEC3[2], 6)
    while atomposition[2] > VEC3[2]:
        atomposition[2]=round(atomposition[2]-VEC3[2], 6)
    
    # Correction of xy-coordinate
    while atomposition[1] < 0:
        atomposition[0]=round(atomposition[0]+VEC2[0], 6)
        atomposition[1]=round(atomposition[1]+VEC2[1], 6)
    while atomposition[1] > VEC2[1]:
        atomposition[0]=round(atomposition[0]-VEC2[0], 6)
        atomposition[1]=round(atomposition[1]-VEC2[1], 6)
    while VEC2[0]/VEC2[1]*atomposition[1]-atomposition[0] > 0:
        atomposition[0]=round(atomposition[0]+VEC1[0], 6)
        atomposition[1]=round(atomposition[1]+VEC1[1], 6)
    while VEC2[0]/VEC2[1]*atomposition[1]-atomposition[0]+VEC1[0] < 0:
        atomposition[0]=round(atomposition[0]-VEC1[0], 6)
        atomposition[1]=round(atomposition[1]-VEC1[1], 6)

    return atomposition
