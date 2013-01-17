class Page:
    def __init__(self):
        self.EmailList = []
        
    def isComment(self, aStr):
        if len(aStr)<7:
            return 1
        elif aStr[0] == "#" or aStr[0] == ' ' or aStr[0]=='\n':
            return 1
        else:
            return 0
        
    def convert(self, aStr):
        if '\n' in aStr:
            aStr = aStr.replace('\n','')
        return aStr.replace('\243\300', '@')
    
    def AddList(self, aStr):
        self.EmailList.append(aStr)
        
    def MakeList(self, aStr):
        file = open(aStr, 'r')
        lines = file.readlines()
        for i in lines:
            if self.isComment(i):
                continue
            self.AddList( self.convert(i) )
        
        
