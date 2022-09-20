class Interpreter:
    def cutInstr(self,inp):
        self.instr = []
        BUFF = ""
        strFlag = False
        counterslashFlag = False
        for i in inp:
            if (strFlag):
                if (i == '"'):
                    strFlag = False
                BUFF += i
            else:
                if (i == '"'):
                    strFlag = True
                elif (i == " "):
                    self.instr.append(BUFF)
                    BUFF = ""
                    continue
                BUFF += i
        self.instr.append(BUFF)
        return self.instr

    def readInstr(self):
        funcFlag = False
        paramsFlag = False
        func = ""
        params = []
        function = []
        for i in self.instr:
            if not funcFlag:
                if (i == "f"):
                    funcFlag = True
            else:
                if (i == "f"):
                    print(f"interpreted {func} with ["+",".join([repr(p) for p in params])+"]")
                    paramsFlag = False
                    func = ""
                    params = []
                elif not paramsFlag:
                    func = i
                    paramsFlag = True
                else:
                    params.append(i)
        else:
            print(f"interpreted {func} with ["+",".join([repr(p) for p in params])+"]")
            function.append([func,params])
            paramsFlag = False
            func = ""
        return function

    def executeInstr(self):
        A = self.readInstr()
        for i in A:
            if (i[0] == "show"):
                for j in i[1]:
                    print(j.replace('"',""),end="")
            else:
                print("idk man")
            

