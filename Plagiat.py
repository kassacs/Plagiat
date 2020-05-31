from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from pprint import pprint
class Plagiat:
    def __init__(self, tekst, tekstcheck):
        self.tekst = tekst
        self.tekstcheck = tekstcheck
    def compare (self,tekst, tekstcheck):
        return sum(map(lambda x: tekst.count(x), tekstcheck))/len(tekstcheck)
    def result (self,tekst, tekstcheck):
        if self.compare(tekst, tekstcheck) > 0.5 :
            print ( " Заимствование без корректного оформления ссылки ", textBase.author(textBase.text), textBase.title(textBase.text),"Заимствованно:", str(self.compare(tekst, tekstcheck)))
        else : print ( "Ваше произведение уникально !" )

class Text:
    def __init__(self ,text):
        self.text = text
    def tokenize(self, text):
        return sent_tokenize(text, 'russian')
    def author (self, text):
        if "Автор" in word_tokenize(text, 'russian'):
            return word_tokenize(text, 'russian')[word_tokenize(text, 'russian').index ("Автор")+2:word_tokenize(text, 'russian').index ("Автор")+4:]
    def title (self, text):
        if "Наименование" in word_tokenize(text, 'russian'):
            return word_tokenize(text, 'russian')[word_tokenize(text, 'russian').index ("Наименование")+2:word_tokenize(text, 'russian').index ("Наименование")+5:]
textBase ="""Автор: Иванов И.И.
Наименование: Лень и Энтропия
В этой статье приведем небольшую, с одной стороны шутливую, но с другой стороны полностью научную теорию с помощью которой можно оправдать себя в те моменты, когда над
Вами взяла верх лень. Дело в том, что в физике существует такая термодинамическая величина как энтропия. Её научное значение определяет меру необратимого рассеивания
энергии. В других случаях она же может определять вероятность осуществления какого-либо макроскопического состояния. Однако, скажем так, «в быту» проще понять значение
энтропии как меры неупорядоченности системы: чем меньше элементы системы подчинены какому-либо порядку, тем выше энтропия.Здесь сделаем небольшое уточняющее замечание
о том, что такое порядок. Это очень важно, потому что ситуацию, когда что-то равномерно распределено по доступному пространству можно назвать беспорядком или хаосом
(если, например, речь идет о мусоре, равномерно накиданном на пол в комнате). Но подобную ситуацию можно назвать и порядком (если речь идет, например, о качественно и
равномерно окрашенной стене), тут уж кому что, и у кого какие ассоциации.Однако мы договоримся для нужд этой статьи, что, как и все физики и другие ученые, будем
понимать под порядком наличие некоторой выраженной структуры в системе (например, существование конкретных предметов в определенных точках пространства), а под
беспорядком – равномерное распределение всех видов материи в пространстве. В таком случае, энтропия – это мера беспорядка. На данный момент Вселенная находится в
относительном порядке. У нас имеется множество космических тел, у каждого из них имеется своя форма, размеры и свойства, все они расположены в определенных местах.
Таким образом, в нашей системе присутствует определенная структура.Но, к сожалению, наукой безоговорочно доказано, что энтропия в замкнутых термодинамических системах
может только возрастать или оставаться неизменной. Таким образом, любая система стремиться к беспорядку, т.е. к равномерному распределению всей имеющейся материи по
доступному пространству. Это утверждение может локально нарушаться, т.е. в некоторых областях пространства часть элементов, составляющих систему, могут стремиться и к
порядку, но вся замкнутая система в целом, всегда стремится только к беспорядку либо сохраняет достигнутый уровень беспорядочности. Иными словами, если где-то
становится чуть больше порядка, то в другом месте беспорядка становится еще больше. Так вот если применить закон неубывания энтропии (беспорядка) ко всей Вселенной в
целом, то получается, что однажды вся материя должна равномерно распределиться по всей Вселенной. При этом не останется никаких выделенных объектов, таких как звезды
или планеты. Всё пространство будет абсолютно равномерно заполнено однородной кашей из различных частиц. А энтропия (или беспорядок) достигнет своего окончательного
максимума. Такое состояние называется Тепловой смертью Вселенной. Существуют разные оценки на счет того, когда она должна произойти. В любом случае это один из самых
отдалённых сценариев конца света. Если в конце концов Вселенная придет именно к такому состоянию, то случится это через очень и очень много миллиардов лет.
Другой важной особенностью энтропии является то, что она возрастает только если что-то происходит, и наоборот, если что-то происходит, то энтропия обязательно
возрастает. А если ничего не происходит, то энтропия по крайней мере остается неизменной. Но так как любое увеличение энтропии, т.е. беспорядка приближает нас к
Тепловой смерти Вселенной, то выходит, что пока ничего не происходит, то этот конец, по крайней мере, не приближается. А как только начинают происходить определенные
события, то Тепловая смерть Вселенной обязательно приближается к нам во времени. Человек конечно не может абсолютно ничего не делать, он должен как минимум дышать, его
сердце бьется, происходят другие процессы в организме. Однако, если человек просто лежит на диване, то энтропия увеличивается значительно медленнее, чем в случае если
человек возьмется активно работать. А значит и Тепловая смерть Вселенной в случае если человек бездельничает приближается медленнее, чем в случае если человек
работает. Этот эффект конечно очень слабый, численные оценки опять-таки очень затруднены, но в любом случае вклад одного человека и его образа жизни в то, когда
наступит Тепловая смерть Вселенной исчисляется малейшими долями секунды. С учетом того, что само это событие удалено от нас на миллиарды лет, то получается, что
относительное влияние каждого человека на этот процесс совсем уж ничтожно мало. Тем не менее, строго говоря, с точки зрения науки все же этот эффект присутствует.
Поэтому, свою лень можно оправдать научно тем, что Вы стремитесь максимально отсрочить момент Тепловой смерти Вселенной. Правды ради отметим, что Тепловая смерть
Вселенной, это лишь гипотеза, лишь один из нескольких десятков возможных сценариев развития событий и того, как в итоге наступит конец Вселенной. Многие из
альтернативных теорий развития событий вообще не предполагают того, что когда-либо у Вселенной должен случиться некий печальный конец. Причем гипотеза о Тепловой
смерти Вселенной далеко не самая обоснованная из всех этих теорий. Ну и главное, само наличие большого количества подобных теорий указывает на то, что науке, к
сожалению, пока неизвестен доподлинно сценарий развития Вселенной в будущем, и возможно, правильная теория на этот счет до сих пор даже не предложена.
Основные выводы на которых строится гипотеза о Тепловой смерти Вселенной сделаны на основе теории, которая хорошо работает для таких систем как идеальный газ, также в
этой гипотезе предполагается, что все виды энергии в конце концов перейдут в тепловую, и что наша Вселенная – это замкнутая система. В то же время наша Вселенная
скорее всего не так проста, чтобы её можно было описать на основе модели идеального газа, в частности её составные части притягиваются гравитационными силами, в
отличие от молекул идеального газа, которые в некотором приближении не взаимодействуют. Также нет никакой уверенности, что вся энергия во Вселенной должна перейти
именно в тепловую. Да и на счет того, что наша Вселенная является замкнутой системой в последнее время у некоторых ученых стали появляться сомнения. Таким образом,
подведем итог. В этой статье мы немного поговорили об энтропии, узнали, что она характеризует и как себя ведет в замкнутых термодинамических системах. Также
познакомились с одной из гипотез о том, каким будет конечное состояние Вселенной. И на основе этих сведений придумали шуточное оправдание человеческой лени, которое
конечно не нужно принимать слишком близко к сердцу, не стоит им также слишком часто пользоваться, а можно просто когда-нибудь с очень умным видом удачно пошутить."""
textBase = Text(textBase)
if __name__  == "__main__":
    textcheck = """В этой статье приведем небольшую, с одной стороны шутливую, но с другой стороны полностью научную теорию с помощью которой можно оправдать себя в те моменты, когда над
Вами взяла верх лень. Дело в том, что в физике существует такая термодинамическая величина как энтропия. Её научное значение определяет меру необратимого рассеивания
энергии. В других случаях она же может определять вероятность осуществления какого-либо макроскопического состояния."""
    textcheck = Text(textcheck)
    plag = Plagiat (textBase,textcheck)
    print (textcheck.tokenize(textcheck.text))
    plag.result (textBase.tokenize(textBase.text), textcheck.tokenize(textcheck.text))
    stih = " Посадил дед репку. Выросла репка большая."
    stih = Text(stih)
    plag = Plagiat (textBase,stih)
    print (stih.tokenize(stih.text))
    plag.result (textBase.tokenize(textBase.text), stih.tokenize(stih.text))
    stih = " Смеркалось?"
    stih = Text(stih)
    plag = Plagiat (textBase,stih)
    print (stih.tokenize(stih.text))
    plag.result (textBase.tokenize(textBase.text), stih.tokenize(stih.text))
    stih = "Метель ей пела песенку - Спи елочка , бай бай!"
    stih = Text(stih)
    plag = Plagiat (textBase,stih)
    print (stih.tokenize(stih.text))
    plag.result (textBase.tokenize(textBase.text), stih.tokenize(stih.text))
