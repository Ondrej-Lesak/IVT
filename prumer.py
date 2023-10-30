import sys

def prumer() -> float:
    cislo = 0
    for i in range(1,len(sys.argv) - 1):
            cislo = sys.argv[i] + cislo
    return(cislo/len(sys.argv))

print(prumer)
