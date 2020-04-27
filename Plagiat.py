
class Plagiat:
    def __init__(self, tekst, tekstcheck, quantity2): 
        self.quantity2 = quantity2
        self.tekst = tekst
        self.tekstcheck = tekstcheck
    def compare (tekst, tekstcheck, quantity2):
         return (100 % *q/quantity2)
class Text:
    def __init__(self , quantity):
        self.quantity = quantity
    def tokenize(self, quantity):
        return textlist
        return quantity

 textBase = " В лесу родилась елочка. В лесу она росла.
                 Зимой и летом стройная, зеленая была!
                 Метель ей пела песенку - Спи елочка , бай бай!
                 Мороз снежком укутывал смотри не замерзай!"
print ( Plagiat.compare (Text (textBase), Text(stih)))
if __name__  == "__main__":
    stih = " В лесу родилась елочка. В лесу она росла."
    stih = Text()
    print (stih.tokenize())
    print ( Plagiat.compare (Text (textBase), Text(stih)))
    stih = " Посадил дед репку. Выросла репка большая."
    print (stih.tokenize())
    print ( Plagiat.compare (Text (textBase), Text(stih)))
    stih = Text()
    stih = " Смеркалось?"
    print (stih.tokenize())
    print ( Plagiat.compare (Text (textBase), Text(stih)))
    stih = Text()
    stih = "Метель ей пела песенку - Спи елочка , бай бай!"
    print (stih.tokenize())
    print ( Plagiat.compare (Text (textBase), Text(stih)))
