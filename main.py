from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from main_ui import Ui_MainWindow
import sys
from functions import getpassword, icmpv4, icmpv4_, funccleaner
from functions import getusername, getcpuname, getdiskspace, getmodel, getram, getmac, getip
import threading
import subprocess
import json
import os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Use the function to find your JSON file
json_path = resource_path("ip_address.json")









with open(json_path) as file:
    iplist : dict = json.loads(file.read())
    
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Sicoob Suporte')
        appicon = QIcon(u'.\\images\\logo.png')
        self.setWindowIcon(appicon)


        ###### NAVIGATING:
        #GO TO MENU:
        self.btn_backtomenu.clicked.connect(self.gotomenu)
        self.btn_backtomenu.clicked.connect(self.resetlaps)
        self.btn_backtomenu_2.clicked.connect(self.gotomenu)
        self.btn_backtomenu_2.clicked.connect(self.resetinfo)
        self.btn_backtomenu_3.clicked.connect(self.gotomenu)
        self.btn_backtomenu_3.clicked.connect(self.resetping)
        

        self.btnquit.clicked.connect(self.quitapp)
        self.btn_page_laps.clicked.connect(self.gotolaps)
        self.btn_page_pingtest.clicked.connect(self.gotoping)
        self.btn_page_infopc.clicked.connect(self.gotoinfo)


#     ---------------   INFO BUTTONS ----------------------

        self.btn_cleaner.clicked.connect(self.cleaner)
        self.btn_gpupdate.clicked.connect(self.gpupdate)
        self.btn_shutdownr.clicked.connect(self.turnoff)
        self.btn_shutdowns.clicked.connect(self.restart)
        
    
    ################ GETTING INFOO ############

        self.submitbutton_info.clicked.connect(self.show_username)
        self.submitbutton_info.clicked.connect(self.showdisk)
        self.submitbutton_info.clicked.connect(self.showcpu)
        self.submitbutton_info.clicked.connect(self.showmodel)
        self.submitbutton_info.clicked.connect(self.showram)
        self.submitbutton_info.clicked.connect(self.showmac)
        self.submitbutton_info.clicked.connect(self.showip)
        
        


        
        # !!!!!!!!!!!!      LAPS!!!!!!!!!!!!
        self.submitbutton_laps.clicked.connect(self.lapsfunction)   
        self.linepcname.editingFinished.connect(self.lapsfunction)    
        
        
        ################## PING############
        self.linepa.editingFinished.connect(self.pingtest_fw)
        self.linepcname_.editingFinished.connect(self.pingtest_others)

        

            # !!!!!!!!!!!!       LAPS !!!!!!!!!!!!
    def lapsfunction(self):
        
        pcname = self.linepcname.text()
        password = getpassword(pcname)
        self.linepassword.setText(password)
        
        

        
        
    def gotomenu(self):
        self.stackedWidget.setCurrentWidget(self.menu)
        
    def gotolaps(self):
        self.stackedWidget.setCurrentWidget(self.page_laps)
        
    def gotoinfo(self):
        self.stackedWidget.setCurrentWidget(self.page_infopc)
        
    def gotoping(self):
        self.stackedWidget.setCurrentWidget(self.page_ping)
        
    def quitapp(self):
        self.close()



# --------------- PING----------------
#firewallcheck playcheck ccscheck centralcheck uadcheck
    def pingtest_fw(self):
        
        ip = str(self.linepa.text())
        result = icmpv4(ip)
        if result == 1:
            self.firewallcheck.setStyleSheet(u"background-color: green;\nborder-radius:10px")
        else:
            self.firewallcheck.setStyleSheet(u"background-color: red;\nborder-radius:10px")
        

    def pingtest_others(self):
        pcname = self.linepcname_.text()
        name_and_ip = {self.playcheck : iplist['play'], self.ccscheck : iplist['ccs'],
                        self.uadcheck : iplist['uad'], self.centralcheck : iplist['central']}
        
        for key, value in name_and_ip.items():  
            
            result = icmpv4_(pcname, value)
            if result == 1:
                key.setStyleSheet(u"background-color: green;\nborder-radius:10px")
            else:
                key.setStyleSheet(u"background-color: red;\nborder-radius:10px")
        
    
    def resetping(self):
        
        self.playcheck.setStyleSheet(u"background-color: aliceblue;\nborder-radius:10px")
        self.firewallcheck.setStyleSheet(u"background-color: aliceblue;\nborder-radius:10px")
        self.uadcheck.setStyleSheet(u"background-color: aliceblue;\nborder-radius:10px")
        self.centralcheck.setStyleSheet(u"background-color: aliceblue;\nborder-radius:10px")
        self.ccscheck.setStyleSheet(u"background-color: aliceblue;\nborder-radius:10px")
        self.linepa.clear()
        self.linepcname_.clear()
        
    def resetinfo(self):
        
        self.linecpu.clear()
        self.lineEdit_3.clear()
        self.linefreedisk.clear()
        self.linetotaldisk.clear()
        self.linemac.clear()
        self.lineip.clear()
        self.lineram.clear()
        self.linetotaldisk.clear()
        self.lineuser.clear()
        self.linemodelo.clear()
        
    def resetlaps(self):
        
        self.linepassword.clear()
        self.linepcname.clear()
            


#   - -------------------------- CLEANER -----------

    def cleaner(self):
        pcname = self.lineEdit_3.text()
        threadclean = threading.Thread(target=funccleaner, args=(pcname,))
        threadclean.start()
        
    def gpupdate(self):
        pcname = self.lineEdit_3.text()
        def gpupdate(pcname):
            subprocess.run(f'psexec \\\\{pcname} cmd /c gpupdate')
        threadgp = threading.Thread(target=gpupdate, args=(pcname,))
        threadgp.start()

    def turnoff(self):
        pcname = self.lineEdit_3.text()
        subprocess.run(f'psexec \\\\{pcname} cmd /c shutdown -s -f -t 0')

    def restart(self):
        pcname = self.lineEdit_3.text()
        subprocess.run(f'psexec \\\\{pcname} cmd /c shutdown -r -f -t 0')

     



#################### INFOO PC ##################





    def show_username(self):
        
        username = getusername(self.lineEdit_3.text())
        self.lineuser.setText(username)
    
    def showcpu(self):
        
        cpu = getcpuname(self.lineEdit_3.text())
        self.linecpu.setText(cpu)
        
    def showdisk(self):
        
        try:
            freedisk, totaldisk = getdiskspace(self.lineEdit_3.text())
            self.linefreedisk.setText(freedisk)
            self.linetotaldisk.setText(totaldisk)
        
        except ValueError:
            self.linefreedisk.setText('Máquina desligada')
            self.linetotaldisk.setText('Máquina desligada')
        
        
    def showmodel(self):
        
        model  = getmodel(self.lineEdit_3.text())
        self.linemodelo.setText(model)
        
    def showram(self):
        
        ram = getram(self.lineEdit_3.text())
        self.lineram.setText(ram)
    
        
    def showmac(self):
        
        mac = getmac(self.lineEdit_3.text())
        self.linemac.setText(mac)
        
    def showip(self):
        
        ip = getip(self.lineEdit_3.text())
        self.lineip.setText(ip)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
