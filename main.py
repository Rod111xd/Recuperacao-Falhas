
from msilib.schema import ReserveCost


INPUT_FILE = "in.txt"

# Ler entrada e retornar operações

class Log:
    def __init__(self):
        self.histories = []

class Recovery:
    def __init__(self, input_file=None):
        self.Log = Log()
        if input_file:
            self.loadInput(input_file)

    def loadInput(self, input_file):
        f = open(input_file, "r")
        lines = f.read().split("\n")

        f.close()

        histories = self.Log.histories

        try:
            for l in lines:
                l = l.replace(" ","")
                l = l.split("|")
                l = tuple(x for x in l)
                histories.append(l)
        except:
            print("Entrada inválida!")

def printHistories(histories):
    for i, op in enumerate(histories):
        t = len(op)
        out = "[ "
        for j, el in enumerate(op):
            out += el + " "
            if j+1 != t:
                out += "| "
        out += "]"
        print(out)

def main():

    recovery = Recovery(INPUT_FILE)

    if not recovery.Log.histories:
        return

    print("Entrada:")
    printHistories(recovery.Log.histories)



main()

