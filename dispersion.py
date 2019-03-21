__author__='Dengdecai'
__email__ = 'decaideng@gmail.com'

from w import *
from imgs import *
import sys
from math import pi
from math import sin
from PyQt5.QtWidgets import QFileDialog,QMessageBox


class Dispersion(Ui_Dispersion,QtWidgets.QDialog):
    def __init__(self):
        super(Dispersion,self).__init__()
        self.setupUi(self)
        self.dtob.clicked.connect(self.d2b)
        self.btod.clicked.connect(self.b2d)
        self.gcal.clicked.connect(self.g_cal)
        self.done=0
        self.c=3e8
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告！', '关掉它吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def d2b(self):
        lamda0=self.lamda.value()*1e-9
        D2=float(self.D2.value())  # ps/nm
        D2=D2*1e-3        # s/m 
        D3=float(self.D3.value())  # ps/nm^2
        D3=D3*1e6         # s/m^2
        D4=float(self.D4.value())  # ps/nm^3
        D4*=1e15          # s/m^3
        beta2=-D2*lamda0**2/(2*pi*self.c) # s^2 
        beta3=(D3-4*pi*self.c/(lamda0**3)*beta2)*lamda0**4/(4*pi**2*self.c**2) # s^3
        beta4=(D4*lamda0**4/(-4*pi*self.c)-3*beta2-6*pi*self.c/lamda0*beta3)/(2*pi**2*self.c**2/lamda0**2)
        beta2=beta2*1e24  #ps^2
        beta3=beta3*1e36  #ps^3
        beta4=beta4*1e48  #ps^4
        self.r_beta2.setText(str('%4.4f' % beta2))
        self.r_beta3.setText(str('%4.4f' % beta3))
        self.r_beta4.setText(str('%4.4f' % beta4))

    def b2d(self):
        lamda0=self.lamda.value()*1e-9
        beta2=float(self.beta2.value())  # ps2
        beta2=beta2*1e-24        # s^2 
        beta3=float(self.beta3.value())  # ps^3
        beta3=beta3*1e-36         # s^3
        beta4=float(self.beta4.value())  # ps^4
        beta4*=1e-48
        D2=-2*pi*self.c*beta2/lamda0**2  #s/m
        D3=4*pi**2*self.c**2*beta3/lamda0**4+4*pi*beta2*self.c/lamda0**3  #s/m^2
        D4=-4*pi*self.c/lamda0**4*(2*pi**2*self.c**2/lamda0**2*beta4+6*pi*self.c/lamda0*beta3+3*beta2) #s/m^3
        D2=D2*1e3
        D3=D3*1e-6
        D4*=1e-15
        self.r_D2.setText(str('%4.4f' % D2))
        self.r_D3.setText(str('%4.4f' % D3))
        self.r_D4.setText(str('%4.4f' % D4))
    def g_cal(self):
        lamda0=self.lamda.value()*1e-9
        G_o=float(self.G.value())
        N_o=float(self.N_o.value())*1e3
        d_o=1/N_o
        theta_o=float(self.theta_o.value())/180*pi
        rg_beta2=-G_o*lamda0**3/(d_o**2*pi*self.c**2*(1-(lamda0/d_o-sin(theta_o))**2)**(3/2))   #s^2
        rg_beta3=-rg_beta2*(3*lamda0/(2*pi*self.c))*(1+lamda0*N_o*((lamda0*N_o-sin(theta_o))/(1-(lamda0*N_o-sin(theta_o))**2)))  #s^3
        rg_beta4=(2*rg_beta3)**2/(3*rg_beta2)+(lamda0**2*N_o/(2*pi*self.c*(1-(lamda0*N_o-sin(theta_o))**2)))**2*rg_beta2  #s^4
        rg_D2=-2*pi*self.c*rg_beta2/lamda0**2  # s/m
        rg_D3=4*pi**2*self.c**2*rg_beta3/lamda0**4+4*pi*rg_beta2*self.c/lamda0**3  #s/m^2
        rg_D4=-4*pi*self.c/lamda0**4*(2*pi**2*self.c**2/lamda0**2*rg_beta4+6*pi*self.c/lamda0*rg_beta3+3*rg_beta2) #s/m^3
        rg_beta2=rg_beta2*1e24     #ps^2
        rg_beta3*=1e36    #ps^3
        rg_beta4*=1e48    #ps^3
        rg_D2*=1e3   # ps/nm
        rg_D3*=1e-6  # ps/nm^2
        rg_D4*=1e-15 #ps /nm^3
        be4_be3=rg_beta4/rg_beta3*1e3
        be3_be2=rg_beta3/rg_beta2*1e3

        self.rg_beta2.setText(str('%4.4f' % rg_beta2))
        self.rg_beta3.setText(str('%4.4f' % rg_beta3))
        self.rg_beta4.setText(str('%4.4f' % rg_beta4))
        self.rg_D2.setText(str('%4.4f' % rg_D2))
        self.rg_D3.setText(str('%4.4f' % rg_D3))
        self.rg_D4.setText(str('%4.4f' % rg_D4))
        self.be3_be2.setText(str('%4.4f' % be3_be2))
        self.be4_be3.setText(str('%4.4f' % be4_be3))



if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    window = Dispersion()
    window.show()
    sys.exit(app.exec())
