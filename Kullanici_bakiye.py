import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Kullanici_bakiye(QtWidgets.QWidget):
    def __init__(self, SHA256Line):
        super().__init__()
        self.init_ui()

        self.SHA256Line = SHA256Line

        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("recycle.db")
        self.cursor = self.baglanti.cursor()

        self.baglanti.commit()

    def init_ui(self):
        self.gonderilecekMiktar = QtWidgets.QLabel("Gönderilecek Miktar:")
        self.gonderilecekMiktarLine = QtWidgets.QLineEdit()
        self.gonderilecekMiktarLine.setValidator(QtGui.QIntValidator(0, 100000000, self))
        self.gonderilecekKisi = QtWidgets.QLabel("Gönderilecek Kişi:")
        self.gonderilecekKisiLine = QtWidgets.QLineEdit()
        self.gonderilecekKisiLine.setPlaceholderText("SHA-256 Adresi")
        self.bilgilendirmeAlani = QtWidgets.QLabel()
        self.gonderButon = QtWidgets.QPushButton("Gönder")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.gonderilecekMiktar)
        v_box.addWidget(self.gonderilecekMiktarLine)
        v_box.addWidget(self.gonderilecekKisi)
        v_box.addWidget(self.gonderilecekKisiLine)
        v_box.addStretch()
        v_box.addWidget(self.bilgilendirmeAlani)
        v_box.addStretch()
        v_box.addWidget(self.gonderButon)

        self.setLayout(v_box)

        self.gonderButon.clicked.connect(self.Gonder)

        self.setGeometry(900, 200, 500, 250)

        self.setWindowTitle("Geri Dönüşüm Uygulaması")

        self.show()

# class Kullanici_bakiye(QtWidgets.QWidget):
#     def __init__(self, ad):
#         super().__init__()
#         self.init_ui()
#
#
#         self.ad = ad
#
#         self.baglanti_olustur()
#
#     def baglanti_olustur(self):
#         self.baglanti = sqlite3.connect("recycle.db")
#         self.cursor = self.baglanti.cursor()
#
#         self.baglanti.commit()
#
#     def init_ui(self):
#         self.arananCarbon = QtWidgets.QLabel("Carbon:")
#         self.arananCarbonLine = QtWidgets.QLabel()
#         self.arananCoin = QtWidgets.QLabel("Coin:")
#         self.arananCoinLine = QtWidgets.QLabel()
#
#         v_box = QtWidgets.QVBoxLayout()
#         v_box.addWidget(self.arananCarbon)
#         v_box.addWidget(self.arananCarbonLine)
#         v_box.addWidget(self.arananCoin)
#         v_box.addWidget(self.arananCoinLine)
#         print(self.ad)
#         self.cursor.execute("Select Carbon, Coin from KullaniciBilgileri Where SHA256 = ?", (self.ad))
#         bakiye = self.cursor.fetchall()
#         print(bakiye[0][0])
#         self.arananCoinLine.setText(bakiye[0][0])
#         self.arananCarbonLine.setText(bakiye[0][1])
#
#         self.setLayout(v_box)
#
#         self.setGeometry(900, 200, 500, 250)
#
#         self.setWindowTitle("Geri Dönüşüm Uygulaması")
#
#         self.show()