# Info and definition on https://github.com/gigasquid/wonderland-clojure-katas/tree/master/alphabet-cipher

class Cypher:

    def __init__(self):
        self.alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
        self.key = list("scones")

    def set_key(self, key):
        self.key = list(key)

    def encode(self, message):
        message_cypher = []
        list_of_message = list(message)

        length_of_key = len(self.key)
        for idx, letter in enumerate(list_of_message):
            key_letter = self.key[idx % length_of_key]
            key_shift = self.alphabet_list.index(key_letter)
            new_index = (self.alphabet_list.index(letter) + key_shift) % len(self.alphabet_list)

            message_cypher.append(self.alphabet_list[new_index])

        return "".join(message_cypher)

    def decode(self, message):
        message_cypher = []
        list_of_message = list(message)

        length_of_key = len(self.key)
        for idx, letter in enumerate(list_of_message):
            key_letter = self.key[idx % length_of_key]
            key_shift = self.alphabet_list.index(key_letter)
            new_index = (self.alphabet_list.index(letter) - key_shift) % len(self.alphabet_list)

            message_cypher.append(self.alphabet_list[new_index])

        return "".join(message_cypher)

    def get_key_shift(self, key_letter):
        return self.alphabet_list.index(key_letter)

    def decipher(self,message, encoded_message):

        code = []
        for letter, encoded_letter in zip(message, encoded_message):
            index = (self.alphabet_list.index(encoded_letter) - self.alphabet_list.index(letter)) % len(self.alphabet_list)

            code.append(self.alphabet_list[index])

        return "".join(code)
