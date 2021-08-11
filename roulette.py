import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

# ----------------Стили кнопок-----------------------------------------------------------
style_12 = 'background-color:#5f5b32; color:white; font-size: 20px;'
style_red = 'background-color:#d71a1a; color:white; font-size: 20px;'
style_black = 'background-color:#272020; color:white; font-size: 20px;'
style_chips = 'background-color:#272020;'


# ---------------------------------------------------------------------------


# --- ---
class roulette(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройки окна
        self.setFixedSize(1200, 900)
        self.setWindowTitle('Roulette by Molodoy Python')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        # Фон окна
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("design/fon.jpg"))
        self.image.resize(1200, 900)
        # Колесо
        self.wheel = QLabel(self)
        self.wheel.setPixmap(QPixmap("design/wheel.png"))
        self.wheel.resize(600, 600)
        self.wheel.move(280, 150)
        # Фон Стола
        self.fon_stola = QLabel(self)
        self.fon_stola.setPixmap(QPixmap("design/fon-stola.jpg"))
        self.fon_stola.resize(1200, 400)
        self.fon_stola.move(0, 450)
        self.fon_stola.setStyleSheet('border: 7px solid #1a1919;')

        # ---------------- Доска--------------------------------
        self.zero = QPushButton('0', self)
        self.zero.setGeometry(50, 460, 50, 150)
        self.zero.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.zero.setStyleSheet('color:white; font-size: 30px; background-color:#b5aa28;')
        self.zero.clicked.connect(self.push_zero)

        self.one_st_12 = QPushButton('1st - 12', self)
        self.one_st_12.setGeometry(100, 610, 320, 50)
        self.one_st_12.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.one_st_12.setStyleSheet(style_12)
        self.one_st_12.clicked.connect(self.push_one_st_12)

        self.two_nd_12 = QPushButton('2nd - 12', self)
        self.two_nd_12.setGeometry(420, 610, 320, 50)
        self.two_nd_12.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.two_nd_12.setStyleSheet(style_12)
        self.two_nd_12.clicked.connect(self.push_two_nd_12)

        self.three_rd_12 = QPushButton('3rd - 12', self)
        self.three_rd_12.setGeometry(740, 610, 320, 50)
        self.three_rd_12.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.three_rd_12.setStyleSheet(style_12)
        self.three_rd_12.clicked.connect(self.push_three_rd_12)

        self.one_18 = QPushButton('1 - 18', self)
        self.one_18.setGeometry(100, 660, 160, 50)
        self.one_18.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.one_18.setStyleSheet(style_12)
        self.one_18.clicked.connect(self.push_one_18)

        self.even = QPushButton('EVEN', self)
        self.even.setGeometry(260, 660, 160, 50)
        self.even.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.even.setStyleSheet(style_12)
        self.even.clicked.connect(self.push_even)

        self.red = QPushButton('RED', self)
        self.red.setGeometry(420, 660, 160, 50)
        self.red.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.red.setStyleSheet(style_red)
        self.red.clicked.connect(self.push_red)

        self.black = QPushButton('BLACK', self)
        self.black.setGeometry(580, 660, 160, 50)
        self.black.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.black.setStyleSheet(style_black)
        self.black.clicked.connect(self.push_black)

        self.odd = QPushButton('ODD', self)
        self.odd.setGeometry(740, 660, 160, 50)
        self.odd.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.odd.setStyleSheet(style_12)
        self.odd.clicked.connect(self.push_odd)

        self.nineteen_36 = QPushButton('19 - 36', self)
        self.nineteen_36.setGeometry(900, 660, 160, 50)
        self.nineteen_36.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.nineteen_36.setStyleSheet(style_12)
        self.nineteen_36.clicked.connect(self.push_nineteen_36)

        # Первая линия чисел
        self.btn_1 = QPushButton('1', self)
        self.btn_1.setGeometry(100, 560, 80, 50)
        self.btn_1.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_1.setStyleSheet(style_red)
        self.btn_1.clicked.connect(self.push_btn_1)

        self.btn_4 = QPushButton('4', self)
        self.btn_4.setGeometry(180, 560, 80, 50)
        self.btn_4.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_4.setStyleSheet(style_black)
        self.btn_4.clicked.connect(self.push_btn_4)

        self.btn_7 = QPushButton('7', self)
        self.btn_7.setGeometry(260, 560, 80, 50)
        self.btn_7.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_7.setStyleSheet(style_red)
        self.btn_7.clicked.connect(self.push_btn_7)

        self.btn_10 = QPushButton('10', self)
        self.btn_10.setGeometry(340, 560, 80, 50)
        self.btn_10.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_10.setStyleSheet(style_black)
        self.btn_10.clicked.connect(self.push_btn_10)

        self.btn_13 = QPushButton('13', self)
        self.btn_13.setGeometry(420, 560, 80, 50)
        self.btn_13.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_13.setStyleSheet(style_black)
        self.btn_13.clicked.connect(self.push_btn_13)

        self.btn_16 = QPushButton('16', self)
        self.btn_16.setGeometry(500, 560, 80, 50)
        self.btn_16.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_16.setStyleSheet(style_red)
        self.btn_16.clicked.connect(self.push_btn_16)

        self.btn_19 = QPushButton('19', self)
        self.btn_19.setGeometry(580, 560, 80, 50)
        self.btn_19.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_19.setStyleSheet(style_red)
        self.btn_19.clicked.connect(self.push_btn_19)

        self.btn_22 = QPushButton('22', self)
        self.btn_22.setGeometry(660, 560, 80, 50)
        self.btn_22.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_22.setStyleSheet(style_black)
        self.btn_22.clicked.connect(self.push_btn_22)

        self.btn_25 = QPushButton('25', self)
        self.btn_25.setGeometry(740, 560, 80, 50)
        self.btn_25.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_25.setStyleSheet(style_red)
        self.btn_25.clicked.connect(self.push_btn_25)

        self.btn_28 = QPushButton('28', self)
        self.btn_28.setGeometry(820, 560, 80, 50)
        self.btn_28.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_28.setStyleSheet(style_black)
        self.btn_28.clicked.connect(self.push_btn_28)

        self.btn_31 = QPushButton('31', self)
        self.btn_31.setGeometry(900, 560, 80, 50)
        self.btn_31.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_31.setStyleSheet(style_black)
        self.btn_31.clicked.connect(self.push_btn_31)

        self.btn_34 = QPushButton('34', self)
        self.btn_34.setGeometry(980, 560, 80, 50)
        self.btn_34.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_34.setStyleSheet(style_red)
        self.btn_34.clicked.connect(self.push_btn_34)

        # Вторая линия чисел
        self.btn_2 = QPushButton('2', self)
        self.btn_2.setGeometry(100, 510, 80, 50)
        self.btn_2.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_2.setStyleSheet(style_black)
        self.btn_2.clicked.connect(self.push_btn_2)

        self.btn_5 = QPushButton('5', self)
        self.btn_5.setGeometry(180, 510, 80, 50)
        self.btn_5.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_5.setStyleSheet(style_red)
        self.btn_5.clicked.connect(self.push_btn_5)

        self.btn_8 = QPushButton('8', self)
        self.btn_8.setGeometry(260, 510, 80, 50)
        self.btn_8.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_8.setStyleSheet(style_black)
        self.btn_8.clicked.connect(self.push_btn_8)

        self.btn_11 = QPushButton('11', self)
        self.btn_11.setGeometry(340, 510, 80, 50)
        self.btn_11.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_11.setStyleSheet(style_black)
        self.btn_11.clicked.connect(self.push_btn_11)

        self.btn_14 = QPushButton('14', self)
        self.btn_14.setGeometry(420, 510, 80, 50)
        self.btn_14.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_14.setStyleSheet(style_red)
        self.btn_14.clicked.connect(self.push_btn_14)

        self.btn_17 = QPushButton('17', self)
        self.btn_17.setGeometry(500, 510, 80, 50)
        self.btn_17.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_17.setStyleSheet(style_black)
        self.btn_17.clicked.connect(self.push_btn_17)

        self.btn_20 = QPushButton('20', self)
        self.btn_20.setGeometry(580, 510, 80, 50)
        self.btn_20.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_20.setStyleSheet(style_black)
        self.btn_20.clicked.connect(self.push_btn_20)

        self.btn_23 = QPushButton('23', self)
        self.btn_23.setGeometry(660, 510, 80, 50)
        self.btn_23.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_23.setStyleSheet(style_red)
        self.btn_23.clicked.connect(self.push_btn_23)

        self.btn_26 = QPushButton('26', self)
        self.btn_26.setGeometry(740, 510, 80, 50)
        self.btn_26.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_26.setStyleSheet(style_black)
        self.btn_26.clicked.connect(self.push_btn_26)

        self.btn_29 = QPushButton('29', self)
        self.btn_29.setGeometry(820, 510, 80, 50)
        self.btn_29.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_29.setStyleSheet(style_black)
        self.btn_29.clicked.connect(self.push_btn_29)

        self.btn_32 = QPushButton('32', self)
        self.btn_32.setGeometry(900, 510, 80, 50)
        self.btn_32.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_32.setStyleSheet(style_red)
        self.btn_32.clicked.connect(self.push_btn_32)

        self.btn_35 = QPushButton('35', self)
        self.btn_35.setGeometry(980, 510, 80, 50)
        self.btn_35.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_35.setStyleSheet(style_black)
        self.btn_35.clicked.connect(self.push_btn_35)

        # Третья линия чисел
        self.btn_3 = QPushButton('3', self)
        self.btn_3.setGeometry(100, 460, 80, 50)
        self.btn_3.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_3.setStyleSheet(style_red)
        self.btn_3.clicked.connect(self.push_btn_3)

        self.btn_6 = QPushButton('6', self)
        self.btn_6.setGeometry(180, 460, 80, 50)
        self.btn_6.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_6.setStyleSheet(style_black)
        self.btn_6.clicked.connect(self.push_btn_6)

        self.btn_9 = QPushButton('9', self)
        self.btn_9.setGeometry(260, 460, 80, 50)
        self.btn_9.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_9.setStyleSheet(style_red)
        self.btn_9.clicked.connect(self.push_btn_9)

        self.btn_12 = QPushButton('12', self)
        self.btn_12.setGeometry(340, 460, 80, 50)
        self.btn_12.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_12.setStyleSheet(style_red)
        self.btn_12.clicked.connect(self.push_btn_12)

        self.btn_15 = QPushButton('15', self)
        self.btn_15.setGeometry(420, 460, 80, 50)
        self.btn_15.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_15.setStyleSheet(style_black)
        self.btn_15.clicked.connect(self.push_btn_15)

        self.btn_18 = QPushButton('18', self)
        self.btn_18.setGeometry(500, 460, 80, 50)
        self.btn_18.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_18.setStyleSheet(style_red)
        self.btn_18.clicked.connect(self.push_btn_18)

        self.btn_21 = QPushButton('21', self)
        self.btn_21.setGeometry(580, 460, 80, 50)
        self.btn_21.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_21.setStyleSheet(style_red)
        self.btn_21.clicked.connect(self.push_btn_21)

        self.btn_24 = QPushButton('24', self)
        self.btn_24.setGeometry(660, 460, 80, 50)
        self.btn_24.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_24.setStyleSheet(style_black)
        self.btn_24.clicked.connect(self.push_btn_24)

        self.btn_27 = QPushButton('27', self)
        self.btn_27.setGeometry(740, 460, 80, 50)
        self.btn_27.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_27.setStyleSheet(style_red)
        self.btn_27.clicked.connect(self.push_btn_27)

        self.btn_30 = QPushButton('30', self)
        self.btn_30.setGeometry(820, 460, 80, 50)
        self.btn_30.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_30.setStyleSheet(style_red)
        self.btn_30.clicked.connect(self.push_btn_30)

        self.btn_33 = QPushButton('33', self)
        self.btn_33.setGeometry(900, 460, 80, 50)
        self.btn_33.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_33.setStyleSheet(style_black)
        self.btn_33.clicked.connect(self.push_btn_33)

        self.btn_36 = QPushButton('36', self)
        self.btn_36.setGeometry(980, 460, 80, 50)
        self.btn_36.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.btn_36.setStyleSheet(style_red)
        self.btn_36.clicked.connect(self.push_btn_36)

        # 2к1 в цонце линии
        self.two_to_one_3_36 = QPushButton('2:1', self)
        self.two_to_one_3_36.setGeometry(1060, 460, 90, 50)
        self.two_to_one_3_36.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.two_to_one_3_36.setStyleSheet(style_12)
        self.two_to_one_3_36.clicked.connect(self.push_two_to_one_3_36)

        self.two_to_one_2_35 = QPushButton('2:1', self)
        self.two_to_one_2_35.setGeometry(1060, 510, 90, 50)
        self.two_to_one_2_35.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.two_to_one_2_35.setStyleSheet(style_12)
        self.two_to_one_2_35.clicked.connect(self.push_two_to_one_2_35)

        self.two_to_one_1_34 = QPushButton('2:1', self)
        self.two_to_one_1_34.setGeometry(1060, 560, 90, 50)
        self.two_to_one_1_34.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.two_to_one_1_34.setStyleSheet(style_12)
        self.two_to_one_1_34.clicked.connect(self.push_two_to_one_1_34)


        # ---------------- Информация игрока--------------------------------
        self.bank_igroka = 100

        # Окно Cash
        self.cash_text = QLabel("Cash:", self)
        self.cash_text.setGeometry(180, 855, 180, 40)
        self.cash_text.setStyleSheet('border: 0px solid red; color:white; font-size: 20px')

        self.cash = QLabel(self)
        self.cash.setGeometry(240, 860, 180, 30)
        self.cash.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 15px')
        self.cash.setText(str(self.bank_igroka))

        # Окно Bet
        self.bet_text = QLabel("Bet:", self)
        self.bet_text.setGeometry(460, 855, 180, 40)
        self.bet_text.setStyleSheet('border: 0px solid red; color:white; font-size: 20px')

        self.bet = QLabel(self)
        self.bet.setGeometry(510, 860, 180, 30)
        self.bet.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 15px')

        # Окно Win
        self.win_text = QLabel("Win:", self)
        self.win_text.setGeometry(720, 855, 180, 40)
        self.win_text.setStyleSheet('border: 0px solid red; color:white; font-size: 20px')

        self.win = QLabel(self)
        self.win.setGeometry(780, 860, 180, 30)
        self.win.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 15px')

        # Окно Bank
        self.bank_info_text = QLabel("BANK", self)
        self.bank_info_text.setGeometry(1015, 300, 180, 40)
        self.bank_info_text.setStyleSheet('border: 0px solid red; color:white; font-size: 30px')
        self.bank_info_text.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))

        self.bank_info = QLabel(self)
        self.bank_info.setGeometry(990, 350, 140, 50)
        self.bank_info.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 20px')

        # Кнопка Spin
        self.spin = QPushButton('SPIN !', self)
        self.spin.setGeometry(860, 730, 200, 100)
        self.spin.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
        self.spin.setStyleSheet('background-color:#272020; color:white; font-size: 40px;')
        self.spin.clicked.connect(self.push_spin)

        # Окно Number
        self.number_text = QLabel("NUMBER", self)
        self.number_text.setGeometry(995, 50, 180, 40)
        self.number_text.setStyleSheet('border: 0px solid red; color:white; font-size: 30px')
        self.number_text.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))

        self.number_ramka = QLabel(self)
        self.number_ramka.setPixmap(QPixmap("design/rand_ramka.png"))
        self.number_ramka.setGeometry(950, 50, 50, 40)
        self.number_ramka.resize(230, 280)

        self.number = QLabel(self)
        self.number.setGeometry(1015, 135, 140, 100)
        self.number.setStyleSheet('border: 0px solid red; background-color:rgba(0, 0, 255, 0.0); color:white; font-size: 70px;')

        # Окно last bet
        self.last_bet_text = QLabel("LAST BET", self)
        self.last_bet_text.setGeometry(20, 80, 180, 40)
        self.last_bet_text.setStyleSheet('border: 0px solid red; color:white; font-size: 25px')
        self.last_bet_text.setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))

        self.last_bet = QLabel(self)
        self.last_bet.setGeometry(20, 135, 150, 250)
        self.last_bet.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 10px;')

        # Окно last Numbers
        self.last_numbers = QLabel(self)
        self.last_numbers.setGeometry(460, 20, 250, 70)
        self.last_numbers.setStyleSheet('border: 1px solid red; background-color:#171714; color:white; font-size: 20px;')

        self.last_numbers_triangle = QLabel(self)
        self.last_numbers_triangle.setPixmap(QPixmap("design/triangle.png"))
        self.last_numbers_triangle.setGeometry(435, 45, 50, 40)
        self.last_numbers_triangle.resize(80, 70)

        self.last_numbers_triangle = QLabel(self)
        self.last_numbers_triangle.setPixmap(QPixmap("design/triangle2.png"))
        self.last_numbers_triangle.setGeometry(435, 0, 50, 40)
        self.last_numbers_triangle.resize(60, 55)

        self.last_rand_ramka = QLabel(self)
        self.last_rand_ramka.setPixmap(QPixmap("design/last_rand_ramka.png"))
        self.last_rand_ramka.setGeometry(445, 5, 50, 40)
        self.last_rand_ramka.resize(290, 100)


        # ---------------- Ставки --------------------------------

        self.chip_5 = QPushButton(self)
        self.chip_5.setGeometry(100, 730, 100, 100)
        self.chip_5.setIcon(QtGui.QIcon("chip/chip_5.png"))
        self.chip_5.setIconSize(QSize(90, 90))
        self.chip_5.setStyleSheet(style_chips)
        self.chip_5.clicked.connect(self.push_chip_5)

        self.chip_10 = QPushButton(self)
        self.chip_10.setGeometry(200, 730, 100, 100)
        self.chip_10.setIcon(QtGui.QIcon("chip/chip_10.png"))
        self.chip_10.setIconSize(QSize(90, 90))
        self.chip_10.setStyleSheet(style_chips)
        self.chip_10.clicked.connect(self.push_chip_10)

        self.chip_20 = QPushButton(self)
        self.chip_20.setGeometry(300, 730, 100, 100)
        self.chip_20.setIcon(QtGui.QIcon("chip/chip_20.png"))
        self.chip_20.setIconSize(QSize(90, 90))
        self.chip_20.setStyleSheet(style_chips)
        self.chip_20.clicked.connect(self.push_chip_20)

        self.chip_50 = QPushButton(self)
        self.chip_50.setGeometry(400, 730, 100, 100)
        self.chip_50.setIcon(QtGui.QIcon("chip/chip_50.png"))
        self.chip_50.setIconSize(QSize(90, 90))
        self.chip_50.setStyleSheet(style_chips)
        self.chip_50.clicked.connect(self.push_chip_50)

        self.chip_100 = QPushButton(self)
        self.chip_100.setGeometry(500, 730, 100, 100)
        self.chip_100.setIcon(QtGui.QIcon("chip/chip_100.png"))
        self.chip_100.setIconSize(QSize(90, 90))
        self.chip_100.setStyleSheet(style_chips)
        self.chip_100.clicked.connect(self.push_chip_100)

    # ---------------- Делаем ставки --------------------------------
    def push_chip_5(self):
        if int(self.cash.text()) >= 5:
            self.bet.setText(str(eval(self.bet.text() + "+5")))
            self.cash.setText(str(eval(self.cash.text() + "-5")))
        elif int(self.cash.text()) <= 0:
            self.cash.setText(str('0'))

    def push_chip_10(self):
        if int(self.cash.text()) >= 10:
            self.bet.setText(str(eval(self.bet.text() + "+10")))
            self.cash.setText(str(eval(self.cash.text() + "-10")))
        elif int(self.cash.text()) <= 0:
            self.cash.setText(str('0'))

    def push_chip_20(self):
        if int(self.cash.text()) >= 20:
            self.bet.setText(str(eval(self.bet.text() + "+20")))
            self.cash.setText(str(eval(self.cash.text() + "-20")))
        elif int(self.cash.text()) <= 0:
            self.cash.setText(str('0'))

    def push_chip_50(self):
        if int(self.cash.text()) >= 50:
            self.bet.setText(str(eval(self.bet.text() + "+50")))
            self.cash.setText(str(eval(self.cash.text() + "-50")))
        elif int(self.cash.text()) <= 0:
            self.cash.setText(str('0'))

    def push_chip_100(self):
        if int(self.cash.text()) >= 100:
            self.bet.setText(str(eval(self.bet.text() + "+100")))
            self.cash.setText(str(eval(self.cash.text() + "-100")))
        elif int(self.cash.text()) <= 0:
            self.cash.setText(str('0'))

    # ---------------- Обработка ставки после выбора места на игровом поле --------------------------------
    # Список для вывода в Last Numbers
    last_numbers_list = []
    # Список для вывода в Last Bet
    history_list = []
    # Строки для подсчета выигрыша:
    win_all = ''
    all_bets = 0

    win_zero = ''
    win_one_st_12 = ''
    win_two_nd_12 = ''
    win_three_rd_12 = ''
    win_btn_1 = ''
    win_btn_2 = ''
    win_btn_3 = ''
    win_btn_4 = ''
    win_btn_5 = ''
    win_btn_6 = ''
    win_btn_7 = ''
    win_btn_8 = ''
    win_btn_9 = ''
    win_btn_10 = ''
    win_btn_11 = ''
    win_btn_12 = ''
    win_btn_13 = ''
    win_btn_14 = ''
    win_btn_15 = ''
    win_btn_16 = ''
    win_btn_17 = ''
    win_btn_18 = ''
    win_btn_19 = ''
    win_btn_20 = ''
    win_btn_21 = ''
    win_btn_22 = ''
    win_btn_23 = ''
    win_btn_24 = ''
    win_btn_25 = ''
    win_btn_26 = ''
    win_btn_27 = ''
    win_btn_28 = ''
    win_btn_29 = ''
    win_btn_30 = ''
    win_btn_31 = ''
    win_btn_32 = ''
    win_btn_33 = ''
    win_btn_34 = ''
    win_btn_35 = ''
    win_btn_36 = ''
    win_one_18 = ''
    win_nineteen_36 = ''
    win_even = ''
    win_red = ''
    win_black = ''
    win_odd = ''
    win_two_to_one_1_34 = ''
    win_two_to_one_2_35 = ''
    win_two_to_one_3_36 = ''

    def push_zero(self):
        self.win.setText('')  # Чистим окно с выигрышем в партии
        self.win_all = ''  # Обнуляем счетчик с общим выигрышем

        if self.bet.text() != '':  # Если ставка сделана
            self.history_list.append(f'Number: 0 | Bet: {self.bet.text()}')  # Добавить инф. о ставке в список
            self.last_bet.setText(str('\n'.join(self.history_list)))  # Добавить список со ставками в Лейбл Last Bet
            # Считаем выигрыш
            self.win_zero += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_zero += '+'
            # Считаем сделанные ставки
            self.all_bets += int(self.bet.text())
            # ----------------------------
            self.bank_info.setText(str(eval(self.bank_info.text() + '+' + self.bet.text())))  # Добавляем в окно банк
            self.bet.setText('')  # Чистим окно со ставками

    def push_one_st_12(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'1st 12 | Bet: {self.bet.text()}')
            self.last_bet.setText(str('\n'.join(self.history_list)))
            self.win_one_st_12 += str(eval(self.bet.text() + '*2' + '+' + self.bet.text()))
            self.win_one_st_12 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_two_nd_12(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'2nd 12 | Bet: {self.bet.text()}')
            self.last_bet.setText(str('\n'.join(self.history_list)))
            self.win_two_nd_12 += str(eval(self.bet.text() + '*2' + '+' + self.bet.text()))
            self.win_two_nd_12 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_three_rd_12(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'3rd 12 | Bet: {self.bet.text()}')
            self.last_bet.setText(str('\n'.join(self.history_list)))
            self.win_three_rd_12 += str(eval(self.bet.text() + '*2' + '+' + self.bet.text()))
            self.win_three_rd_12 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_1(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 1 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_1 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_1 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_2(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 2 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_2 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_2 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_3(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 3 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_3 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_3 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_4(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 4 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_4 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_4 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_5(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 5 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_5 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_5 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_6(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 6 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_6 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_6 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_7(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 7 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_7 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_7 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_8(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 8 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_8 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_8 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_9(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 9 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_9 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_9 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_10(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 10 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_10 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_10 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_11(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 11 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_11 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_11 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_12(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 12 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_12 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_12 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_13(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 13 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_13 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_13 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_14(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 10 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_14 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_14 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_15(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 15 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_15 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_15 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_16(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 16 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_16 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_16 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_17(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 17 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_17 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_17 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_18(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 18 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_18 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_18 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_19(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 19 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_19 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_19 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_20(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 20 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_20 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_20 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_21(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 21 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_21 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_21 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_22(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 22 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_22 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_22 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_23(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 23 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_23 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_23 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_24(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 24 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_24 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_24 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_25(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 25 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_25 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_25 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_26(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 26 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_26 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_26 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_27(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 27 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_27 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_27 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_28(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 28 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_28 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_28 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_29(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 29 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_29 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_29 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_30(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 30 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_30 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_30 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_31(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 31 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_31 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_31 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_32(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 32 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_32 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_32 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_33(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 33 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_33 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_33 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_34(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 34 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_34 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_34 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_35(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 30 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_35 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_35 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_btn_36(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 36 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_btn_36 += str(eval(self.bet.text() + '*36' + '+' + self.bet.text()))
            self.win_btn_36 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_one_18(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 1-18 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_one_18 += str(eval(self.bet.text() + '*2'))
            self.win_one_18 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_nineteen_36(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: 19-36 | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_nineteen_36 += str(eval(self.bet.text() + '*2'))
            self.win_nineteen_36 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_even(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: EVEN | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_even += str(eval(self.bet.text() + '*2'))
            self.win_even += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_red(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: RED | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_red += str(eval(self.bet.text() + '*2'))
            self.win_red += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_black(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: BLACK | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_black += str(eval(self.bet.text() + '*2'))
            self.win_black += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_odd(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: ODD | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_odd += str(eval(self.bet.text() + '*2'))
            self.win_odd += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_two_to_one_1_34(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: FIRST LINE | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_two_to_one_1_34 += str(eval(self.bet.text() + '*2'))
            self.win_two_to_one_1_34 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_two_to_one_2_35(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: SECOND LINE | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_two_to_one_2_35 += str(eval(self.bet.text() + '*2'))
            self.win_two_to_one_2_35 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')

    def push_two_to_one_3_36(self):
        self.win.setText('')
        self.win_all = ''

        if self.bet.text() != '':
            self.history_list.append(f'Number: THIRD LINE | Bet: {self.bet.text()}')
            self.last_bet.setText(
                str('\n'.join(self.history_list)))
            self.win_two_to_one_3_36 += str(eval(self.bet.text() + '*2'))
            self.win_two_to_one_3_36 += '+'
            self.all_bets += int(self.bet.text())
            self.bank_info.setText(
                str(eval(self.bank_info.text() + '+' + self.bet.text())))
            self.bet.setText('')



    # Запускаем колесо
    def push_spin(self):
        self.rand_number = random.randrange(0, 37)
        if self.bet.text() == '' and self.bank_info.text() == '':
            pass
        elif self.bank_info.text() != '':
            self.number.setText(str(self.rand_number))
            # Добавление в список и окно последних чисел рулетки
            self.last_numbers_list.append(self.rand_number)
            self.last_numbers_list.reverse()
            self.last_numbers.setText(str(self.last_numbers_list)[1:-1])

        #  Если выпал ноль
        if self.rand_number == 0:
            self.win_all += self.win_zero

        #  Если выпал 1st 12
        if self.last_bet.text().count('1st 12'):
            if 0 < self.rand_number <= 12:
                self.win_all += self.win_one_st_12

        #  Если выпал 2nd 12
        if self.last_bet.text().count('2nd 12'):
            if 13 <= self.rand_number <= 24:
                self.win_all += self.win_two_nd_12

        #  Если выпал 3rd 12
        if self.last_bet.text().count('3rd 12'):
            if 25 <= self.rand_number <= 36:
                self.win_all += self.win_three_rd_12

        if self.last_bet.text().count('1-18'):
            for i in range(0, 19):
                if self.rand_number == i:
                    self.win_all += self.win_one_18

        if self.last_bet.text().count('19-36'):
            for i in range(19, 37):
                if self.rand_number == i:
                    self.win_all += self.win_nineteen_36

        if self.last_bet.text().count('EVEN'):
            if self.rand_number % 2 == 0:
                self.win_all += self.win_even

        if self.last_bet.text().count('ODD'):
            if self.rand_number % 2 != 0:
                self.win_all += self.win_odd

        if self.last_bet.text().count('RED'):
            red_numbers = [1, 3, 5, 7, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            if self.rand_number in red_numbers:
                self.win_all += self.win_red

        if self.last_bet.text().count('BLACK'):
            black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 28, 31, 33, 35]
            if self.rand_number in black_numbers:
                self.win_all += self.win_black

        if self.last_bet.text().count('FIRST LINE'):
            first_line = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
            if self.rand_number in first_line:
                self.win_all += self.win_two_to_one_1_34

        if self.last_bet.text().count('SECOND LINE'):
            second_line = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
            if self.rand_number in second_line:
                self.win_all += self.win_two_to_one_2_35

        if self.last_bet.text().count('THIRD LINE'):
            third_line = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
            if self.rand_number in third_line:
                self.win_all += self.win_two_to_one_3_36

         # Если выпал 1
        if self.rand_number == 1:
            self.win_all += self.win_btn_1

        if self.rand_number == 2:
            self.win_all += self.win_btn_2

        if self.rand_number == 3:
            self.win_all += self.win_btn_3

        if self.rand_number == 4:
            self.win_all += self.win_btn_4

        if self.rand_number == 5:
            self.win_all += self.win_btn_5

        if self.rand_number == 6:
            self.win_all += self.win_btn_6

        if self.rand_number == 7:
            self.win_all += self.win_btn_7

        if self.rand_number == 8:
            self.win_all += self.win_btn_8

        if self.rand_number == 9:
            self.win_all += self.win_btn_9

        if self.rand_number == 10:
            self.win_all += self.win_btn_10

        if self.rand_number == 11:
            self.win_all += self.win_btn_11

        if self.rand_number == 12:
            self.win_all += self.win_btn_12

        if self.rand_number == 13:
            self.win_all += self.win_btn_13

        if self.rand_number == 14:
            self.win_all += self.win_btn_14

        if self.rand_number == 15:
            self.win_all += self.win_btn_15

        if self.rand_number == 16:
            self.win_all += self.win_btn_16

        if self.rand_number == 17:
            self.win_all += self.win_btn_17

        if self.rand_number == 18:
            self.win_all += self.win_btn_18

        if self.rand_number == 19:
            self.win_all += self.win_btn_19

        if self.rand_number == 20:
            self.win_all += self.win_btn_20

        if self.rand_number == 21:
            self.win_all += self.win_btn_21

        if self.rand_number == 22:
            self.win_all += self.win_btn_22

        if self.rand_number == 23:
            self.win_all += self.win_btn_23

        if self.rand_number == 24:
            self.win_all += self.win_btn_24

        if self.rand_number == 25:
            self.win_all += self.win_btn_25

        if self.rand_number == 26:
            self.win_all += self.win_btn_26

        if self.rand_number == 27:
            self.win_all += self.win_btn_27

        if self.rand_number == 28:
            self.win_all += self.win_btn_28

        if self.rand_number == 29:
            self.win_all += self.win_btn_29

        if self.rand_number == 30:
            self.win_all += self.win_btn_30

        if self.rand_number == 31:
            self.win_all += self.win_btn_31

        if self.rand_number == 32:
            self.win_all += self.win_btn_32

        if self.rand_number == 33:
            self.win_all += self.win_btn_33

        if self.rand_number == 34:
            self.win_all += self.win_btn_34

        if self.rand_number == 35:
            self.win_all += self.win_btn_35

        if self.rand_number == 36:
            self.win_all += self.win_btn_36



        #  Итоги партии
        self.history_list = []  # Чистим историю
        self.last_bet.setText('')  # Чистим Лейбл со ставками
        self.all_bets = 0  # Обнуляем счетчик ставок

        if self.win_all != '':
            if self.bank_info.text() != '':
                self.win.setText(str(eval(self.win_all[0:-1])))  # Показываем общий выигрыш за партию
                self.cash.setText(str(eval(
                    self.cash.text() + '+' + self.win.text() + '+' + self.bank_info.text())))  # Добавляем выигрыш в окно Cash
            elif self.bank_info.text() == '':
                self.cash.setText(self.cash.text())
        elif self.bank_info.text() == '':
            self.cash.setText(self.cash.text())

        self.bank_info.setText('')  # Чистим окно Банк
        # Чистим счетчики с выигрышем с каждой позиции стола:
        self.win_zero = ''
        self.win_one_st_12 = ''
        self.win_two_nd_12 = ''
        self.win_three_rd_12 = ''
        self.win_btn_1 = ''
        self.win_btn_2 = ''
        self.win_btn_3 = ''
        self.win_btn_4 = ''
        self.win_btn_5 = ''
        self.win_btn_6 = ''
        self.win_btn_7 = ''
        self.win_btn_8 = ''
        self.win_btn_9 = ''
        self.win_btn_10 = ''
        self.win_btn_11 = ''
        self.win_btn_12 = ''
        self.win_btn_13 = ''
        self.win_btn_14 = ''
        self.win_btn_15 = ''
        self.win_btn_16 = ''
        self.win_btn_17 = ''
        self.win_btn_18 = ''
        self.win_btn_19 = ''
        self.win_btn_20 = ''
        self.win_btn_21 = ''
        self.win_btn_22 = ''
        self.win_btn_23 = ''
        self.win_btn_24 = ''
        self.win_btn_25 = ''
        self.win_btn_26 = ''
        self.win_btn_27 = ''
        self.win_btn_28 = ''
        self.win_btn_29 = ''
        self.win_btn_30 = ''
        self.win_btn_31 = ''
        self.win_btn_32 = ''
        self.win_btn_33 = ''
        self.win_btn_34 = ''
        self.win_btn_35 = ''
        self.win_btn_36 = ''
        self.win_one_18 = ''
        self.win_nineteen_36 = ''
        self.win_even = ''
        self.win_red = ''
        self.win_black = ''
        self.win_odd = ''
        self.win_two_to_one_1_34 = ''
        self.win_two_to_one_2_35 = ''
        self.win_two_to_one_3_36 = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = roulette()
    ex.show()
    sys.exit(app.exec_())
