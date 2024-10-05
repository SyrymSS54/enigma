class rotor:
    def __init__(self) -> None:
        self.func_list = [self.first_add,self.second_add,self.first_sub,self.second_sub,self.first_mul,self.second_mul]

    def first_add(self,key):
        return key + 4
    
    def second_add(self,key):
        return key + 6
    
    def first_sub(self,key):
        return key - 3
    
    def second_sub(self,key):
        return key - 5
    
    def first_mul(self,key):
        return key * 2
    
    def second_mul(self,key):
        return key * 3
    
    def __getitem__(self,key):
        if key <= 5:
            return self.func_list[key]
        elif key > 5:
            return self.__getitem__(key-6)
        

if __name__ == "__main__":
    print(rotor()[0](5))