GSC_TYPES = {
    "UNKNOWN": -1,
    
    "INT":   0,
    "FLOAT": 1,
    "STR":   2
}

class Variable:
    def __init__(self, name, val) -> None:
        self.name = name
        self.val = val
        self.type = Variable.get_type(val)
    
    def set_value(self, value):
        self.val = value
        self.type = self.type = Variable.get_type(value)
    
    def get_value(self):
        return self.val

    def get_type(value):
        if type(value) == int:
            return GSC_TYPES["INT"]
        if type(value) == float:
            return GSC_TYPES["FLOAT"]
        if type(value) == str:
            return GSC_TYPES["STR"]
        return GSC_TYPES["UNKNOWN"]
    
    def __hash__(self):
        return self.name.__hash__();

class Register:
    def __init__(self) -> None:
        self.registeredVariables = {}
        self.registerVariableName = []

    def store_var(self, name, value):
        if name.__hash__() in self.registerVariableName:
            self.set_var(name, value)
        else:
            self.decl_var(name, value)

    def decl_var(self, name, value):
        self.registeredVariables[name] = Variable(name, value)
    
    def set_var(self, name, newValue):
        if not name in self.registeredVariables.keys():
            raise SyntaxError("Unknown variable: " + str(name))
        
        self.registeredVariables[name].set_value(newValue)
    
    def get_var(self, name):
        if not name in self.registeredVariables.keys():
            raise SyntaxError("Unknown variable: "+ str(name))
        
        return self.registeredVariables[name].get_value()