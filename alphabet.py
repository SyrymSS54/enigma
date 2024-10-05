class alphabet:
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_len = len(alphabet_list)

    def __init__(self) -> None:
        self.alphabet = self.alphabet_list
        self.length = self.alphabet_len

    def __getitem__(self,key):
        if key > (self.length-1):
            return self.__getitem__(key-26)
        else:
            return self.alphabet[key]
        
    def __fetch_alpha__(self,key):
        if key.isalpha() and len(key) == 1:
            return self.alphabet.index(key)
        else:
            return key
    
if __name__ == "__main__":
    al = alphabet()
    print(al[27])
    
    def fetch(obj = alphabet(),key = ''):
        return obj.__fetch_alpha__(key)
    
    print(fetch(key = 'q'))
            
