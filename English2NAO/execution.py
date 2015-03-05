from component import component

__author__ = 'NBUCHINA'

class sequence(component):
    tags = ["after", "then", "next"]
    regexp =r"(?!x)x"

    def __init__(self, string):
        pass

    def __repr__(self):
        return " & "

class parallel(component):
    tags = ["and", "while", "same time"]
    regexp = r"(?!x)x"

    def __init__(self, string):
        pass

    def __repr__(self):
        return " | "