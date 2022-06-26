
INPUT_FILE = "in.txt"

# Ler entrada e retornar operações

class Log:
    def __init__(self):
        self.histories = []

class Recovery:
    def __init__(self, input_file=None):
        self.Log = Log()
        self.listaRedo = []    # Ids de transações commited
        self.listaUndo = []    # Ids de transações ativas
        if input_file:
            self.loadInput(input_file)
        self.analisarLog()

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

    def analisarLog(self):
        # Transações que commitaram vão para a listaRedo
        # Transações que não commitaram vão para a listaUndo
        transactions = set()
        transactions_commited = set()
        for h in self.Log.histories:
            tr = h[2]
            op = h[3]
            transactions.add(tr)
            if op == 'c':
                transactions_commited.add(tr)
        self.listaRedo = list(transactions_commited)
        self.listaUndo = list(transactions - transactions_commited)



    def recover(self):

        log = self.Log.histories
        log_inv = log[::-1]
        



def printHistories(histories):
    for op in histories:
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

    recovery.recover()

main()

