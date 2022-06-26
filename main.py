
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
        self.dados = {}        # Objetos de dados e valores
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

        self.analisarLog()

    def analisarLog(self):
        # Transações que commitaram vão para a listaRedo
        # Transações que não commitaram vão para a listaUndo
        transactions = set()
        transactions_commited = set()
        for h in self.Log.histories:
            tr = h[2]
            op = h[3]
            transactions.add(tr)
            if op == 'r' or op == 'w':
                obj = h[4]
                self.dados[obj] = ''
            elif op == 'c':
                transactions_commited.add(tr)

        self.listaRedo = list(transactions_commited)
        self.listaUndo = list(transactions - transactions_commited)



    def recover(self):

        # Referências
        log = self.Log.histories
        log_inv = log[::-1]
        listaRedo = self.listaRedo
        listaUndo = self.listaUndo
        dados = self.dados

        print("Lista Redo: ", listaRedo)
        print("Lista Undo: ", listaUndo)
        print()

        # Varredura backward
        for h in log_inv:
            tr = h[2]
            if tr in listaUndo:
                # UNDO
                op = h[3]
                if op == 'w':
                    obj = h[4]
                    beforeImg = h[5]
                    dados[obj] = beforeImg
        
        # Varredura forward
        for h in log:
            tr = h[2]
            if tr in listaRedo:
                # REDO
                op = h[3]
                if op == 'w':
                    obj = h[4]
                    afterImg = h[6]
                    dados[obj] = afterImg
                    
        

    def lastConsistentState(self):
        dados = self.dados

        # Printar último estado consistente dos dados
        for obj, value in dados.items():
            print(obj + ": " + value)


    def printLog(self):
        for op in self.Log.histories:
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
    recovery.printLog()
    print()

    recovery.recover()

    print("Último estado consistente dos dados")
    recovery.lastConsistentState()
    print()

main()

