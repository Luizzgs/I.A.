import timeit
from collections import deque


EstadoFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
NoFinal = None 
NoExpandido = 0 
MaxSearchDeep = 0
MaxFrontier = 0 


class PuzzleState:
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




def bfs(estadoInicial):
    global MaxFrontier, NoFinal, MaxSearchDeep
    boardVisited= set()
    Fila = deque([PuzzleState(estadoInicial, None, None, 0, 0)])

    while Fila:
        node = Fila.popleft()
        boardVisited.add(node.map)
        if node.state == EstadoFinal:
            NoFinal = node
            return Fila
        posiblePaths = subNodes(node)

        for path in posiblePaths:
            if path.map not in boardVisited:
                Fila.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Fila) > MaxFrontier:
            FilaSize = len(Fila)
            MaxFrontier = FilaSize
            

def dfs(estadoInicial):

    global MaxFrontier, NoFinal, MaxSearchDeep

    boardVisited = set()
    stack = list([PuzzleState(estadoInicial, None, None, 0, 0)])
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
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = 1 + MaxSearchDeep
        if len(stack) > MaxFrontier:
            MaxFrontier = len(stack)
    



def subNodes(node):

    global NoExpandido
    NoExpandido = NoExpandido + 1

    nextPaths = []
    nextPaths.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1))
    nextPaths.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1))
    nextPaths.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1))
    nextPaths.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1))
    nodes=[]
    for procPaths in nextPaths:
        if(procPaths.state!=None):
            nodes.append(procPaths)
    return nodes


def move(state, direction):
    #cópia
    newState = state[:]
    
    #encontra o index do 0
    index = newState.index(0)
    
    #Direção 1 = Cima, 2 = Baixo, 3 = Esquerda, 4 = Direita

    if(index==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[0]
            newState[0]=newState[3]
            newState[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[0]
            newState[0]=newState[1]
            newState[1]=temp
        return newState      
    if(index==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[1]
            newState[1]=newState[4]
            newState[4]=temp
        if(direction==3):
            temp=newState[1]
            newState[1]=newState[0]
            newState[0]=temp
        if(direction==4):
            temp=newState[1]
            newState[1]=newState[2]
            newState[2]=temp
        return newState    
    if(index==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=newState[2]
            newState[2]=newState[5]
            newState[5]=temp
        if(direction==3):
            temp=newState[2]
            newState[2]=newState[1]
            newState[1]=temp
        if(direction==4):
            return None
        return newState
    if(index==3):
        if(direction==1):
            temp=newState[3]
            newState[3]=newState[0]
            newState[0]=temp
        if(direction==2):
            temp=newState[3]
            newState[3]=newState[6]
            newState[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[3]
            newState[3]=newState[4]
            newState[4]=temp
        return newState
    if(index==4):
        if(direction==1):
            temp=newState[4]
            newState[4]=newState[1]
            newState[1]=temp
        if(direction==2):
            temp=newState[4]
            newState[4]=newState[7]
            newState[7]=temp
        if(direction==3):
            temp=newState[4]
            newState[4]=newState[3]
            newState[3]=temp
        if(direction==4):
            temp=newState[4]
            newState[4]=newState[5]
            newState[5]=temp
        return newState
    if(index==5):
        if(direction==1):
            temp=newState[5]
            newState[5]=newState[2]
            newState[2]=temp
        if(direction==2):
            temp=newState[5]
            newState[5]=newState[8]
            newState[8]=temp
        if(direction==3):
            temp=newState[5]
            newState[5]=newState[4]
            newState[4]=temp
        if(direction==4):
            return None
        return newState
    if(index==6):
        if(direction==1):
            temp=newState[6]
            newState[6]=newState[3]
            newState[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=newState[6]
            newState[6]=newState[7]
            newState[7]=temp
        return newState
    if(index==7):
        if(direction==1):
            temp=newState[7]
            newState[7]=newState[4]
            newState[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[7]
            newState[7]=newState[6]
            newState[6]=temp
        if(direction==4):
            temp=newState[7]
            newState[7]=newState[8]
            newState[8]=temp
        return newState
    if(index==8):
        if(direction==1):
            temp=newState[8]
            newState[8]=newState[5]
            newState[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=newState[8]
            newState[8]=newState[7]
            newState[7]=temp
        if(direction==4):
            return None
        return newState



def main(data, metodo):

    global NoFinal
    EstadoInicial = []
    
    for i in data:
        EstadoInicial.append(i)    

    #Tempo de execução
    start = timeit.default_timer()

    if(metodo=='bfs'):
        bfs(EstadoInicial)
    if(metodo=='dfs'):
        dfs(EstadoInicial)

    stop = timeit.default_timer()
    time = stop-start


    moves = []
    while EstadoInicial != NoFinal.state:
        if NoFinal.move == 1:
            path = 'Cima'
        if NoFinal.move == 2:
            path = 'Baixo'
        if NoFinal.move == 3:
            path = 'Esquerda'
        if NoFinal.move == 4:
            path = 'Direita'
        moves.insert(0, path)
        NoFinal = NoFinal.parent

    
    #Resultados
    print("\ncaminho: ", moves)
    print("\ncusto: ",len(moves))
    print("nós expandidos: ",str(NoExpandido))
    print("Tempo(s): ",format(time, '.8f'))
   

if __name__ == '__main__':
    #define a entrada inicial
    data = [4,0,5,8,7,3,2,1,6]
    #define o metodo de busca (bfs ou dfs)
    metodo = 'bfs'
    
    main(data, metodo)
