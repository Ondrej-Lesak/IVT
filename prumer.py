import sys

def prumer() -> float:
    nummero = 0
    for i in range(1,len(sys.argv) - 1):
            nummero = sys.argv[i] + nummero
    return(nummero/len(sys.argv))

print(prumer)
