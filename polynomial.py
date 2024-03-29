class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    # exercise c): calculate the value of a polynomia
    def evaluate(self, val):
        return val
    
class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, val): 
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2) 
    
    def evaluate(self, val): 
        return self.p1.evaluate(val) + self.p2.evaluate(val)
    
# exercise b): print subtraction and division equations
class Sub: 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p2, (Add, Sub)): 
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2) 
    
    def evaluate(self, val): 
        return self.p1.evaluate(val) - self.p2.evaluate(val)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    # 注意检查子句计算优先级（括号匹配情况）
    # pay attention to clause calculation priorities (parentheses)
    def __repr__(self): 
        if isinstance(self.p1, (Add, Sub)):   # is a/b*c okay?
            repr_p1 = "( " + repr(self.p1) + " )"
        else:
            repr_p1 = repr(self.p1)

        if isinstance(self.p2, (Add, Sub)):
            repr_p2 = "( " + repr(self.p2) + " )"
        else: 
            repr_p2 = repr(self.p2)

        '''
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        '''
        return repr_p1 + " * " + repr_p2
    
    def evaluate(self, val): 
        return self.p1.evaluate(val) * self.p2.evaluate(val)

class Div:  # exercise b)
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self): 
        if isinstance(self.p1, (Add, Sub)): 
            repr_p1 = "( " + repr(self.p1) + " )"
        else:
            repr_p1 = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            repr_p2 = "( " + repr(self.p2) + " )"
        else: 
            repr_p2 = repr(self.p2)

        return repr_p1 + " / " + repr_p2
    
    def evaluate(self, val): 
        if self.p2.evaluate(val) == 0:
            raise ValueError("ERROR: Division by zero!")
        return self.p1.evaluate(val) / self.p2.evaluate(val)
    

# test
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print("poly:\t", poly)
print(poly.evaluate(-1))

poly1 = Sub(Add(X(), Mul(Int(3), X())), Int(4))
poly2 = Mul(Div(Add(X(), Int(2)), Sub(X(), Int(3))), Add(X(), Int(4)))
poly3 = Div(Div(X(), Int(2)), Add(X(), Int(1)))
print("poly1:\t", poly1)
print(poly1.evaluate(0))
print("poly2:\t", poly2)
print(poly2.evaluate(5))
print("poly3:\t", poly3)
print(poly3.evaluate(2))
# print(poly3.evaluate(-1))