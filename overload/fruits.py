class Caixa:

    def __init__(self, unit, name):
        assert isinstance(name,str)
        assert isinstance(unit,int)
        assert unit >= 0
        self.unit = unit
        self.name = name

    def __eq__(self,obj):
        assert isinstance(obj,Caixa)
        assert self.name == obj.name, "As frutas devem ser iguais"
        return self.unit == obj.unit,
    
    def __lt__(self,obj):
        assert isinstance(obj,Caixa)
        assert self.name == obj.name, "As frutas devem ser iguais"
        return self.unit < obj.unit
    
    def __gt__(self,obj):
        assert isinstance(obj,Caixa)
        assert self.name == obj.name, "As frutas devem ser iguais"
        return self.unit > obj.unit

    def __add__(self,obj):
        assert isinstance(obj,Caixa)
        assert self.name == obj.name, "As frutas devem ser iguais"
        return Caixa(self.unit + obj.unit,self.name)

    def __sub__(self,obj):
        assert isinstance(obj,Caixa)
        assert self.name == obj.name, "As frutas devem ser iguais"
        return Caixa(self.unit - obj.unit,self.name)

    def __str__(self):
        return "{} {}".format(self.name, self.unit)

class Caminhao:
    def __init__(self,name,limit):
        self.name = name
        self.limit = limit
        self.caixas = list()
        self.space = 0
    
    def add(self,caixa):
        assert isinstance(caixa,Caixa)
        if(self.space <= self.limit):
            self.caixas.append(caixa)
    
    def __len__(self):
        return len(self.caixas)
    
    def __getitem__(self,position):
        return self.caixas[position]
    
    def __str__(self):
        return "{}".format(self.name)