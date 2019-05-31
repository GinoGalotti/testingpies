# Info and definition on https://github.com/gigasquid/wonderland-clojure-katas/tree/master/alphabet-cipher

class Cypher:

    def __init__(self):
        self.code = {}
        self.alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
        self.key = list("scones")

        for idx, letter in enumerate(self.alphabet_list):
            new_list = self.alphabet_list[idx:]
            new_list.extend(self.alphabet_list[:idx])
            self.code[letter] = new_list
            # it's a two dimentional Row - Colum matrix

    def set_key(self, key):
        self.key = list(key)

    def encode(self, message):
        message_cypher = []
        list_of_message = list(message)

        length_of_key = len(self.key)
        for idx, letter in enumerate(list_of_message):
            key_letter = self.key[idx % length_of_key]
            index_of_key = self.alphabet_list.index(key_letter)

            message_cypher.append(self.code[letter][index_of_key])

        return "".join(message_cypher)

    def decode(self, message): 

        return False

    def decipher(self,message, encoded_message):

        code = []
        for letter, encoded_letter in zip(message, encoded_message):
            index = (self.alphabet_list.index(encoded_letter) - self.alphabet_list.index(letter)) % len(self.alphabet_list)

            code.append(self.alphabet_list[index])

        return "".join(code)
