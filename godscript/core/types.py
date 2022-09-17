from godscript.core.register import Register

class ValueType:
    def __init__(self, val) -> None:
        self.val = val
    
    def get_value(self):
        return self.val
    
    def set_value(self, val):
        self.val = val
    
    def __str__(self) -> str:
        return self.val
    
class ReferenceType:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    
    def get_value(self):
        return Register.get_value(self.name)

    def set_value(self):
        Register.set_value(self.name)

    def __str__(self) -> str:
        return f"Ref({self.name})"

class LineReferenceType:
    def __init__(self, line) -> None:
        self.line = line

    def get_line(self):
        return self.line
    
    def __str__(self) -> str:
        return f"LineRef({self.line})"