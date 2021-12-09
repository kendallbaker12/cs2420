class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Graph:
    def __init__(self,numvertices):
        self.mNeighbors = []
        for i in range(numvertices):
            self.mNeighbors.append([])
    
    def addEdge(self,start,end):
        self.mNeighbors[start].append(end)
    
    # def isNotVisited(x,path):
    #     size = len(path)
    #     for i in range(size):
    #         if (path[i] == x):
    #             return 0
    #     return 1

    def FindPath(self,start,end):
        q = Queue()
        prev = []
        path =[]
        for i in range(len(self.mNeighbors)):
            prev.append(-1)
        prev[start] = start
        q.enqueue(start)
        while not q.isEmpty():
            c = q.dequeue()
            if c == end:
                path = [c]
                while prev[c]!=c:
                    path.append(prev[c])
                    c = prev[c]
                path.reverse()
                return path
            for n in self.mNeighbors[c]:
                if prev[n] == -1:
                    prev[n] = c
                    q.enqueue(n)
        return None        

            #for each neighbor n of c:
                #if n has not been visited:
                    #mark n as visited ffrom 
                    #enqueue n
            #return None

def main():
    file = open("edge.txt", "r")
    v = int(file.readline())
    e = int(file.readline())
    g = Graph(v)
    for dc in range(e):
        line = file.readline().split()
        g.addEdge(int(line[0]),int(line[1]))
    t = int(file.readline())
    for na in range(t):
        line = file.readline().split()
        path = g.FindPath(int(line[0]),int(line[1]))
        print(path)

main()





