# This Python file uses the following encoding: utf-8
import sys
import random
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_anaPencere

secenek = ["TAŞ","KAĞIT","MAKAS"]
humanPuan = 0
pcPuan = 0
pc = random.randint(0,2)
say= 1
class anaPencere(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_anaPencere()
        self.ui.setupUi(self)
        self.ui.radioTas.clicked.connect(self.kontrol)
        self.ui.radioKagit.clicked.connect(self.kontrol)
        self.ui.radioMakas.clicked.connect(self.kontrol)
    def kontrol(self):
        global humanPuan,pcPuan,pc,say
        if (self.ui.radioTas.isChecked()):
            secim = 0
        elif (self.ui.radioKagit.isChecked()):
            secim = 1
        elif (self.ui.radioMakas.isChecked()):
            secim = 2

        if (((pc== 0) and (secim==1)) or ((pc==1) and (secim==2)) or ((pc==2) and (secim==0))):
            humanPuan=humanPuan+1
            self.ui.label_2.setText("DURUM : KAZANDINIZ")
        elif (pc==secim):
            self.ui.label_2.setText("DURUM : BERABERE")
        else:
            self.ui.label_2.setText("DURUM : KAYBETTİNİZ")
            pcPuan=pcPuan+1
        self.ui.label_1.setText("PC SEÇİMİ : "+secenek[pc])
        self.ui.label_3.setText("SİZ: "+str(humanPuan)+"   BİLGİSAYAR: "+str(pcPuan))
        pc = random.randint(0,2)
        self.ui.sayac.setText("sayaç="+str(say))
        say= say+1

        self.ui.radioTas.setCheckable(False)
        self.ui.radioKagit.setCheckable(False)
        self.ui.radioMakas.setCheckable(False)

        self.ui.radioTas.setCheckable(True)
        self.ui.radioKagit.setCheckable(True)
        self.ui.radioMakas.setCheckable(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = anaPencere()
    widget.show()
    sys.exit(app.exec())
