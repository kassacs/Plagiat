from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from pprint import pprint
class Plagiat:
    def __init__(self, tekst, tekstcheck): 
        self.tekst = tekst
        self.tekstcheck = tekstcheck
    def compare (tekst, tekstcheck):
        return sum(map(lambda x: tekst.count(x), tekstcheck))/len(tekstcheck)
    def result (tekst, tekstcheck):
        if self.compare(tekst, tekstcheck) > 0.5 :
            pprint ( " Заимствование без корректного оформления ссылки ", Text.author(textBase), Text.title(textBase), self.compare(tekst, tekstcheck))
        else : print ( "Ваше произведение уникально !" )   
            
class Text:
    def __init__(self ,text):
        self.text = text
    def tokenize(self, text):
        return sent_tokenize(text, 'russian')
    def author (self, text):
        if "Автор" in word_tokenize(text, 'russian'): 
            return word_tokenize(text, 'russian')[word_tokenize(text, 'russian').index ("Автор")+1:word_tokenize(text, 'russian').index ("Автор")+3:]
    def title (self, text):
        if "Наименование" in sent_tokenize(text, 'russian'): 
            return sent_tokenize(text, 'russian')[sent_tokenize(text, 'russian').index ("Наименование")+2]               
textBase = open('Лень и энтропия.txt', 'r')
if __name__  == "__main__":
    textcheck = open('Лень и энтропия_цитата.txt', 'r')
    textcheck = Text()
    print (textcheck.tokenize())
    print ( Plagiat.result (Text.tokenize(textBase), Text.tokenize(textcheck)))
    stih = " Посадил дед репку. Выросла репка большая."
    print (stih.tokenize())
    print ( Plagiat.result (Text.tokenize(textBase), Text.tokenize(stih)))
    stih = Text()
    stih = " Смеркалось?"
    print (stih.tokenize())
    print ( Plagiat.result (Text.tokenize(textBase), Text.tokenize(stih)))
    stih = Text()
    stih = "Метель ей пела песенку - Спи елочка , бай бай!"
    print (stih.tokenize())
    print ( Plagiat.result (Text.tokenize(textBase), Text.tokenize(stih)))
