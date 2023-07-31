import timeit
from collections import deque

EstadoInicial = [[5,4, 3, 2, 1], [], []]
EstadoFinal = [[], [], [5,4, 3, 2, 1]]
NoFinal = None
NoExpandido = 0
profundidade = 0
MaxFrontier = 0


class Torre:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

    def __str__(self):
        return str(self.map)

def subNodes(node):
    global NoExpandido
    NoExpandido = NoExpandido + 1

    child = []
    child.append(Torre(move(node.state, 0, 1), node, 1, node.depth + 1, node.cost + 1))
    child.append(Torre(move(node.state, 0, 2), node, 2, node.depth + 1, node.cost + 1))
    child.append(Torre(move(node.state, 1, 0), node, 3, node.depth + 1, node.cost + 1))
    child.append(Torre(move(node.state, 1, 2), node, 4, node.depth + 1, node.cost + 1))
    child.append(Torre(move(node.state, 2, 0), node, 5, node.depth + 1, node.cost + 1))
    child.append(Torre(move(node.state, 2, 1), node, 6, node.depth + 1, node.cost + 1))
    nodes = []
    for procPaths in child:
        if procPaths.state:
            nodes.append(procPaths)
    return nodes

def bfs(estadoInicial):
    global MaxFrontier, NoFinal, profundidade
    boardVisited = set()
    Fila = deque([Torre(estadoInicial, None, None, 0, 0)])

    while Fila:
        node = Fila.popleft()
        boardVisited.add(node.map)
        if node.state == EstadoFinal:
            NoFinal = node
            break  
        posiblePaths = subNodes(node)

        for path in posiblePaths:
            if path.map not in boardVisited:
                Fila.append(path)
                boardVisited.add(path.map)
                if path.depth > profundidade:
                    profundidade = path.depth
        if len(Fila) > MaxFrontier:
            FilaSize = len(Fila)
            MaxFrontier = FilaSize

def dfs(estadoInicial):

    global MaxFrontier, NoFinal, profundidade

    boardVisited = set()
    stack = list([Torre(estadoInicial, None, None, 0, 0)])
    while stack:
        node = stack.pop()
        boardVisited.add(node.map)
        if node.state == EstadoFinal:
            NoFinal = node
            return stack
        #inverte a ordem dos filhos
        posiblePaths = reversed(subNodes(node))
        for path in posiblePaths:
            if path.map not in boardVisited:
                stack.append(path)
                boardVisited.add(path.map)
                if path.depth > profundidade:
                    profundidade = 1 + profundidade
        if len(stack) > MaxFrontier:
            MaxFrontier = len(stack)

def move(state, origem, destino):
    newState = [peg[:] for peg in state]

    def topo(torre):
        if not torre:
            return 99
        else:
            return torre[-1]

    torre0 = topo(newState[0])
    torre1 = topo(newState[1])
    torre2 = topo(newState[2])

    # verificação se movimento é valido
    if origem == 0:
        if destino == 1 and torre1 > torre0:
            newState[1].append(torre0)
            newState[0].pop()
        if destino == 2 and torre2 > torre0:
            newState[2].append(torre0)
            newState[0].pop()
        return newState
    if origem == 1:
        if destino == 0 and torre0 > torre1:
            newState[0].append(torre1)
            newState[1].pop()
        if destino == 2 and torre2 > torre1:
            newState[2].append(torre1)
            newState[1].pop()
        return newState
    if origem == 2:
        if destino == 0 and torre0 > torre2:
            newState[0].append(torre2)
            newState[2].pop()
        if destino == 1 and torre1 > torre2:
            newState[1].append(torre2)
            newState[2].pop()
        return newState
    return None


def main(metodo):
    global NoFinal

    #Tempo de execução
    start = timeit.default_timer()

    if(metodo=='bfs'):
        bfs(EstadoInicial)
    if(metodo=='dfs'):
        dfs(EstadoInicial)

    stop = timeit.default_timer()
    time = stop-start

    moves = []
    while NoFinal:
        if(NoFinal.move == 1):
            moves.insert(0, "Moveu da torre 1 -> 2")
        if(NoFinal.move == 2):
            moves.insert(0, "Moveu da torre 1 -> 3")
        if(NoFinal.move == 3):
            moves.insert(0, "Moveu da torre 2 -> 1")
        if(NoFinal.move == 4):
            moves.insert(0, "Moveu da torre 2 -> 3")
        if(NoFinal.move == 5):
            moves.insert(0, "Moveu da torre 3 -> 1")
        if(NoFinal.move == 6):
            moves.insert(0, "Moveu da torre 3 -> 2")

        NoFinal = NoFinal.parent

    # Resultados
    for i in moves:
        print(i)
    
    print("\ncusto: ", len(moves))
    print("nós expandidos: ", NoExpandido)
    print("profundidade: ", profundidade)
    print("tempo de execução: ", format(time, '.4f'))


if __name__ == '__main__':
    metodo = 'bfs' #ou 'dfs'
    main(metodo)
