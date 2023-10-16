import sys

def prumer() -> float:
    nummer = 0
    for i in range(1,len(sys.argv) - 1):
            nummer = sys.argv[i] + nummer
    return(nummer/len(sys.argv))

print(prumer)
