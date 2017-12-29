

class Xor(object):
    def __init__(self, key: bin, text: str):
        self.encoded = []
        self.key = key
        self.text = [x for x in text.encode('utf-8')]
        self.xor_it()

    def xor_it(self):
        for character in self.text:
            self.encoded.append(bin(character ^ self.key)[2:].zfill(8))

    def __str__(self):
        return self.encoded


