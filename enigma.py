from alphabet import alphabet
from rotor import rotor
from reverb_rotor import reverb_rotor

class enigma:
    def __init__(self) -> None:
        self.input_text = self.func_input_text()
        self.normalize_text = self.normalize(self.input_text)
        self.cipher = self.func_input_cipher()
        self.rotor = rotor()
        self.reverb_rotor = reverb_rotor()
        self.final = []

    def func_input_text(self):
        return input('Ввод текста:')
    
    def normalize(self,str):
        return list(map(lambda key: alphabet().__fetch_alpha__(key),list(str.lower())))
    
    def func_input_cipher(self):
        return list(map(int,list(input("Ввод шрифта:"))))
    
    def fetch(self):
        print(self.normalize_text)
        for elem in self.normalize_text:
            if isinstance(elem,int):
                for count in range(0,len(self.cipher)):
                    rotor_count = self.cipher[count]
                    func = self.rotor[rotor_count]
                    print("{} -> {}".format(elem,func(elem)))
                    elem = func(elem)

                    if elem > 25:
                        self.cipher[count] += 1
                    elif elem < 0:
                        self.cipher[count] -= 1
                print(elem,self.cipher)
                self.final.append(elem)
            else:
                self.final.append(elem)

    def reverb(self):
        self.input_text = self.func_input_text()
        self.normalize_text = self.normalize(self.input_text)
        self.cipher = self.func_input_cipher()
        
        reverb = []
        for elem in self.final:
            if isinstance(elem,int):
                for count in range(len(self.cipher)-1,-1,-1):
                    rotor_count = self.cipher[count]
                    func = self.reverb_rotor[rotor_count]
                    print("{} -> {}".format(elem,func(elem)))

                    if elem > 25:
                        self.cipher[count] += 1
                    elif elem < 0:
                        self.cipher[count] -= 1
                    elem = func(elem)

                reverb.append(elem)
            else:
                reverb.append(elem)
        return reverb

    def read(self):
        al = alphabet()
        value = ''
        for elem in self.final:
            if isinstance(elem,int):
                value += al[elem]
            else:
                value += elem
        return value




    
if __name__ == "__main__":
    e = enigma()
    e.fetch()
    print(e.read())
    print(e.reverb())
    print(e.normalize_text)