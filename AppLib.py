import sqlite3
from PySide6 import QtCore, QtWidgets, QtGui
from tkinter import messagebox

class HWDPROC(QtWidgets.QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.__initUI()
        pass
        
    def __initUI(self) -> None:
        
        image = QtGui.QPixmap('icon.ico')
        image = image.scaledToWidth(100)
        imageLabel = QtWidgets.QLabel("", self)
        imageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        imageLabel.setPixmap(image)
        
        label_1 = QtWidgets.QLabel("Ник на osu!Bancho", self)
        self.__entry_name = QtWidgets.QLineEdit(self)
        
        label_2 = QtWidgets.QLabel("Ссылка на ваш osu! профиль", self)
        self.__entry_link = QtWidgets.QLineEdit(self)
        
        label_3 = QtWidgets.QLabel("Ваш дискорд-тэг", self)
        self.__entry_discord = QtWidgets.QLineEdit(self, "Необходимо для связи с вами")
        
        label_4 = QtWidgets.QLabel("Выберите в каком турнире хотите участвовать.")
        self.__combobox_1 = QtWidgets.QComboBox(self)
        self.__combobox_1.addItem("Osu! World Cup 2024")
        self.__combobox_1.addItem("Osu! Australia Cup 2024")
        self.__combobox_1.addItem("Osu! Russia Cup 2024")
        
        button_1 = QtWidgets.QPushButton("Отправить", self)
        button_1.clicked.connect(self.__callback_1)
        
        button_2 = QtWidgets.QPushButton("Очистить форму.", self)
        button_2.clicked.connect(self.__callback_2)
        
        layout = QtWidgets.QGridLayout()
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(5)
        
        layout.addWidget(imageLabel, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label_1, 1, 0, 1, 2)
        layout.addWidget(self.__entry_name, 2, 0, 1, 2)
        
        layout.addWidget(label_2, 3, 0, 1, 2)
        layout.addWidget(self.__entry_link, 4, 0, 1, 2)
        
        layout.addWidget(label_3, 5, 0, 1, 2)
        layout.addWidget(self.__entry_discord, 6, 0, 1, 2)
        
        layout.addWidget(label_4, 7, 0, 1, 2)
        layout.addWidget(self.__combobox_1, 8, 0, 1, 2)
        
        layout.addWidget(button_1, 9, 0, 1, 1)
        layout.addWidget(button_2, 9, 1, 1, 1)
        
        self.setLayout(layout)
        self.setFixedSize(layout.sizeHint())
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setWindowTitle("Регистрация")
        self.show()
        pass
    
    def __callback_1(self) -> None:
        self.sendToDB(self.__entry_name.text(), self.__entry_link.text(), self.__entry_discord.text(), self.__combobox_1.currentText())
        pass
    
    def __callback_2(self) -> None:
        self.__entry_name.clear()
        self.__entry_link.clear()
        self.__entry_discord.clear()
        pass
    
    def sendToDB(self, name: str, link: str, discord: str, tournament: str) -> None:
        if name == "" or link == "" or discord == "" or tournament == "":
            connection = sqlite3.connect("tournaments.db")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tournament (name, url, discord, tournament) VALUES (?, ?, ?, ?)", (name, link, discord, tournament))
            connection.commit()
            connection.close()
        else:
            messagebox.showwarning("Внимание!", "Одно из обязательных полей пустое")
        pass