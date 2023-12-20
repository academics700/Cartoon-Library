# -*- coding: utf-8 -*-

'''
Author: @Anish Sarkar

Created: @06-07-2022
        14:51

Cartoon Finder v1.0.0
'''

# importing modules
import sys
import pandas as pd
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QPushButton, QGraphicsColorizeEffect, QSizePolicy,
                             QDesktopWidget, QGridLayout, QHBoxLayout, QAction,
                             qApp, QMenu, QShortcut, QFrame)
from PyQt5.QtGui import QIcon, QFont, QKeySequence
from PyQt5 import QtGui


widget_index = 0
index = 0
win = ''
qss = ['color : #ffc40c;\
           font-size : 38px;\
               font-family : Aller;',
        'color : #ffff66;\
            font-size : 20px;',
               'border : 0px solid black;\
                   border-radius : 0px;', '',
        'color : #e1d89f;\
            font-family : Calibri;\
                font-size : 20px;',
            'color : #e1d89f;\
                padding-top : 5px;\
                padding-left : 5px;\
                background : rgba(255, 255, 255, 0.03);\
                font-family : Calibri;\
                    font-size : 20px;',
            'color : #e1d89f;\
                font-family : Calibri;\
                    font-size : 20px;',
            'color : #e1d89f;\
                padding-top : 5px;\
                padding-left : 5px;\
                background : rgba(255, 255, 255, 0.05);\
                font-family : Aller;\
                    font-size : 16px;',
            'color : #e1d89f;\
                padding-top : 5px;\
                padding-left : 5px;\
                background : rgba(255, 255, 255, 0.07);\
                font-family : Calibri;\
                    font-size : 20px;']

df = pd.read_excel('Data.xlsx')
            
show_name = df['ShowName'].tolist()
series_type = df['SeriesType'].tolist()
date = df['Date'].tolist()
length = df['Length'].tolist()
genre1 = df['Genre1'].tolist()
genre2 = df['Genre2'].tolist()
genre3 = df['Genre3'].tolist()
genre = []
for i in range(len(genre1)):
    _ = [genre1[i], genre2[i], genre3[i]]
    genre.append(_)
rating = [str(x) for x in df['Rating'].tolist()]
rating_no = [str(x) for x in df['RatingNo'].tolist()]
popularity = [str(int(x)) for x in df['Popularity'].tolist()]
certificate = df['Certificate'].tolist()
creator = df['Creator'].tolist()
description = df['Description'].tolist()
wins = [str(int(x)) for x in df['Wins'].tolist()]
nominations = [str(int(x)) for x in df['Nominations'].tolist()]
Image = df['Image'].tolist()
Link = df['Link'].tolist()

labelText = []

for i in range(len(Link)):
    txt = [show_name[i],
                 '<sup><i>' + series_type[i] + '</i> | <i>' + date[i] + '\
                     </i> | <i>' + length[i] + '</i></sup>',
                 '',
                  '','<i>' + genre[i][0] + ' &nbsp;&nbsp;&nbsp;' + genre[i][1] + '\
                      &nbsp;&nbsp;&nbsp;\
                      ' + genre[i][2] + '</i><br>&#11088;\
                      <b><font style = "font-size : 24px;"px>' + rating[i] + '\
                          </font></b>/10\
                    <sub>' + rating_no[i] + '</sub>\
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
                        <font color = #ffc40c size = 30><b>&#8605;</b></font>\
                <b><font style = "font-size : 24px">' + popularity[i] + '</font></b>',
                  '<font color = #ffc40c><b>Certificate</b></font>\
                      &nbsp;&nbsp;<i>' + certificate[i] + '</i>',
                  '<br><b><font color = #ffc40c>Creator</font></b>\
                      <i>&nbsp;&nbsp;&nbsp;&nbsp;' + creator[i] + '</i>',
                  '<font color = #ffc40c><b>Description</b></font><br><br>\
                      ' + description[i],
                '<font color = #ffc40c><b>Awards & Nominations</b></font><br>\
                <br><i>' + wins[i] + ' wins & ' + nominations[i] + ' nominations</i>']
    labelText.append(txt)

uIndex = [1, 1, 2, 3, 1, 1, 1, 1, 1]
Pos = [(0, 0, 1, 1), (1, 0, 1, 1), (2, 0, 6, 1),
       (2, 1, 6, 1), (8, 0, 1, 1), (9, 0, 1, 1),
       (8, 1, 1, 1), (10, 0, 4, 1), (9, 1, 5, 1)]

R_stretch = [(0, 1), (1, 1), (2, 6), (8, 1), (9 ,1), (10, 4)]
Btn_ss = 'QPushButton::hover \
    { \
     background-color : rgba(255, 255, 255, 0.5); \
         } \
        QPushButton::pressed \
    { \
     background-color : rgba(255, 255, 255, 0.5); \
         }'
        
def cartoonlist(self, bg_img, action, tooltip_txt):
    global win, Image

    grid = QGridLayout()
    grid.setSpacing(16)
    self.setLayout(grid)
    
    self.label = QLabel(self)
    self.label.setWordWrap(True)
    self.label.setAlignment(Qt.AlignCenter)
    self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.label.setText('CHOOSE A CARTOON')
    self.label.setStyleSheet("color : black;\
                             background : #7fffd4;\
                             font-size : 35px;\
                                     font-family : Impact;\
                                         font-weight : bold;")
    grid.addWidget(self.label, 0, 0, 1, 3)

    pos = [(1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1),
           (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1),
           (3, 0, 1, 1), (3, 1, 1, 1), (3, 2, 1, 1)]
    
    row_stretch = [(0, 1), (1, 3), (2, 3), (3, 3)]
    
    for row, stretch in row_stretch:
        grid.setRowStretch(row, stretch)

    for i in range(len(pos)):
        
        qss = 'QPushButton\
            {border-image : url(' + bg_img[i] + ');}\
                QPushButton::hover \
                   { \
                    border : 5px solid black; \
                        }'
              
        btn = QPushButton(self)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn.clicked.connect(action[i])
        btn.setToolTip(tooltip_txt[i])
        btn.setStyleSheet(qss)

        x, y, rowspan, colspan = pos[i]
        grid.addWidget(btn, x, y, rowspan, colspan)

class __InfoWidget__(QWidget):

    def __init__(self):
        super().__init__()
        global widget_index, index
        index = widget_index - 7
        self.func_widget(index)
        
    def func_widget(self, index):
        
        global labelText, uIndex, Pos, R_stretch, Btn_ss, Image, Link
        
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        
        for row, stretch in R_stretch:
            grid.setRowStretch(row, stretch)

        for i in range(len(labelText[index])):
            if uIndex[i] == 1 or uIndex[i] == 2:
                self.label = QLabel(self)
                self.label.setTextFormat(Qt.RichText)
                self.label.setWordWrap(True)
                self.label.setAlignment(Qt.AlignLeft)
                self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.label.setText(labelText[index][i])
                self.label.setStyleSheet(qss[i])
                if uIndex[i] == 2:
                    self.label.setStyleSheet("border-radius : 0px;\
                                             border-image : url(" + Image[index] + ")")

                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(self.label, x, y, rowspan, colspan)
            if uIndex[i] == 3:
                
                txt = labelText[index][i]
                btn = QPushButton(txt, self)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btn.clicked.connect(self.open_webbrowser)
                btn.setStyleSheet(Btn_ss)
                btn.setStyleSheet("border-image : url(play.png)")
                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(btn, x, y, rowspan, colspan)
                
    def open_webbrowser(self):
        global Link, index
        url = QUrl(Link[index])
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')
            
class __ageWidget__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        global win

        grid = QGridLayout()
        grid.setSpacing(16)
        self.setLayout(grid)
        self.label = QLabel(self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setText('CHOOSE YOUR CHILD\'S AGE')
        self.label.setStyleSheet("color : black;\
                                 border : 5px solid black;\
                                 background : #e8f48c;\
                                 font-size : 35px;\
                                         font-family : IMPACT;")
        grid.addWidget(self.label, 0, 0, 1, 3)

        button_txt = ['', '', '',
                      '', '', '']

        pos = [(1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1),
               (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1)]

        action = [self.action0_3, self.action3_5, self.action5_7,
                  self.action7_9, self.action9_12, self.action12_plus]

        tooltip_txt = ['Cartoons for\n0-3 years', 'Cartoons for\n3-5 years',
                       'Cartoons for\n5-7 years', 'Cartoons for\n7-9 years',
                       'Cartoons for\n9-12 years', 'Cartoons for\n12+ years']

        row_stretch = [(0, 1), (1, 3), (2, 3)]

        bg_img = ['age_0.png', 'age_3.png', 'age_7.png',
                  'age_9.png', 'age_12.png', 'age_17.png']

        bg_clr = ['#ffa500', '#adff2f', '#8f00ff',
                  'cyan', '#808000', '#ffcc33']

        hover_clr = ['#ff4500', '#32cd32', '#4b0082',
                     '#48d1cc', '#556b2f', '#cba135']

        for row, stretch in row_stretch:
            grid.setRowStretch(row, stretch)

        for i in range(len(button_txt)):

            qss = 'QPushButton\
                {\
                 border-image : url(' + bg_img[i] + ');\
                     background :' + bg_clr[i] + ';\
                     border : 5px solid black;}\
                     QPushButton::hover \
                        { \
                         background-color :' + hover_clr[i] + '; \
                             }'

            txt = button_txt[i]
            btn = QPushButton(txt, self)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont('Calibri', btn.rect().width() // 6))
            btn.setToolTip(tooltip_txt[i])
            btn.setStyleSheet(qss)

            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)

    def action0_3(self):
        win.action0_3()

    def action3_5(self):
        win.action3_5()

    def action5_7(self):
        win.action5_7()

    def action7_9(self):
        win.action7_9()

    def action9_12(self):
        win.action9_12()

    def action12_plus(self):
        win.action12_plus()

class __Widget0_3__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):
        
        action = [self.dino_train, self.d_tiger, self.w_party,
                  self.w_kratts, self.s_street, self.s_why,
                  self.ssc_kid, self.w_girl, self.a_sbots ]

        tooltip_txt = show_name[0:9]        
        bg_img = Image[0:9]
        cartoonlist(self, bg_img, action, tooltip_txt)
    
    def dino_train(self):
        global widget_index
        widget_index = 7
        win.call_widget()
        
    def d_tiger(self):
        global widget_index
        widget_index = 8
        win.call_widget()

    def w_party(self):
        global widget_index
        widget_index = 9
        win.call_widget()

    def w_kratts(self):
        global widget_index
        widget_index = 10
        win.call_widget()

    def s_street(self):
        global widget_index
        widget_index = 11
        win.call_widget()

    def s_why(self):
        global widget_index
        widget_index = 12
        win.call_widget()
        
    def ssc_kid(self):
        global widget_index
        widget_index = 13
        win.call_widget()
        
    def w_girl(self):
        global widget_index
        widget_index = 14
        win.call_widget()
        
    def a_sbots(self):
        global widget_index
        widget_index = 15
        win.call_widget()

class __Widget3_5__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        action = [self.b_clues, self.n_blocks, self.p_petrol,
                  self.w_world, self.dora, self.l_einstein,
                  self.m_machine, self.octanauts, self.t_bus]

        tooltip_txt = show_name[9:18]        
        bg_img = Image[9:18]
        cartoonlist(self, bg_img, action, tooltip_txt)

    def b_clues(self):
        global widget_index
        widget_index = 16
        win.call_widget()
        
    def n_blocks(self):
        global widget_index
        widget_index = 17
        win.call_widget()

    def p_petrol(self):
        global widget_index
        widget_index = 18
        win.call_widget()

    def w_world(self):
        global widget_index
        widget_index = 19
        win.call_widget()

    def dora(self):
        global widget_index
        widget_index = 20
        win.call_widget()

    def l_einstein(self):
        global widget_index
        widget_index = 21
        win.call_widget()
        
    def m_machine(self):
        global widget_index
        widget_index = 22
        win.call_widget()
        
    def octanauts(self):
        global widget_index
        widget_index = 23
        win.call_widget()
        
    def t_bus(self):
        global widget_index
        widget_index = 24
        win.call_widget()

class __Widget5_7__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        action = [self.t_j, self.l_tunes, self.doraemon,
                  self.c_bheem, self.b_builder, self.s_bob,
                  self.p_sailor, self.m_mouse, self.simpsons]

        tooltip_txt = show_name[18:27]       
        bg_img = Image[18:27]
        cartoonlist(self, bg_img, action, tooltip_txt)

    def t_j(self):
        global widget_index
        widget_index = 25
        win.call_widget()
        
    def l_tunes(self):
        global widget_index
        widget_index = 26
        win.call_widget()

    def doraemon(self):
        global widget_index
        widget_index = 27
        win.call_widget()

    def c_bheem(self):
        global widget_index
        widget_index = 28
        win.call_widget()

    def b_builder(self):
        global widget_index
        widget_index = 29
        win.call_widget()

    def s_bob(self):
        global widget_index
        widget_index = 30
        win.call_widget()
        
    def p_sailor(self):
        global widget_index
        widget_index = 31
        win.call_widget()
        
    def m_mouse(self):
        global widget_index
        widget_index = 32
        win.call_widget()
        
    def simpsons(self):
        global widget_index
        widget_index = 33
        win.call_widget()

class __Widget7_9__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        action = [self.flintstones, self.d_tales, self.sonic,
                  self.y_bear, self.p_panther, self.s_doo,
                  self.pp_girls, self.pokemon, self.a_boy]

        tooltip_txt = show_name[27:36]       
        bg_img = Image[27:36]
        cartoonlist(self, bg_img, action, tooltip_txt)

    def flintstones(self):
        global widget_index
        widget_index = 34
        win.call_widget()
        
    def d_tales(self):
        global widget_index
        widget_index = 35
        win.call_widget()

    def sonic(self):
        global widget_index
        widget_index = 36
        win.call_widget()

    def y_bear(self):
        global widget_index
        widget_index = 37
        win.call_widget()

    def p_panther(self):
        global widget_index
        widget_index = 38
        win.call_widget()

    def s_doo(self):
        global widget_index
        widget_index = 39
        win.call_widget()
        
    def pp_girls(self):
        global widget_index
        widget_index = 40
        win.call_widget()
        
    def pokemon(self):
        global widget_index
        widget_index = 41
        win.call_widget()
        
    def a_boy(self):
        global widget_index
        widget_index = 42
        win.call_widget()

class __Widget9_12__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        action = [self.b_10, self.b_10af, self.b_10ua,
                  self.b_man, self.avengers, self.spiderm,
                  self.s_man, self.j_league, self.x_men]

        tooltip_txt = show_name[36:45]       
        bg_img = Image[36:45]
        cartoonlist(self, bg_img, action, tooltip_txt)

    def b_10(self):
        global widget_index
        widget_index = 43
        win.call_widget()
        
    def b_10af(self):
        global widget_index
        widget_index = 44
        win.call_widget()

    def b_10ua(self):
        global widget_index
        widget_index = 45
        win.call_widget()

    def b_man(self):
        global widget_index
        widget_index = 46
        win.call_widget()

    def avengers(self):
        global widget_index
        widget_index = 47
        win.call_widget()

    def spiderm(self):
        global widget_index
        widget_index = 48
        win.call_widget()
        
    def s_man(self):
        global widget_index
        widget_index = 49
        win.call_widget()
        
    def j_league(self):
        global widget_index
        widget_index = 50
        win.call_widget()
        
    def x_men(self):
        global widget_index
        widget_index = 51
        win.call_widget()

class __Widget12_plus__(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__widget()

    def __init__widget(self):

        global widget_index

        # setting grid layout
        grid = QGridLayout()
        grid.setSpacing(3)
        self.setLayout(grid)

        # button text
        button_txt = ['Dinosaur Train', 'Daniel Tiger\'s',
                      'Word Party', 'Wild Kratts',
                      'Sesame Street', 'Super Why', 'Sid the Science Kid',
                      'Word Girl', 'Ask the storybots']

        # grid position
        pos = [(0, 0, 1, 1), (0, 1, 1, 1), (0, 2, 1, 1),
               (1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1),
               (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1)]

        # action
        action = [self.action0_3, self.action3_5, self.action5_7,
                  self.action7_9, self.action9_12, self.action12_plus,
                  self.action0_3, self.action3_5, self.action5_7, ]

        tooltip_txt = ['Cartoons for\n0-3 years', 'Cartoons for\n3-5 years',
                       'Cartoons for\n5-7 years', 'Cartoons for\n7-9 years',
                       'Cartoons for\n9-12 years', 'Cartoons for\n12+ years',
                       'Cartoons for\n7-9 years',
                       'Cartoons for\n9-12 years', 'Cartoons for\n12+ years']

        row_stretch = [(0, 1), (1, 1), (2, 1)]

        for row, stretch in row_stretch:
            grid.setRowStretch(row, stretch)

        # setting buttons and actions
        for i in range(len(button_txt)):

            txt = button_txt[i]
            btn = QPushButton(txt, self)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont('Calibri', btn.rect().width() // 6))
            btn.setToolTip(tooltip_txt[i])

            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)

    # defining button actions+

    def action0_3(self):
        global widget_index
        widget_index = 1
        w = __main__window__()
        w.call_widget()

    def action3_5(self):
        global widget_index
        widget_index = 2

    def action5_7(self):
        global widget_index
        widget_index = 3

    def action7_9(self):
        global widget_index
        widget_index = 4

    def action9_12(self):
        global widget_index
        widget_index = 5

    def action12_plus(self):
        global widget_index
        widget_index = 6

class __main__window__(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting default window geometry
        self.setGeometry(100, 100, 100, 100)
        self.setMinimumSize(900, 700)
        self.setWindowTitle('Cartoon Finder')
        self.setWindowIcon(QIcon('Cartoon.ico'))
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 1.0.0')
        self.center()
        '''self.menu_bar()'''
        self.call_widget()
        self.show()

    def call_widget(self):
        global widget_index
        
        widget_list = [__ageWidget__(), __Widget0_3__(), __Widget3_5__(),
                       __Widget5_7__(), __Widget7_9__(), __Widget9_12__(),
                       __Widget12_plus__(), __InfoWidget__()]

        if widget_index < 7:
            widget = widget_list[widget_index]
                
        else:
            widget = __InfoWidget__()

        style_sheet = "QWidget \
            { \
             background : #222222; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #000000; \
                             border-radius : 10px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : rgba(0, 0, 0, 0.5); \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #D3D3D3; \
                             } \
                QLabel \
                    { \
                     border : 0px solid #000000; \
                         border-radius : 10px; \
                             } \
                QMenu \
                    { \
                     min-width : 80px; \
                         background-color : white; \
                             } \
                    QMenu::item \
                        { \
                         min-width : 60px; \
                             margin : 5; \
                                 padding : 5; \
                                     } \
                    QMenu::item:selected \
                        { \
                         color : black; \
                             background-color : #E5E4E2; \
                                 border : 0px solid black; \
                                     border-radius : 5px; \
                                         } \
                    QMenu::item:pressed \
                        { \
                         background-color : #D3D3D3; \
                             } \
                    QMenuBar::item:selected \
                        { \
                         border : 0px solid black; \
                             border-radius : 5px; \
                                 background-color : #E5E4E2; \
                                     } \
                    QMenuBar::item:pressed \
                        { \
                         background-color : white; \
                             }"

        self.setCentralWidget(widget)
        self.setStyleSheet(style_sheet)
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)
                
    def action0_3(self):
        global widget_index
        widget_index = 1
        self.call_widget()

    def action3_5(self):
        global widget_index
        widget_index = 2
        self.call_widget()

    def action5_7(self):
        global widget_index
        widget_index = 3
        self.call_widget()

    def action7_9(self):
        global widget_index
        widget_index = 4
        self.call_widget()

    def action9_12(self):
        global widget_index
        widget_index = 5
        self.call_widget()

    def action12_plus(self):
        global widget_index
        widget_index = 6
        self.call_widget()
        
    def func_call_widget(self):
        self.call_widget
        
    '''def dino_train(self):
        global widget_index
        widget_index = 7
        self.call_widget()
    
    def d_tiger(self):
        global widget_index
        widget_index = 8
        self.call_widget()
        
    def w_party(self):
        global widget_index
        widget_index = 9
        self.call_widget()
        
    def w_kratts(self):
        global widget_index
        widget_index = 10
        self.call_widget()
        
    def s_street(self):
        global widget_index
        widget_index = 11
        self.call_widget()
        
    def s_why(self):
        global widget_index
        widget_index = 12
        self.call_widget()
        
    def ssc_kid(self):
        global widget_index
        widget_index = 13
        self.call_widget()
        
    def w_girl(self):
        global widget_index
        widget_index = 14
        self.call_widget()
        
    def a_sbots(self):
        global widget_index
        widget_index = 15
        self.call_widget()
        
    def b_clues(self):
        global widget_index
        widget_index = 16
        self.call_widget()
    
    def n_blocks(self):
        global widget_index
        widget_index = 17
        self.call_widget()
        
    def p_petrol(self):
        global widget_index
        widget_index = 18
        self.call_widget()
        
    def w_world(self):
        global widget_index
        widget_index = 19
        self.call_widget()
        
    def dora(self):
        global widget_index
        widget_index = 20
        self.call_widget()
        
    def l_einstein(self):
        global widget_index
        widget_index = 21
        self.call_widget()
        
    def m_machine(self):
        global widget_index
        widget_index = 22
        self.call_widget()
        
    def octanauts(self):
        global widget_index
        widget_index = 23
        self.call_widget()
        
    def t_bus(self):
        global widget_index
        widget_index = 24
        self.call_widget()'''
        
    '''def menu_bar(self):
        menubar = self.menuBar()
        self.file_menu(menubar)
        self.view_menu(menubar)
        return menubar
        
        
    def file_menu(self, menubar):
        fileMenu = menubar.addMenu('&File')
        quit_act = self.exit_act()
        fileMenu.addAction(quit_act)
        
    def view_menu(self, menubar):
        viewMenu = menubar.addMenu('&View')
        self.view_stat_act(viewMenu)
        self.view_button_menu(viewMenu)
        self.view_display_menu(viewMenu)
    
    def view_button_menu(self, viewMenu):
        button_menu = QMenu('Buttons', self)
        font_menu = QMenu('Font', self)
        button_menu.addMenu(font_menu)
        icon = ['abel.png', 'times_new_roman.png', 'calibri.png',
                'arial.png', 'adam_warren_pro.png', 'brush_script.png']

        font_fcn = [self.__Abel__(icon[0]), self.__timesNewRoman__(icon[1]),
                    self.__calibri__(icon[2]), self.__arial__(icon[3]),
                    self.__adamWarrenPro__(icon[4]), self.__brushScriptMT__(icon[5])]
        
        for i in range(len(font_fcn)):
            font = font_fcn[i]
            font_menu.addAction(font)

        viewMenu.addMenu(button_menu)
        
    def view_display_menu(self, viewMenu):
        display_menu = QMenu('Themes', self)

        theme_fcn = [self.__classicLight__(), self.__classicDark__(), self.__dusk__()]
        
        for i in range(len(theme_fcn)):
            theme = theme_fcn[i]
            display_menu.addAction(theme)

        viewMenu.addMenu(display_menu)
        
    def view_stat_act(self, viewMenu):
        viewStatAct = QAction('Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View Statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggle_statusbar_Menu)
        viewMenu.addAction(viewStatAct)
        
    def toggle_statusbar_Menu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()'''

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    '''def exit_act(self):
        exitAct = QAction(QIcon('quit.png'), 'Exit', self)
        exitAct.setShortcut('Alt+F4')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        return exitAct'''

# defining main function to run application
def main():
    global win
    app = QApplication(sys.argv)
    win = __main__window__()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
