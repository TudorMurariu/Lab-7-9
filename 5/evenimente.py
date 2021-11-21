class evenimente:
    def __init__(self ,ID ,data ,timp ,descriere):
        self.ID = ID
        self.data = data
        self.timp = timp
        self.descriere = descriere
        self.lista_persoane = []
    
    def __str__(self):
        return '(' + str(self.ID) + ", " + self.data + ", " + self.timp + ", " + self.descriere + ')'
    
    def set_ID(self, ID):
        self.ID = ID

    def set_data(self, data):
        self.data = data

    def set_timp(self, timp):
        self.timp = timp

    def set_descriere(self, descriere):
        self.descriere = descriere

    def get_ID(self):
        return self.ID

    def get_data(self):
        return self.data

    def get_timp(self):
        return self.timp

    def get_descriere(self):
        return self.descriere

    def __gt__(self, other):
        data1 = self.get_data().split('.') 
        data2 = other.get_data().split('.') 
        if data1[2] > data2[2]:
            return True
        elif data1[2] == data2[2] and data1[1] > data2[1]:
            return True
        elif data1[2] == data2[2] and data1[1] == data2[1] and data1[0] > data2[0]:
            return True
        elif data1[2] == data2[2] and data1[1] == data2[1] and data1[0] == data2[0] and self.get_descriere() > other.get_descriere():
            return True
        return False
        
    
