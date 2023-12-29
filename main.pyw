import sys,pyperclip,keyboard,pyautogui,time,webbrowser
from googletrans import Translator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel
from PyQt5.QtCore import pyqtSlot,Qt
from plyer import notification

translator = Translator()
dictionary = {"q":"й","w":"ц","e":"у","r":"к","t":"е","y":"н","u":"г","i":"ш","o":"щ","p":"з","[":"х","]":"ї","a":"ф","s":"і","d":"в","f":"а","g":"п","h":"р","j":"о","k":"л","l":"д",";":"ж","'":"є","z":"я","x":"ч","c":"с","v":"м","b":"и","n":"т","m":"ь",",":"б",".":"ю"," ":" ","?":"."}

class App(QWidget):

    def __init__(self):
        super().__init__()
        x,y = pyautogui.position()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, pyautogui.size()[0], pyautogui.size()[1])
        translate = QPushButton('translate', self)
        translate.setStyleSheet('''
            background-color: black;color: white;border-radius: 10px;padding: 8px 10px;
            ''')
        transliterate = QPushButton('transliterate', self)
        transliterate.setStyleSheet('''
            background-color: black;color: white;border-radius: 10px;padding: 8px 10px;
            ''')
        search = QPushButton('search', self)
        search.setStyleSheet('''
            background-color: black;color: white;border-radius: 10px;padding: 8px 10px;
            ''')
        self.label = QLabel('',self)
        
        translate.move(x,y)
        transliterate.move(x,y+30)
        search.move(x,y+60)
        translate.clicked.connect(self.on_click1)
        transliterate.clicked.connect(self.on_click2)
        search.clicked.connect(self.on_click3)
        self.show()
        keyboard.send("alt+shift+tab")
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            exit()

    @pyqtSlot()
    def on_click1(self):
        text = pyperclip.paste()
        src_lang = translator.detect(text).lang
        keyboard.send("alt+tab")
        keyboard.write(translator.translate(text, src = src_lang, dest='uk' if src_lang == 'en' else 'en').text)
        notification.notify(title = "Keyboard-Switcher",message = text)
        # self.label.setText(translator.translate(text, src = src_lang, dest='uk' if src_lang == 'en' else 'en').text)
        exit()
    def on_click2(self):
        text = pyperclip.paste()
        keyboard.send("alt+tab")
        try:transliterated = "".join([dictionary[i] for i in text])
        except:transliterated = "".join([[k for k, v in dictionary.items() if v == i][0] for i in text])
        time.sleep(0.2)
        keyboard.write(transliterated)
        exit()
    def on_click3(self):
        webbrowser.open_new_tab(f"https://www.google.com/search?q={pyperclip.paste()}")
        exit() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec()
