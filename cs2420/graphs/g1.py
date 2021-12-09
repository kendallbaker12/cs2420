from graphics import *


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def InfixToPostfix(infix):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infix.split()

    for token in tokenList:
        if token in "x" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)





def postfixEval(postfix,x):
    s = Stack()
    for c in postfix:
        if c  >= '0' and c <= '9':
            s.push(float(c))
        elif c == 'x':
            s.push(x)
        elif c == '+':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs + rhs
            s.push(result)
        return s.pop()





def main():

    
    infix = input("Enter your functions here: ")
    postfix = InfixToPostfix(infix)

    points = []
    xlow = -10
    ylow = -10
    xhigh = +10
    yhigh = +10
    xinc = .1
    x = xlow
    epsilon = .0001
    while x < xhigh+epsilon:
        #y = x*x
        y = postfixEval(postfix, x)
        points.append( [x,y] )
        x += .1
    print(points)

    win = GraphWin("My Circle", 500,500)
    win.setCoords(xlow,ylow, xhigh,yhigh)
    for i in range(len(points)):
        #c = Circle(Point(points[i][0],points[i][1]),.1)
        #c.draw(win)
        l = Line(Point(points[i][0], points[i][1]),
                Point(points[i+1][0], points[i+1][1]) )
        l.draw(win)
    win.getMouse()
    win.close()

main()