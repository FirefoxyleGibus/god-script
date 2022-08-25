GSC_TYPES = {
    "UNKNOWN": -1,
    
    "INT":   0,
    "BOOL":  1,
    "STR":   2,
    "FLOAT": 3
}

class Variable:
    def __init__(self, name, val) -> None:
        self.name = name
        self.type = Variable.get_type(val)
        self.val = Variable.parse_to_type(val)
    
    def set_value(self, value):
        self.val = Variable.parse_to_type(value)
        self.type = self.type = Variable.get_type(value)
    
    def get_value(self):
        return self.val

    def get_type(value):
        if type(value) == int:
            return GSC_TYPES["INT"]
        if type(value) == float:
            return GSC_TYPES["FLOAT"]
        if type(value) == str:
            # avoid reconversion
            if value[0] == '"' and value[-1] == '"':
                return value
            # try to convert
            if value == "false"\
            or value == "true": return GSC_TYPES["BOOL"]
            if "." in value:    return GSC_TYPES["FLOAT"]
            try: int(value);    return GSC_TYPES["INT"]
            except: pass

            return GSC_TYPES["STR"]
        return GSC_TYPES["UNKNOWN"]
    
    def parse_to_type(value):
        if type(value) == int:
            return int(value)
        if type(value) == float:
            return float(value)
        if type(value) == str:
            # avoid reconversion
            if value[0] == '"' and value[-1] == '"':
                return str(value)
            # try to convert
            if value == "false": return 0
            if value == "true":  return 1
            if "." in value: return float(value)
            try: return int(value);
            except: pass
        return value
    
    def __hash__(self):
        return self.name.__hash__();

class Register:
    def __init__(self) -> None:
        self.registeredVariables = {}

    def store_var(self, name, value):
        if name in self.registeredVariables:
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