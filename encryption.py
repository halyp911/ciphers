import string


class Cipher:

    def __init__(self, text):
        self.text = text
    
    def szyfruj_znak(self, znak):
        znak = znak.lower()
        if 'a' <= znak <= 'z': 
            znak = ord(znak)
            znak = znak + 13
            if znak > ord('z'):
                znak  = znak - ord('z') + ord('a') - 1
                znak = chr(znak)
            else:
                znak = chr(znak)
        return znak
    
    def get_atbash_cipher(self):
        cipher = {}
        size = len(string.ascii_lowercase)
        for i in range(size):
            key = string.ascii_lowercase[i]
            val = string.ascii_lowercase[size - i - 1]
            cipher[key] = val
        return cipher

    def code_message(self, msg):
        new_msg = ""
        cipher = self.get_atbash_cipher()
        for c in msg:
            if c in cipher:
                c = cipher[c]
                new_msg = new_msg + c
        return new_msg

    def encryption_cezar(self):
        nowy_napis = ""

        for litera in self.text:
            nowy_napis = nowy_napis + self.szyfruj_znak(litera)
        self.text = nowy_napis
        return self.text
    
    def decryption_cezar(self):
        nowy_napis = ""

        for litera in self.text:
            nowy_napis = nowy_napis + self.szyfruj_znak(litera)
        self.text = nowy_napis
        return self.text

    def encryption_atbash(self):
        nowy_napis = ""

        for litera in self.text:
            nowy_napis = nowy_napis + self.code_message(litera)
            self.text = nowy_napis
        return self.text
    
    def decryption_atbash(self):
        nowy_napis = ""

        for litera in self.text:
            nowy_napis = nowy_napis + self.code_message(litera)
            self.text = nowy_napis
        return self.text

if __name__ == '__main__':
    a = Cipher('abcde')
    print(a.encryption_cezar())
    print(a.decryption_cezar())
    b = Cipher('abcde')
    print(b.encryption_atbash())
    print(b.decryption_atbash())