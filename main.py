def citire_lista():
    '''
    citeste lista
    '''
    lst = []
    n = int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("lst[" + str(i) + "]=")))
    return lst

def nrnegative(lst):
    '''
    afiseaza numerele negative din lista
    '''
    for i in range(len(lst)):
        if lst[i] < 0:
            print(lst[i])
def celmaimicnumarcitit(lst):
    '''
    afiseaza cel mai mic numar care are ultima cifra egala cu cifra citita
    '''
    x = int(input("Dati o cifra"))
    minx = 10000
    for i in range(len(lst)):
        if lst[i]%10 == x and lst[i] < minx:
            minx = lst[i]
    print(minx)
def nrprim(x):
    '''
    determina daca numarul este prim
    '''
    if x<2:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True
def superprim(lst):
    '''
    afiseaza numerele superprime
    '''
    for i in range(len(lst)):
        n = lst[i]
        while nrprim(n) == True and n != 0:
            n = n // 10
        if n == 0:
            print(lst[i])


def main():
    while True:
        print("1.Citire date")
        print("2.Afisarea numerelor negative din lista")
        print("3.Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura")
        print("4.Afisarea tuturor numerelor din lista care sunt superprime")
        print("Pentru a inchide, introduce x")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            nrnegative(l)
        elif optiune == "3":
            celmaimicnumarcitit(l)
        elif optiune == "4":
            superprim(l)
        elif optiune == "x":
            break


if __name__ == '__main__':
    main()