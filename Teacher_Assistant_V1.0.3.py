#  First project with PyQt
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
import webbrowser
import os


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.esquerda = 100
        self.topo = 80
        self.largura = 800
        self.altura = 620
        self.titulo = 'Teacher Assistant Planet School'

        self.logo = QLabel(self)
        self.logo.resize(400, 90)
        self.logo.move(585, 485)
        self.logo.setPixmap(QtGui.QPixmap('LOGO.jpg'))

        self.label_mogi = QLabel(self)
        self.label_mogi.setText('Salas Mogi')
        self.label_mogi.move(60, 20)
        self.label_mogi.setStyleSheet('QLabel {font:bold;font-size:22px; color:white}')
        self.label_mogi.resize(150, 30)
        self.label_mogi.setFont(QFont('Book Antiqua', 10))

        australia = QPushButton('Australia', self)
        australia.resize(150, 30)
        australia.move(40, 55)
        australia.setStyleSheet('QPushButton {font-size: 17px; '
                                'border: 2px solid #8f8f91;'
                                'border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        australia.setFont(QFont('Book Antiqua', 10))
        australia.clicked.connect(self.australia)

        fiji = QPushButton('Fiji Island', self)
        fiji.resize(150, 30)
        fiji.move(40, 90)
        fiji.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        fiji.setFont(QFont('Book Antiqua', 10))
        fiji.clicked.connect(self.fiji)

        canada = QPushButton('Canada', self)
        canada.resize(150, 30)
        canada.move(40, 125)
        canada.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        canada.setFont(QFont('Book Antiqua', 10))
        canada.clicked.connect(self.canada)

        ireland = QPushButton('Ireland', self)
        ireland.resize(150,30)
        ireland.move(40, 160)
        ireland.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        ireland.setFont(QFont('Book Antiqua', 10))
        ireland.clicked.connect(self.ireland)

        jamaica = QPushButton('Jamaica', self)
        jamaica.resize(150,30)
        jamaica.move(40, 195)
        jamaica.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        jamaica.setFont(QFont('Book Antiqua', 10))
        jamaica.clicked.connect(self.jamaica)

        malta = QPushButton('Malta', self)
        malta.resize(150,30)
        malta.move(40,230)
        malta.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        malta.setFont(QFont('Book Antiqua', 10))
        malta.clicked.connect(self.malta)

        nzealand = QPushButton('New Zealand', self)
        nzealand.resize(150,30)
        nzealand.move(40, 265)
        nzealand.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        nzealand.setFont(QFont('Book Antiqua', 10))
        nzealand.clicked.connect(self.nzealand)

        norway = QPushButton('Norway', self)
        norway.resize(150, 30)
        norway.move(40, 300)
        norway.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        norway.setFont(QFont('Book Antiqua', 10))
        norway.clicked.connect(self.norway)

        scotland = QPushButton('Scotland', self)
        scotland.resize(150, 30)
        scotland.move(40, 335)
        scotland.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        scotland.setFont(QFont('Book Antiqua', 10))
        scotland.clicked.connect(self.scotland)

        safrica = QPushButton('South Africa', self)
        safrica.resize(150, 30)
        safrica.move(40, 370)
        safrica.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        safrica.setFont(QFont('Book Antiqua', 10))
        safrica.clicked.connect(self.safrica)

        unitedk = QPushButton('United Kingdom', self)
        unitedk.resize(150,30)
        unitedk.move(40, 405)
        unitedk.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        unitedk.setFont(QFont('Book Antiqua', 10))
        unitedk.clicked.connect(self.unitedk)

        uniteds = QPushButton('United States', self)
        uniteds.resize(150, 30)
        uniteds.move(40, 440)
        uniteds.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        uniteds.setFont(QFont('Book Antiqua', 10))
        uniteds.clicked.connect(self.uniteds)

        self.suzano = QLabel(self)
        self.suzano.setText('Salas Suzano')
        self.suzano.resize(150, 30)
        self.suzano.move(50, 475)
        self.suzano.setStyleSheet('QLabel {font:bold;font-size:22px; color:white}')
        self.suzano.setFont(QFont('Book Antiqua', 10))

        philippines = QPushButton('Philippines', self)
        philippines.resize(150, 30)
        philippines.move(40, 510)
        philippines.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        philippines.setFont(QFont('Book Antiqua', 10))
        philippines.clicked.connect(self.philippines)

        wales = QPushButton('Wales', self)
        wales.resize(150, 30)
        wales.move(40, 545)
        wales.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        wales.setFont(QFont('Book Antiqua', 10))
        wales.clicked.connect(self.wales)

        bahamas = QPushButton('Bahamas', self)
        bahamas.resize(150, 30)
        bahamas.move(40, 580)
        bahamas.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        bahamas.setFont(QFont('Book Antiqua', 10))
        bahamas.clicked.connect(self.bahamas)

        self.anotacoes = QLabel(self)
        self.anotacoes.resize(150, 30)
        self.anotacoes.move(340, 20)
        self.anotacoes.setText('Anotações')
        self.anotacoes.setStyleSheet('QLabel{font:bold; font-size:22px; color:white}')
        self.anotacoes.setFont(QFont('Book Antiqua', 10))

        notes = open('Notes.txt', 'r')
        notes = notes.read()

        self.textbox = QTextEdit(self)
        self.textbox.resize(350,520)
        self.textbox.move(220, 55)
        self.textbox.setStyleSheet('background-color:white')
        self.textbox.setText(notes)

        salvar = QPushButton('Salvar', self)
        salvar.resize(150,30)
        salvar.move(320, 580)
        salvar.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        salvar.setFont(QFont('Book Antiqua', 10))
        salvar.clicked.connect(self.salvar)

        self.livros = QLabel(self)
        self.livros.setText('Livros')
        self.livros.move(650, 20)
        self.livros.resize(150, 30)
        self.livros.setStyleSheet('QLabel {font:bold; font-size:22px; color:white}')
        self.livros.setFont(QFont('Book Antiqua', 10))

        l12 = QPushButton('Livro 1/2', self)
        l12.resize(150,30)
        l12.move(610, 55)
        l12.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l12.setFont(QFont('Book Antiqua', 10))
        l12.clicked.connect(self.livro1)

        l34 = QPushButton('Livro 3/4', self)
        l34.resize(150, 30)
        l34.move(610, 90)
        l34.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l34.setFont(QFont('Book Antiqua', 10))
        l34.clicked.connect(self.livro3)

        l56 = QPushButton('Livro 5/6', self)
        l56.resize(150, 30)
        l56.move(610, 125)
        l56.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l56.setFont(QFont('Book Antiqua', 10))
        l56.clicked.connect(self.livro5)

        l78 = QPushButton('Livro 7/8', self)
        l78.resize(150, 30)
        l78.move(610, 160)
        l78.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l78.setFont(QFont('Book Antiqua', 10))
        l78.clicked.connect(self.livro7)

        l910 = QPushButton('Livro 9/10', self)
        l910.resize(150, 30)
        l910.move(610, 195)
        l910.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l910.setFont(QFont('Book Antiqua', 10))
        l910.clicked.connect(self.livro9)

        l1112 = QPushButton('Livro 11/12', self)
        l1112.resize(150, 30)
        l1112.move(610, 230)
        l1112.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        l1112.setFont(QFont('Book Antiqua', 10))
        l1112.clicked.connect(self.livro11)

        slides = QPushButton('Slides', self)
        slides.resize(150, 30)
        slides.move(610, 265)
        slides.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        slides.setFont(QFont('Book Antiqua', 10))
        slides.clicked.connect(self.slides)

        self.sistemas = QLabel(self)
        self.sistemas.resize(150, 30)
        self.sistemas.move(640, 305)
        self.sistemas.setText('Sistemas')
        self.sistemas.setStyleSheet('QLabel {font:bold; font-size:22px; color:white}')
        self.sistemas.setFont(QFont('Book Antiqua', 10))

        visao = QPushButton('Visão', self)
        visao.resize(150, 30)
        visao.move(610, 340)
        visao.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        visao.setFont(QFont('Book Antiqua', 10))
        visao.clicked.connect(self.visao)

        planilhas = QPushButton('Planilhas Google', self)
        planilhas.resize(150, 30)
        planilhas.move(610, 375)
        #planilhas.setStyleSheet('QPushButton {background-color:#ced0ff; font-size:17px; border-radius: 15px}')
        planilhas.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        planilhas.setFont(QFont('Book Antiqua', 10))
        planilhas.clicked.connect(self.planilhas)


        drive = QPushButton('Google Drive', self)
        drive.resize(150, 30)
        drive.move(610, 410)
        #drive.setStyleSheet('QPushButton {background-color:#597b6d; font-size:17px}')
        drive.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #ced0ff, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #ced0d1;}QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #dadbde, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        drive.setFont(QFont('Book Antiqua', 10))
        drive.clicked.connect(self.drive)

        whats = QPushButton('Whatsapp web', self)
        whats.resize(150, 30)
        whats.move(610, 445)
        #whats.setStyleSheet('QPushButton {background-color:#ced0ff; font-size:17px}')
        whats.setStyleSheet('QPushButton {font-size: 17px; border: 2px solid #8f8f91;border-radius: 15px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #597b6d, stop: 1 #dadbde);min-width: 80px;}QPushButton:hover {background-color: #556d6a;} QPushButton:pressed {background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0,stop: 0 #505c59, stop: 1 #f6f7fa);}QPushButton:flat {border: none; /* no border for a flat push button */}QPushButton:default {border-color: navy; /* make the default button prominent */}')
        whats.setFont(QFont('Book Antiqua', 10))#ced0d1
        whats.clicked.connect(self.whatsapp)

        self.assinatura = QLabel(self)
        self.assinatura.setText('Developed by Teacher Johnny')
        self.assinatura.setStyleSheet('QLabel {font:bold; font-size:18px; color:white}')
        self.assinatura.setFont(QFont('Bradley Hand ITC'))
        self.assinatura.resize(250,30)
        self.assinatura.move(550,580)

        self.Carregar_Janela()

    def Carregar_Janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowIcon(QtGui.QIcon('LOGO.jpg'))
        self.setWindowTitle(self.titulo)
        self.setStyleSheet('background-color:#00223c')
        self.setWindowIcon(QtGui.QIcon('logo_corte_Nrs_icon.ico'))
        self.show()

    def australia(self):
        webbrowser.open_new_tab('https://meet.google.com/cdh-dfjn-ubx')

    def fiji(self):
        webbrowser.open_new_tab('https://meet.google.com/sqr-wtpm-def')

    def canada(self):
        webbrowser.open_new_tab('https://meet.google.com/bte-xpkq-srb')

    def ireland(self):
        webbrowser.open_new_tab('https://meet.google.com/coo-nqfq-xcq')

    def jamaica(self):
        webbrowser.open_new_tab('https://meet.google.com/knc-jxer-pog')

    def malta(self):
        webbrowser.open_new_tab('https://meet.google.com/qgm-hspa-kzv')

    def nzealand(self):
        webbrowser.open_new_tab('https://meet.google.com/edg-nvby-scq')

    def norway(self):
        webbrowser.open_new_tab('https://meet.google.com/stn-ngdx-rmc')

    def scotland(self):
        webbrowser.open_new_tab('https://meet.google.com/xuz-kfgk-hut')

    def safrica(self):
        webbrowser.open_new_tab('https://meet.google.com/iiw-ikjq-hne')

    def unitedk(self):
        webbrowser.open_new_tab('https://meet.google.com/fkr-iumu-tze')

    def uniteds(self):
        webbrowser.open_new_tab('https://meet.google.com/okr-ytkg-vdx')

    def philippines(self):
        webbrowser.open_new_tab('https://meet.google.com/zvz-azds-nzs')

    def wales(self):
        webbrowser.open_new_tab('https://meet.google.com/tdc-opks-uis')

    def bahamas(self):
        webbrowser.open_new_tab('https://meet.google.com/pnj-xtha-jrc')

    def livro1(self):
        os.startfile('livro-1-2.pdf')

    def livro3(self):
        os.startfile('livro-3-4.pdf')

    def livro5(self):
        os.startfile('livro-5-6.pdf')

    def livro7(self):
        os.startfile('livro-7-8.pdf')

    def livro9(self):
        os.startfile('livro-9-10.pdf')

    def livro11(self):
        os.startfile('livro-11-12.pdf')

    def slides(self):
        os.startfile('slides.pdf')

    def visao(self):
        webbrowser.open_new_tab('https://visaoschool.com.br/login')

    def planilhas(self):
        webbrowser.open_new_tab('https://docs.google.com/spreadsheets/u/0/')

    def drive(self):
        webbrowser.open_new_tab('https://drive.google.com/drive/u/4/shared-with-me')

    def whatsapp(self):
        webbrowser.open_new_tab('https://web.whatsapp.com/')

    def salvar(self):
        notes = open('Notes.txt', 'w')
        text = self.textbox.toPlainText()
        notes.write(text)

app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec_())
