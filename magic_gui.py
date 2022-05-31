from pywhatkit import sendwhatmsg,text_to_handwriting,playonyt,search,info
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QComboBox,QTextEdit,QLineEdit
from PyQt6.QtGui import QIcon,QPixmap
from sys import argv
import datetime
from re import match

class BrilliantGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BrilliantGUI")
        self.setWindowIcon(QIcon("black panther.png"))
        self.setStyleSheet("background-color:black;")
        self.setFixedSize(600,600)

        self.widget_list = []

        self.options_selector = QComboBox(self)
        self.options_selector.addItems(["Send A Whatsapp Message","Convert Text To Handwriting","Perform A Google Search","Play A Video On Youtube","Get Information About A Particular Topic"])
        self.options_selector.setGeometry(100,50,400,50)
        self.options_selector.setStyleSheet("background-color:transparent;color:magenta;font-size:16px;font-weight:bold;border:1px groove cyan;border-radius:15px;")
        self.options_selector.currentIndexChanged.connect(self.connector)

        self.whatsapp_country_number = QComboBox(self)
        self.whatsapp_country_number.addItems(sorted(["+" + item[1] + " , " + item[0] for item in info_list if info_list.index(item)]))
        self.whatsapp_country_number.setGeometry(100,150,400,50)
        self.whatsapp_country_number.setStyleSheet("background-color:transparent;color:gold;font-size:16px;font-weight:bold;border:1px groove lightgreen;border-radius:15px;")
        self.whatsapp_country_number.currentIndexChanged.connect(self.sloap)
        self.widget_list.append(self.whatsapp_country_number)

        self.whatsapp_phone_number_destination = QLineEdit(self)
        self.whatsapp_phone_number_destination.setGeometry(100,230,400,50)
        self.whatsapp_phone_number_destination.setStyleSheet("background-color:transparent;color:green;font-size:16px;font-weight:bold;border:1px groove yellow;border-radius:15px;")
        self.whatsapp_phone_number_destination.setText(self.whatsapp_country_number.currentText().split(" , ")[0] + " ")
        self.widget_list.append(self.whatsapp_phone_number_destination)

        self.input = QTextEdit(self)
        self.input.setGeometry(100,300,400,150)
        self.input.setStyleSheet("background-color:rgba(255,70,150,0.3);color:grey;font-size:14px;font-weight:bold;border:0px groove red;border-radius:10px;")
        self.input.verticalScrollBar().setStyleSheet("QScrollBar:vertical {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")
        self.input.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")

        self.ok = QLabel(self)
        self.ok.setGeometry(520,350,50,50)
        self.ok.setPixmap(QPixmap("k.png").scaled(50,50))
        self.ok.setStyleSheet("background-color:white;color:white;")
        self.ok.mousePressEvent = self.verify

        self.output = QTextEdit(self)
        self.output.setGeometry(100,470,400,120)
        self.output.setStyleSheet("background-color:rgba(200,170,150,0.2);color:white;font-size:14px;font-weight:bold;border:0px groove red;border-radius:10px;")
        self.output.setReadOnly(True)
        self.output.verticalScrollBar().setStyleSheet("QScrollBar:vertical {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:vertical {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")
        self.output.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal {"              
            "    border: 0px solid transparent;"
            "    background:white;"
            "    width:5px;    "
            "    margin: 0px 0px 0px 0px;"
            "}"
            "QScrollBar::handle:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));"
            "    min-height: 0px;"
            "}"
            "QScrollBar::add-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0px;"
            "    subcontrol-position: bottom;"
            "    subcontrol-origin: margin;"
            "}"
            "QScrollBar::sub-line:horizontal {"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,"
            "    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));"
            "    height: 0 px;"
            "    subcontrol-position: top;"
            "    subcontrol-origin: margin;"
        "}")

        self.counter = 0

        self.show()

    def sloap(self):
        self.whatsapp_phone_number_destination.setText(self.whatsapp_country_number.currentText().split(" , ")[0] + " ")
    
    def connector(self):
        if self.options_selector.currentIndex() == 0:
            for item in self.widget_list:
                item.show()
            self.input.setGeometry(100,300,400,150)
            self.output.setGeometry(100,470,400,120)
            self.ok.setGeometry(520,350,50,50)
            self.setFixedSize(600,600)
            self.whatsapp_phone_number_destination.setText(self.whatsapp_country_number.currentText().split(" , ")[0] + " ")
            self.input.setPlaceholderText("Ex : +216 21536741")
        elif self.options_selector.currentIndex() == 1:
            for item in self.widget_list:
                item.hide()
            self.input.setGeometry(100,150,400,150)
            self.output.setGeometry(100,320,400,120)
            self.ok.setGeometry(520,200,50,50)
            self.setFixedSize(600,450)
            self.input.setPlaceholderText("Ex : The Prince Of Darkness And The King Of Light")
        elif self.options_selector.currentIndex() == 2:
            for item in self.widget_list:
                item.hide()
            self.input.setGeometry(100,150,400,150)
            self.output.setGeometry(100,320,400,120)
            self.ok.setGeometry(520,200,50,50)
            self.setFixedSize(600,450)
            self.input.setPlaceholderText("Ex : Nikola Tesla")
        elif self.options_selector.currentIndex() == 3:
            for item in self.widget_list:
                item.hide()
            self.input.setGeometry(100,150,400,150)
            self.output.setGeometry(100,320,400,120)
            self.ok.setGeometry(520,200,50,50)
            self.setFixedSize(600,450)
            self.input.setPlaceholderText("Ex : Starboy The Weeknd\n(OR)\nhttps://www.youtube.com/watch?v=L4W0GP8xNUE&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg")
        elif self.options_selector.currentIndex() == 4:
            for item in self.widget_list:
                item.hide()
            self.input.setGeometry(100,150,400,150)
            self.output.setGeometry(100,320,400,120)
            self.ok.setGeometry(520,200,50,50)
            self.setFixedSize(600,450)
            self.input.setPlaceholderText("Ex : The Universe Expansion")

    def verify(self,e):
        try:
            if self.options_selector.currentIndex() == 0:
                if not match(r"(?=.{2,11})\+\d{1,3} \d+",self.whatsapp_phone_number_destination.text()):
                    ...
                elif not self.input.toPlainText():
                    ...
                else:
                    sendwhatmsg("+21628056362","hello friend",*(int(str(datetime.datetime.now())[11:].split(":")[0]),int(str(datetime.datetime.now())[11:].split(":")[1]) + 1))
                    self.output.setText("Done...")
            elif self.options_selector.currentIndex() == 1:
                if not self.input.toPlainText():
                    ...
                else:
                    text_to_handwriting(self.input.toPlainText(),f"magic{self.counter + 1}.png")
                    self.output.setText("Done...")
                    self.counter += 1
            elif self.options_selector.currentIndex() == 2:
                if not self.input.toPlainText():
                    ...
                else:
                    self.output.setText(search(self.input.toPlainText()))
            elif self.options_selector.currentIndex() == 3:
                if not self.input.toPlainText():
                    ...
                else:
                    playonyt(self.input.toPlainText())
                    self.output.setText("Done...")
            elif self.options_selector.currentIndex() == 4:
                if not self.input.toPlainText():
                    ...
                else:
                    self.output.setText(info(self.input.toPlainText(),return_value = True))
        except Exception as e:
            self.output.setText(str(e))

if __name__ == "__main__":
    countries_codes_file = open("country_codes.txt")
    info_list = [(item.split(" : ")[0],item.split(" : ")[1].replace("\n","")) for item in countries_codes_file if item != 'COUNTRY CODE\n']
    application = QApplication(argv)
    brilliant_gui = BrilliantGUI()
    application.exec()
    countries_codes_file.close()