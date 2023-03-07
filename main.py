import sys, configparser, os, re, string
from threading import local

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,                                                                                                                      
    QMetaObject, QObject, QPoint, QRect,                                                                                                                                                      
    QSize, QTime, QUrl, Qt, QFile)                                                                                                                                                                   
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,                                                                                                                         
    QFont, QFontDatabase, QGradient, QIcon,                                                                                                                                                   
    QImage, QKeySequence, QLinearGradient, QPainter,                                                                                                                                          
    QPalette, QPixmap, QRadialGradient, QTransform)                                                                                                                                           
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,                                                                                                             
    QLabel, QLineEdit, QPushButton, QScrollArea,                                                                                                                                              
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,                                                                                                                                        
    QWidget, QMainWindow, QFileDialog, QCheckBox, QMessageBox, QDialog, QTextEdit)

from design import Ui_Form
from dialog import Ui_Dialog

class DialogWindow(QDialog):
    def __init__(self, root_ui, root):
        super(DialogWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.main = root_ui
        self.root = root
        QFontDatabase.addApplicationFont("fonts/Cuprum.ttf")

        self.ui.buttonBox.accepted.connect(self.accept_data)
        self.ui.buttonBox.rejected.connect(self.reject_data)

    def accept_data(self):
        word = self.ui.textEdit.toPlainText()
        result = len(re.findall(r'\w+', word))
        if result != 1:
            self.close()
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Введите одно слово!')
            msgBox.setText('Вы ввели не одно слово!')
            msgBox.exec()
        else:
            self.close()
            text = str(self.ui.textEdit.toPlainText()).replace('\n', '')
            checkbox = QCheckBox(text)
            self.root.checkbox_arr.append(checkbox)
            with open('KeyList.txt', 'a', encoding='utf-8') as f:
                f.write(f'\n{text.lower()}')
                f.close()
            self.main.verticalLayout_3.addWidget(checkbox)
            self.ui.textEdit.setText('')
            

        
    def reject_data(self):
        self.close()



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("fonts/Cuprum.ttf")

        self.files_list = []
        self.total_stat = {}

        config = configparser.ConfigParser()
        config.read("config.ini")
        self.ui.label_2.setText(config["Path"]["path"])

        self.ui.pushButton.clicked.connect(self.getDirectory)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.pushButton_6.clicked.connect(self.scan)
        self.ui.pushButton_3.clicked.connect(self.addWord)
        self.ui.pushButton_4.clicked.connect(self.removeWord)
        self.ui.pushButton_5.clicked.connect(self.search)

        self.checkbox_arr = []
        f = open('KeyList.txt', 'r', encoding='utf-8')
        keylist = f.read()
        keylist = keylist.lower()
        keylist = keylist.split('\n')
        for i in keylist: 
            checkbox = QCheckBox(i)
            self.ui.verticalLayout_3.addWidget(checkbox)
            self.checkbox_arr.append(checkbox)
        f.close()
        

    def getDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        self.ui.label_4.setText(dirlist)

    def save(self):
        if len(self.ui.label_4.text()) > 0: 
            config = configparser.ConfigParser()
            config.read("config.ini")
            config.set("Path", "path", self.ui.label_4.text())
            config.write(open("config.ini", "w"))
            self.ui.label_4.setText('')
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.ui.label_2.setText(config["Path"]["path"])

    def scan(self):
        self.files_list = []

        while self.ui.verticalLayout_6.count():
            child = self.ui.verticalLayout_6.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        tree = os.walk(self.ui.label_2.text())
        for root, dirs, files in tree:
            for i in dirs:
                if i in names:
                    for j in os.listdir(i):
                        if j.endswith('.txt'):
                            self.files_list.append(os.path.abspath(f'{i}\{j}'))
        
        for i in self.files_list:
            label = QLabel(i)
            self.ui.verticalLayout_6.addWidget(label)


    def addWord(self):
        self.dialog = DialogWindow(self.ui, self)
        self.dialog.show()
        self.dialog.exec()

    def removeWord(self):
        f = open('KeyList.txt', encoding='utf-8')
        words = f.read()
        f.close()
        removed = open('KeyList.txt', 'w', encoding='utf-8')
        new_checkbox_arr = []
        count = 0
        for i in self.checkbox_arr:
            if i.isChecked() == False:
                new_checkbox_arr.append(i)
            elif i.isChecked() == True:
                count += 1
                words = words.replace(f'{i.text()}', '')
                re.sub('\n', '', words)
                if words.endswith('\n'):
                    words = words.rstrip(words[-1])
                self.ui.verticalLayout_3.removeWidget(i)
                i.deleteLater()
                
        self.checkbox_arr = new_checkbox_arr        
        removed.write(words)
        removed.close()

    def search(self):

        #clean area
        while self.ui.verticalLayout_5.count():
            child = self.ui.verticalLayout_5.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


        if self.files_list == []:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Ошибка')
            msgBox.setText('Начните сканирование на первой вкладке')
            msgBox.exec()
        else:
            #creating list of keywords
            words = []
            for i in self.checkbox_arr:
                if i.isChecked() == True:
                    words.append(i.text())

            for i in self.checkbox_arr:
                if i.isChecked() == True:
                    self.total_stat[i.text()]=0

            #reading files
            for file in self.files_list:
                f = open(file, 'r', encoding='utf-8')
                text = f.read()

                #remove punctuation
                text = text.lower()
                punc = string.punctuation + '—'
                text = "".join([ch for ch in text if ch not in punc])

                #replacing newlines with spaces and splitting text
                text = text.replace('\n', ' ')
                text = text.split()

                local_stat = {}
                i = 0
                for key in words:
                    for word in text:
                        if key == word:
                            i += 1
                    local_stat[key] = i
                    self.total_stat[key] = self.total_stat[key] + i
                    i = 0

                labelTitle = QLabel(f'Статистика для файла {file}:')
                self.ui.verticalLayout_5.addWidget(labelTitle)
                for key in words:
                    label = QLabel(f'{key}: {local_stat[key]}')
                    self.ui.verticalLayout_5.addWidget(label)
                verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)
                self.ui.verticalLayout_5.addItem(verticalSpacer)

            labelTitle = QLabel('Общая статистика:')
            self.ui.verticalLayout_5.addWidget(labelTitle)
            for key in words:
                label = QLabel(f'{key}: {self.total_stat[key]}')
                self.ui.verticalLayout_5.addWidget(label)

            

        
       

                
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())




