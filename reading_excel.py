# import pandas as pd
#
# x = pd.read_excel("Book1.xlsx", index_col=0)
# # y = pd.read_excel("Bookl.xlsx", index_col=0, header=0)
# # y = pd.read_excel("Book1.xlsx", index_col=0, usecols=())
# df = pd.DataFrame(x, index=0)
# print(df.iloc[0])
#
# # print(x)
# # print(y)
# # print(y)

import pandas as pd

df = pd.read_excel('Book1.xlsx')
# print(df['Symbol'])
# print(df[['Elements', 'Atomic Number']]
print('Type 1 for search by Atomic Number, 2 for Name and 3 for Symbol \n 1 = Atomic Number \n 2 = Name\n 3 = Symbol '
      '\n 4 = Entire Table')
selection = int(input())


def an():
    print("Type Atomic Number")
    sl1 = int(input())
    if sl1 == 1:
        print(df.iloc[0])
    elif sl1 == 2:
        print(df.iloc[1])
    elif sl1 == 3:
        print(df.iloc[2])
    elif sl1 == 4:
        print(df.iloc[3])
    elif sl1 == 5:
        print(df.iloc[4])
    elif sl1 == 6:
        print(df.iloc[5])
    elif sl1 == 7:
        print(df.iloc[6])
    elif sl1 == 8:
        print(df.iloc[7])
    elif sl1 == 9:
        print(df.iloc[8])
    elif sl1 == 10:
        print(df.iloc[9])
    elif sl1 == 11:
        print(df.iloc[10])
    elif sl1 == 12:
        print(df.iloc[11])
    elif sl1 == 13:
        print(df.iloc[12])
    elif sl1 == 14:
        print(df.iloc[13])
    elif sl1 == 15:
        print(df.iloc[14])
    elif sl1 == 16:
        print(df.iloc[15])
    elif sl1 == 17:
        print(df.iloc[16])
    elif sl1 == 18:
        print(df.iloc[17])
    elif sl1 == 19:
        print(df.iloc[18])
    elif sl1 == 20:
        print(df.iloc[19])
    elif sl1 == 21:
        print(df.iloc[20])
    elif sl1 == 22:
        print(df.iloc[21])
    elif sl1 == 23:
        print(df.iloc[22])
    elif sl1 == 24:
        print(df.iloc[23])
    elif sl1 == 25:
        print(df.iloc[24])
    elif sl1 == 26:
        print(df.iloc[25])
    elif sl1 == 27:
        print(df.iloc[26])
    elif sl1 == 28:
        print(df.iloc[27])
    elif sl1 == 29:
        print(df.iloc[28])
    elif sl1 == 30:
        print(df.iloc[29])


def symbol():
    print("Enter the symbol of that element")
    sym1 = str(input())
    sl2 = sym1.capitalize()
    if sl2 == "H":
        print(df.iloc[0])
    elif sl2 == "He":
        print(df.iloc[1])
    elif sl2 == "Li":
        print(df.iloc[2])
    elif sl2 == "Be":
        print(df.iloc[3])
    elif sl2 == "B":
        print(df.iloc[4])
    elif sl2 == "C":
        print(df.iloc[5])
    elif sl2 == "N":
        print(df.iloc[6])
    elif sl2 == "O":
        print(df.iloc[7])
    elif sl2 == "F":
        print(df.iloc[8])
    elif sl2 == "Ne":
        print(df.iloc[9])
    elif sl2 == "Na":
        print(df.iloc[10])
    elif sl2 == "Mg":
        print(df.iloc[11])
    elif sl2 == "Al":
        print(df.iloc[12])
    elif sl2 == "Si":
        print(df.iloc[13])
    elif sl2 == "P":
        print(df.iloc[14])
    elif sl2 == "S":
        print(df.iloc[15])
    elif sl2 == "Cl":
        print(df.iloc[16])
    elif sl2 == "Ar":
        print(df.iloc[17])
    elif sl2 == "K":
        print(df.iloc[18])
    elif sl2 == "Ca":
        print(df.iloc[19])
    elif sl2 == "Sc":
        print(df.iloc[20])
    elif sl2 == "Ti":
        print(df.iloc[21])
    elif sl2 == "V":
        print(df.iloc[22])
    elif sl2 == "Cr":
        print(df.iloc[23])
    elif sl2 == "Mn":
        print(df.iloc[24])
    elif sl2 == "Fe":
        print(df.iloc[25])
    elif sl2 == "Co":
        print(df.iloc[26])
    elif sl2 == "Ni":
        print(df.iloc[27])
    elif sl2 == "Cu":
        print(df.iloc[28])
    elif sl2 == "Zn":
        print(df.iloc[29])


def name():
    print("Type the name of that element")
    sl = str(input())
    sl2 = sl.capitalize()
    if sl2 == "Hydrogen":
        print(df.iloc[0])
    elif sl2 == "Helium":
        print(df.iloc[1])
    elif sl2 == "Lithium":
        print(df.iloc[2])
    elif sl2 == "Beryllium":
        print(df.iloc[3])
    elif sl2 == "Boron":
        print(df.iloc[4])
    elif sl2 == "Carbon":
        print(df.iloc[5])
    elif sl2 == "Nitrogen":
        print(df.iloc[6])
    elif sl2 == "Oxygen":
        print(df.iloc[7])
    elif sl2 == "Fluorine":
        print(df.iloc[8])
    elif sl2 == "Neon":
        print(df.iloc[9])
    elif sl2 == "Sodium":
        print(df.iloc[10])
    elif sl2 == "Magnesium":
        print(df.iloc[11])
    elif sl2 == "Aluminium":
        print(df.iloc[12])
    elif sl2 == "Silicon":
        print(df.iloc[13])
    elif sl2 == "Phosphorus":
        print(df.iloc[14])
    elif sl2 == "Sulfur":
        print(df.iloc[15])
    elif sl2 == "Chlorine":
        print(df.iloc[16])
    elif sl2 == "Argon":
        print(df.iloc[17])
    elif sl2 == "Potassium":
        print(df.iloc[18])
    elif sl2 == "Calcium":
        print(df.iloc[19])
    elif sl2 == "Scandium":
        print(df.iloc[20])
    elif sl2 == "Titanium":
        print(df.iloc[21])
    elif sl2 == "Vanadium":
        print(df.iloc[22])
    elif sl2 == "Chromium":
        print(df.iloc[23])
    elif sl2 == "Manganese":
        print(df.iloc[24])
    elif sl2 == "Iron":
        print(df.iloc[25])
    elif sl2 == "Cobalt":
        print(df.iloc[26])
    elif sl2 == "Nickel":
        print(df.iloc[27])
    elif sl2 == "Copper":
        print(df.iloc[28])
    elif sl2 == "Zinc":
        print(df.iloc[29])


if selection == 1:
    an()
    print("Thanks for using our software")
elif selection == 2:
    name()
    print("Thanks for using our software")
elif selection == 3:
    symbol()
    print("Thanks for using our software")
elif selection == 4:
    print(df)
    print("Thanks for using our software")
