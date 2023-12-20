# -*- coding: utf-8 -*-

'''
Author: @Anish Sarkar

Created: @06-07-2022
        14:51

Cartoon Finder v1.1.0
'''

import sys
import pandas as pd
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QPushButton, QSizePolicy, QDesktopWidget, QGridLayout,
                             QVBoxLayout, QAction, QFrame, QScrollArea,
                             QGroupBox, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon, QFont, QDesktopServices

a = 0
count = ''
widget_index = 0
index = 0
win = ''
df = pd.read_excel('Data/Data.xlsx', sheet_name='qss')
qss = df['Qss'].tolist()
sheet_name =['age_0_3', 'age_3_5', 'age_5_7', 'age_7_9', 'age_9_12', 'age_12+']
show_name = []
series_type = []
date = []
length = []
genre1 = []
genre2 = []
genre3 = []
rating = []
rating_no = []
popularity = []
certificate = []
creator = []
description = []
wins = []
nominations = []
Image = []
Link = []
Image_300 = []
var = [show_name, series_type, date, length, genre1, genre2, genre3,
       rating, rating_no, popularity, certificate, creator, description,
       wins, nominations, Image, Link, Image_300]
var_index = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0]
col_name = ['ShowName', 'SeriesType', 'Date', 'Length', 'Genre1', 'Genre2', 'Genre3',
            'Rating', 'RatingNo', 'Popularity', 'Certificate', 'Creator', 'Description',
            'Wins', 'Nominations', 'Image', 'Link', 'Image_300'] 

for i in range(len(sheet_name)):
    df = pd.read_excel('Data/Data.xlsx', sheet_name=sheet_name[i])
    for _ in range(len(var)):
        if var_index[_] == 0:
            var[_].append(df[col_name[_]].tolist())
        elif var_index[_] == 1:
            var[_].append([str(x) for x in df[col_name[_]].tolist()])
        else:
            var[_].append([str(int(x)) for x in df[col_name[_]].tolist()])

Gradient_clr = ['#2f4f4f', '#483c32', '#444c38', '#36454f', '#003153', '#4e1609']

labelText = [[], [], [], [], [], []]

for j in range(len(Link)):
    for i in range(len(Link[j])):
        txt = [show_name[j][i],
               '<sup><i>' + series_type[j][i] + '</i> | <i>' + date[j][i] + '\
                </i> | <i>' + length[j][i] + '</i></sup>', '',
                '','<i>' + genre1[j][i] + ' &nbsp;&nbsp;&nbsp;' + genre2[j][i] + '\
                &nbsp;&nbsp;&nbsp;' + genre3[j][i] + '</i><br>&#11088;\
                <b><font style = "font-size : 24px;"px>' + rating[j][i] + '\
                </font></b>/10<sub>' + rating_no[j][i] + '</sub>\
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
                <font color = #ceff00 size = 30><b>&#8605;</b></font>\
                <b><font style = "font-size : 24px">' + popularity[j][i] + '</font></b>',
                '<font color = #ceff00><b>Certificate</b></font>\
                &nbsp;&nbsp;<i>' + certificate[j][i] + '</i>',
                '<br><b><font color = #ceff00>Creator</font></b>\
                <i>&nbsp;&nbsp;&nbsp;&nbsp;' + creator[j][i] + '</i>',
                '<font color = #ceff00><b>Description</b></font><br><br>\
                ' + description[j][i],
                '<font color = #ceff00><b>Awards & Nominations</b></font><br>\
                <br><i>' + wins[j][i] + ' wins & ' + nominations[j][i] + ' nominations</i>\
                <br><br><i><font style="font-size:18px;">This cartoon is '
                + genre3[j][i] + '. This should be appropriate for\
                your child\'s age.</font></i>']
        labelText[j].append(txt)

uIndex = [1, 1, 2, 3, 1, 1, 1, 1, 1]
Pos = [(0, 0, 1, 1), (1, 0, 1, 1), (2, 0, 6, 1),
       (2, 1, 6, 1), (8, 0, 1, 1), (9, 0, 1, 1),
       (8, 1, 1, 1), (10, 0, 4, 1), (9, 1, 5, 1)]

R_stretch = [(0, 1), (1, 1), (2, 6), (8, 1), (9 ,1), (10, 4)]
Btn_ss = 'QPushButton::hover { background-color : rgba(255, 255, 255, 0.5);} \
         QPushButton::pressed { background-color : rgba(255, 255, 255, 0.5);}'

def _info_1():
    global widget_index
    widget_index = 7
    win.call_widget()
    
def _info_2():
    global widget_index
    widget_index = 8
    win.call_widget()

def _info_3():
    global widget_index
    widget_index = 9
    win.call_widget()

def _info_4():
    global widget_index
    widget_index = 10
    win.call_widget()

def _info_5():
    global widget_index
    widget_index = 11
    win.call_widget()

def _info_6():
    global widget_index
    widget_index = 12
    win.call_widget()
    
def _info_7():
    global widget_index
    widget_index = 13
    win.call_widget()
    
def _info_8():
    global widget_index
    widget_index = 14
    win.call_widget()
    
def _info_9():
    global widget_index
    widget_index = 15
    win.call_widget()
        
def cartoonlist(self, bg_img, action, tooltip_txt, local_rating,
                local_rating_no, local_creator, local_genre3, grad_clr,
                local_genre1, local_genre2):
    global win, Image

    grid = QGridLayout()
    grid.setSpacing(16)
    
    scroll = QScrollArea()   
    scroll.setStyleSheet("border:0px;")    
    scroll.setFrameShape(QFrame.Box)
    scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.setWidgetResizable(True)

    groupbox = QGroupBox("")
    groupbox.setMinimumSize(200, 1000)
    groupbox.setStyleSheet('border:0px; border-radius:10px;')
    groupbox.setCheckable(False)
    vbox = QVBoxLayout()
    groupbox.setLayout(vbox)
    grid.addWidget(scroll, 0, 0, 3, 1)
    grid.setContentsMargins(0, 0, 0, 0)

    self.setLayout(grid) 

    for i in range(len(tooltip_txt)):
        
        qss = 'QPushButton\
            {border-image:url("Images/' + bg_img[i] + '");}\
            QPushButton::hover\
            {border:5px solid black;}'
                       
        inner_grid = QGridLayout()
        inner_grid.setColumnStretch(0, 1)
        inner_grid.setColumnStretch(1, 5)
        g_box = QGroupBox("")
        g_box.setCheckable(False)
        g_box.setLayout(inner_grid)
        g_box.setStyleSheet("QGroupBox{background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\
                            stop: 0 #2b2b2b, stop: 1 " + grad_clr + ");}")
        
        lbl = QLabel(self)
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignLeft)
        lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        lbl.setStyleSheet('QLabel{color:#ffff99; font-size:24px; padding-left:10px;\
                          background : rgba(255, 255, 255, 0.0)}\
                          QLabel::hover{background:rgba(0, 0, 0, 0.08)}')
        lbl.setText('<font style = "font-size:20px;">'+tooltip_txt[i]+
                    '</font><br>&#11088;\
                    <b><font size = 24px color= #e1d89f>' + local_rating[i] + '\
                    </font></b><font color=#e1d89f size=22px>/10\
                    <sub>' + local_rating_no[i] + '</font></sub><br>' +
                    '<font size=22px><b>Creator:</b></font> <font color=#e1d89f size=22px>'
                    +local_creator[i]+'<br><i>'+local_genre3[i]+'&nbsp;&nbsp;&nbsp;&nbsp;'+local_genre2[i]+
                    '&nbsp;&nbsp;&nbsp;&nbsp;'+local_genre1[i]+'</i></font>')   
              
        btn = QPushButton(self)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn.clicked.connect(action[i])
        btn.setToolTip(tooltip_txt[i])
        btn.setStyleSheet(qss)
        inner_grid.addWidget(btn, 0, 0, 1, 1)
        inner_grid.addWidget(lbl, 0, 1, 1, 5)
        vbox.addWidget(g_box)
        
    scroll.setWidget(groupbox)
    
class __InfoWidget__(QWidget):

    def __init__(self):
        super().__init__()
        global widget_index, index
        index = widget_index-7
        self.func_widget(index)
        
    def func_widget(self, index):
        global labelText, uIndex, Pos, R_stretch, Btn_ss, Image, Link
        
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        
        for row, stretch in R_stretch:
            grid.setRowStretch(row, stretch)
        for i in range(len(labelText[a][index])):
            if uIndex[i] == 1 or uIndex[i] == 2:
                self.label = QLabel(self)
                self.label.setTextFormat(Qt.RichText)
                self.label.setWordWrap(True)
                self.label.setAlignment(Qt.AlignLeft)
                self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.label.setText(labelText[a][index][i])
                self.label.setStyleSheet(qss[i])
                if uIndex[i] == 2:
                    self.label.setStyleSheet("border-radius:0px;\
                                             border-image:url('Images/" + Image[a][index] + "')")

                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(self.label, x, y, rowspan, colspan)
            if uIndex[i] == 3:               
                txt = labelText[a][index][i]
                btn = QPushButton(txt, self)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btn.clicked.connect(self.open_webbrowser)
                btn.setStyleSheet(Btn_ss)
                btn.setStyleSheet("border-image:url('Images/play.png')")
                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(btn, x, y, rowspan, colspan)
                
    def open_webbrowser(self):
        global Link, index
        url = QUrl(Link[a][index])
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not open url')
            
class __ageWidget__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):
        global win
        grid = QGridLayout()
        grid.setSpacing(16)
        
        scroll = QScrollArea()   
        scroll.setStyleSheet("border:0px;")    
        scroll.setFrameShape(QFrame.Box)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)

        groupbox = QGroupBox("")
        groupbox.setMinimumSize(200, 1000)
        groupbox.setStyleSheet('border:0px; border-radius:10px;')
        groupbox.setCheckable(False)
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        grid.addWidget(scroll, 0, 0, 3, 1)
        grid.setContentsMargins(0, 0, 0, 0)

        self.setLayout(grid)
        
        action = [self.action0_3, self.action3_5, self.action5_7,
                  self.action7_9, self.action9_12, self.action12_plus]

        tooltip_txt = ['Cartoons for\n0-3 years', 'Cartoons for\n3-5 years',
                       'Cartoons for\n5-7 years', 'Cartoons for\n7-9 years',
                       'Cartoons for\n9-12 years', 'Cartoons for\n12+ years']

        bg_img = ['age_0.png', 'age_3.png', 'age_7.png', 'age_9.png', 'age_12.png', 'age_17.png']
        df = pd.read_excel('Data/Data.xlsx', sheet_name='age_label_txt')
        __label_text = df['text'].tolist()

        for i in range(len(action)):
            qss = 'QPushButton{\
                border-image:url("Images/' + bg_img[i] + '");\
                background:rgba(255,255,255,0.15);\
                border:5px solid black;}\
                QPushButton::hover{ \
                background-color:rgba(255,255,255,0.25);}'
                           
            inner_grid = QGridLayout()
            inner_grid.setColumnStretch(0, 1)
            inner_grid.setColumnStretch(1, 5)
            g_box = QGroupBox("")
            g_box.setCheckable(False)
            g_box.setLayout(inner_grid)
            g_box.setStyleSheet("QGroupBox{background-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,\
                                stop: 0 #2b2b2b, stop: 1 #4c516d); padding-left:5px; padding-right:5px;}")
            
            lbl = QLabel(self)
            lbl.setWordWrap(True)
            lbl.setAlignment(Qt.AlignLeft)
            lbl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            lbl.setStyleSheet('QLabel{color:#ffff99; font-size:20px; padding-left:10px;\
                              background:rgba(255, 255, 255, 0.0)}\
                              QLabel::hover{background:rgba(0, 0, 0, 0.08)}')
            lbl.setText(__label_text[i])   
                  
            btn = QPushButton('', self)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont('Calibri', btn.rect().width() // 6))
            btn.setToolTip(tooltip_txt[i])
            btn.setStyleSheet(qss)
            inner_grid.addWidget(btn, 0, 0, 1, 1)
            inner_grid.addWidget(lbl, 0, 1, 1, 5)
            vbox.addWidget(g_box)
            
        scroll.setWidget(groupbox)

    def action0_3(self):
        global widget_index
        widget_index = 1
        win.call_widget()

    def action3_5(self):
        global widget_index
        widget_index = 2
        win.call_widget()

    def action5_7(self):
        global widget_index
        widget_index = 3
        win.call_widget()

    def action7_9(self):
        global widget_index
        widget_index = 4
        win.call_widget()

    def action9_12(self):
        global widget_index
        widget_index = 5
        win.call_widget()

    def action12_plus(self):
        global widget_index
        widget_index = 6
        win.call_widget()

class __InfoShow__(QWidget):

    def __init__(self, counter):
        super().__init__()
        self.__init__widget(counter)

    def __init__widget(self, counter):
        global count, _action
        count = counter
        
        action = [_info_1, _info_2, _info_3, _info_4, _info_5, _info_6,
                  _info_7, _info_8, _info_9]

        cartoonlist(self, Image_300[count], action, show_name[count], rating[count],
                    rating_no[count], creator[count], genre3[count], Gradient_clr[count],
                    genre2[count], genre1[count])

class __main__window__(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(900, 750)
        self.setWindowTitle('Cartoon World')
        self.setWindowIcon(QIcon('Cartoon.ico'))
        self.setWindowOpacity(0.95)
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 1.1.0')
        back = QAction(QIcon('Images/back.png'), 'Back', self)
        back.setShortcut('Back Space')
        back.triggered.connect(self.action_back)

        self.toolbar = self.addToolBar('Back')
        self.toolbar.addAction(back)
        self.center()
        self.call_widget()
        self.show()

    def call_widget(self):
        global widget_index, a
        
        if widget_index == 0:
            widget = __ageWidget__()
        elif widget_index > 0 and widget_index < 7:
            widget = __InfoShow__(widget_index-1)
        else:
            for i in range(6):
                if count == i:
                    a = i
                    widget = __InfoWidget__()

        self.setCentralWidget(widget)
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)
        
    def action_back(self):
        global widget_index
        if widget_index == 0:
            widget_index = 0
        elif widget_index >= 1 and widget_index <= 6:
            widget_index = 0
            self.call_widget()
        else:
            for i in range(6):
                if count == i:
                    widget_index = i+1
                    self.call_widget()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    global win
    app = QApplication(sys.argv)
    qss="Data/stylesheet.qss"
    with open(qss,"r") as fh:
        app.setStyleSheet(fh.read())
    win = __main__window__()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()