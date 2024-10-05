from alphabet import alphabet
from rotor import rotor

class enigma:
    def __init__(self) -> None:
        self.input_text = self.func_input_text()
        self.normalize_text = self.normalize(self.input_text)
        self.cipher = self.func_input_cipher()
        self.final_hash = []
        self.final = ''
        self.rotor = rotor()

    def func_input_text(self):
        return input('Ввод текста:')
    
    def normalize(self,str):
        return list(map(lambda key: alphabet().__fetch_alpha__(key),list(str.lower())))
    
    def func_input_cipher(self):
        return list(map(int,list(input("Ввод шрифта:"))))
    
    def fetch(self):
        for elem in self.normalize_text:
            new_step_cipher = []

            if isinstance(elem,int):
                for cipher in self.cipher:

                    elem = self.rotor[cipher](elem)

                    if elem > 25:
                        new_step_cipher.append(cipher + 1)
                    elif elem < 0:
                        new_step_cipher.append(cipher - 1)
                    else:
                        new_step_cipher.append(cipher)

                self.final_hash.append(elem)
                    
                self.cipher = new_step_cipher
                print(elem, self.cipher)

            else:
                self.final_hash.append(elem)
                    
    def read(self):
        alpha = alphabet()
        for hash in self.final_hash:
            if isinstance(hash,int):
                self.final += alpha[hash]
            elif isinstance(hash,str):
                self.final += hash

    
if __name__ == "__main__":
    e = enigma()
    print(e.normalize_text)
    print(e.cipher)
    e.fetch()
    print(e.final_hash)
    e.read()
    print(e.final)