
def citire_lista():
    lst = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst

def nrnegative(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            print(" ", lst[i])


def main():
    while True:
        print("1.Citire date")
        print("2.Afisarea numerelor negative din lista")
        print("Pentru a inchide, introduce x")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            nrnegative(l)
        elif optiune == "x":
            break


if __name__ == '__main__':

    main()