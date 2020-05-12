from nltk.tokenize import sent_tokenize
class Plagiat:
    def __init__(self, tekst, tekstcheck): 
        self.tekst = tekst
        self.tekstcheck = tekstcheck
    def compare (tekst, tekstcheck):
         return sum(map(lambda x: tekst.count(x), tekstcheck))/len(tekstcheck)
class Text:
    def __init__(self ,text):
        self.text = text
    def tokenize(self, text):
        return sent_tokenize(text, 'russian')
textBase = "В лесу родилась елочка. В лесу она росла.
            Зимой и летом стройная, зеленая была!
            Метель ей пела песенку - Спи елочка , бай бай!
            Мороз снежком укутывал смотри не замерзай!"
print ( Plagiat.compare (Text (textBase), Text(stih)))
if __name__  == "__main__":
    stih = " В лесу родилась елочка. В лесу она росла. Но не выросла"
    stih = Text()
    print (stih.tokenize())
    print ( Plagiat.compare (Text.tokenize(textBase), Text.tokenize(stih)))
    stih = " Посадил дед репку. Выросла репка большая."
    print (stih.tokenize())
    print ( Plagiat.compare (Text.tokenize(textBase), Text.tokenize(stih)))
    stih = Text()
    stih = " Смеркалось?"
    print (stih.tokenize())
    print ( Plagiat.compare (Text.tokenize(textBase), Text.tokenize(stih)))
    stih = Text()
    stih = "Метель ей пела песенку - Спи елочка , бай бай!"
    print (stih.tokenize())
    print ( Plagiat.compare (Text.tokenize(textBase), Text.tokenize(stih)))
