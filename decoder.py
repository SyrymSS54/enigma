from alphabet import alphabet
from reverb_rotor import reverb_rotor
from rotor import rotor

class decoder:
    def __init__(self) -> None:
        self.input_text = self.func_input_text()
        self.normalize_text = self.normalize(self.input_text)
        self.ciphers = self.func_input_cipher()
        self.final = []
        self.final_text = ''
        self.rotor = reverb_rotor()



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
                for cipher in reversed(self.ciphers):

                    elem = self.rotor[cipher](elem)

                    if elem > 25:
                        new_step_cipher.append(cipher - 1)
                    elif elem < 0:
                        new_step_cipher.append(cipher + 1)
                    else:
                        new_step_cipher.append(cipher)

                self.final.append(elem)
                    
                self.ciphers = new_step_cipher
                print(elem, self.ciphers)

            else:
                self.final.append(elem)
    
    def read(self):
        alpha = alphabet()
        for hash in self.final:
            if isinstance(hash,int):
                self.final_text += alpha[hash]
            elif isinstance(hash,str):
                self.final_text += hash
                
    

if __name__ == "__main__":
    decoder_obj = decoder()
    print("Text:",decoder_obj.input_text)
    print("Text code:",decoder_obj.normalize_text)
    print("Cipher:",decoder_obj.ciphers)
    decoder_obj.fetch()
    decoder_obj.read()
    print("decode:",decoder_obj.final_text)