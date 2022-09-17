from godscript.errors.error import Error

class SyntaxRuleError(Error):
    def __init__(self, line, reason):
        self.line = line
        self.reason = reason

    def __str__(self):
        return f"SyntaxRuleError[{self.line}]: {self.reason}"