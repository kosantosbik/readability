# -*- encoding: utf-8 -*-
import sys

class word_count():
    def __init__(self, text):
        self.words = []
        self.total = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0

        temp_words = text.split()
        for word in temp_words:
            self.words.append(word)

        self.count()

    def count(self):
        vowels = ["a", "e", "ı", "i", "u", "ü", "o", "ö"]
        for word in self.words:
            vowel_count = 0
            for letter in word:
                if letter in vowels:
                    vowel_count += 1

            if vowel_count == 2:
                self.two += 1
            elif vowel_count == 3:
                self.three += 1
            elif vowel_count == 4:
                self.four += 1
            elif vowel_count == 5:
                self.five += 1
            elif vowel_count == 6:
                self.six += 1

            self.total += vowel_count

    def get_numbers(self):
        return self.two, self.three, self.four, self.five, self.six, self.total


if __name__ == '__main__':
    wc = word_count("")
    w2,w3,w4,w5,w6,wt = wc.get_numbers()
    print("2 heceli:", w2)
    print("3 heceli:", w3)
    print("4 heceli:", w4)
    print("5 heceli:", w5)
    print("6 heceli:", w6)
    print("Toplam hece:", wt)
