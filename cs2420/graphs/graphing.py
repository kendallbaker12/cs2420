from graphics import *

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def top(self):
        if self.items == []:
            return ""
        return self.items[-1]
    


def InfixToPostfix(infix):
    s = Stack()
    postfix = ""
    for c in infix:
        if c in "0123456789":
            #x*(5/2)print(c)
            postfix += c
        elif c == 'x':
            postfix += c
        elif c in "+-":
            while not s.isEmpty() and s.top() in "+-*/":
                postfix += s.pop()
            s.push(c)
        elif c in "*/":
            print(s.top())
            while not s.isEmpty() and s.top() in "*/":
                #print(postfix)
                postfix += s.pop()
                #print(postfix)
            s.push(c)
        elif c == '(':
            print(c)
            s.push(c)
        elif c == ')':
            while s.top() != '(':
                print(s.top())
                postfix += s.pop()
            s.pop()
    while not s.isEmpty():
        postfix += s.pop()
            
            
    return postfix


def EvaluatePostfix(postfix,x):
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
        elif c == '-':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs - rhs
            s.push(result)
        elif c == '*':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs * rhs
            s.push(result)
        elif c == '/':
            rhs = s.pop()
            lhs = s.pop()
            result = lhs / rhs
            s.push(result)
        #print(s.items)
    return s.pop()
        

        



def main():

    #PrintDirections()
    infix = input("Enter your functions here: ")
    postfix = InfixToPostfix(infix)
    print(postfix)

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
        y = EvaluatePostfix(postfix, x)
        points.append( [x,y] )
        x += .1
    print(points)

    win = GraphWin("My Circle", 800,800)
    win.setCoords(xlow,ylow, xhigh,yhigh)
    for i in range(len(points)-1):
        #c = Circle(Point(points[i][0],points[i][1]),.1)
        #c.draw(win)
        l = Line(Point(points[i][0], points[i][1]),
                Point(points[i+1][0], points[i+1][1]) )
        l.draw(win)
    win.getMouse()
    win.close()

main()