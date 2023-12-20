# -*- coding: utf-8 -*-

'''
Author: @Anish Sarkar

Created: @06-07-2022
        14:51

Cartoon Finder v1.2.0
'''

import sys
import pandas as pd
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QPushButton, QSizePolicy, QDesktopWidget, QGridLayout,
                             QVBoxLayout, QAction, QFrame, QScrollArea, QSlider,
                             QGroupBox, QHBoxLayout, QMessageBox, QStyle)
from PyQt5.QtGui import QIcon, QFont, QDesktopServices

a = 0
count = ''
widget_index = 0
index = 0
win = ''
df = pd.read_excel('Data/Data.xlsx', sheet_name='qss')
qss = df['Qss'].tolist()

for i in range(0, 19):
    globals()[f"col_{i}"] = []

sheet_name =['age_0_3', 'age_3_5', 'age_5_7', 'age_7_9', 'age_9_12', 'age_12+']
var = [col_0, col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10, col_11,
       col_12, col_13, col_14, col_15, col_16, col_17, col_18]
var_index = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0]
col_name = ['ShowName', 'SeriesType', 'Date', 'Length', 'Genre1', 'Genre2', 'Genre3',
            'Rating', 'RatingNo', 'Popularity', 'Certificate', 'Creator', 'Description',
            'Wins', 'Nominations', 'Image', 'Link', 'Image_300', 'Video'] 

for i in range(len(sheet_name)):
    df = pd.read_excel('Data/Data.xlsx', sheet_name=sheet_name[i])
    for _ in range(19):
        if var_index[_] == 0:
            var[_].append(df[col_name[_]].tolist())
        elif var_index[_] == 1:
            var[_].append([str(x) for x in df[col_name[_]].tolist()])
        else:
            var[_].append([str(int(x)) for x in df[col_name[_]].tolist()])
Gradient_clr = ['#2f4f4f', '#483c32', '#444c38', '#36454f', '#003153', '#4e1609']
labelText = [[], [], [], [], [], []]

for j in range(len(sheet_name)):
    for i in range(len(var[16][j])):
        txt = [var[0][j][i],
               '<sup><i>' + var[1][j][i] + '</i> | <i>' + var[2][j][i] + '\
                </i> | <i>' + var[3][j][i] + '</i></sup>', '', '',
                '','<i>' + var[4][j][i] + ' &nbsp;&nbsp;&nbsp;' + var[5][j][i] + '\
                &nbsp;&nbsp;&nbsp;' + var[6][j][i] + '</i><br>&#11088;\
                <b><font style = "font-size : 24px;"px>' + var[7][j][i] + '\
                </font></b>/10<sub>' + var[8][j][i] + '</sub>\
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\
                <font color = #ceff00 size = 30><b>&#8605;</b></font>\
                <b><font style = "font-size : 24px">' + var[9][j][i] + '</font></b>',
                '<font color = #ceff00><b>Certificate</b></font>\
                &nbsp;&nbsp;<i>' + var[10][j][i] + '</i>',
                '<br><b><font color = #ceff00>Creator</font></b>\
                <i>&nbsp;&nbsp;&nbsp;&nbsp;' + var[11][j][i] + '</i>',
                '<font color = #ceff00><b>Description</b></font><br><br>\
                ' + var[12][j][i],
                '<font color = #ceff00><b>Awards & Nominations</b></font><br>\
                <br><i>' + var[13][j][i] + ' Wins & ' + var[14][j][i] + ' Nominations</i>\
                <br><br><i><font style="font-size:18px;">This cartoon is '
                + var[6][j][i] + '. This should be appropriate for\
                your child\'s age.</font></i>']
        labelText[j].append(txt)

uIndex = [1, 1, 2, 4, 3, 1, 1, 1, 1, 1]
Pos = [(0, 0, 1, 3), (1, 0, 1, 3), (2, 0, 7, 2), (2, 2, 7, 3),
       (2, 5, 7, 1), (9, 0, 1, 3), (10, 0, 1, 3),
       (9, 3, 1, 3), (11, 0, 4, 3), (10, 3, 5, 3)]

R_stretch = [(0, 1), (1, 1), (2, 10), (9, 1), (10 ,1), (11, 4)]
C_stretch = [(0, 1), (1, 1), (2, 3), (3, 1), (4, 1), (5, 1)]
Btn_ss = 'QPushButton::hover { background-color : rgba(255, 255, 255, 0.5);} \
         QPushButton::pressed { background-color : rgba(255, 255, 255, 0.5);}'

def factory(dummy):
    def _info_():
        global widget_index
        widget_index = dummy
        win.call_widget()
    return _info_

info_functions = []
for i in range(7,16):
    info_functions.append(factory(i))
        
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
        global labelText, uIndex, Pos, R_stretch, Btn_ss, Image, Link, C_Stretch
        
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        
        for row, stretch in R_stretch:
            grid.setRowStretch(row, stretch)
        for col, stretch in C_stretch:
            grid.setColumnStretch(col, stretch)
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
                                             border-image:url('Images/" + var[15][a][index] + "')")

                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(self.label, x, y, rowspan, colspan)
            elif uIndex[i] == 3:               
                txt = labelText[a][index][i]
                btn = QPushButton(txt, self)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btn.clicked.connect(self.open_webbrowser)
                btn.setStyleSheet(Btn_ss)
                btn.setStyleSheet("border-image:url('Images/play.png')")
                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(btn, x, y, rowspan, colspan)
                
            elif uIndex[i] == 4:
                
                wid = self._videoPlayer(var[18][a][index])
                
                x, y, rowspan, colspan = Pos[i]
                grid.addWidget(wid, x, y, rowspan, colspan)
    
    def _videoPlayer(self, vid):
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        
        videoWidget = QVideoWidget()
        videoWidget.setStyleSheet("background:black;")
        
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        self.playButton.setStyleSheet('background:#ccff00; border-radius:9px;')
        
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        
        wid = QGroupBox(self)
        wid.setStyleSheet("QGroupBox{background-color:#111111;\
                            border:0px;\
                            border-radius:10px;}")
        
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        
        wid.setLayout(layout)
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("Videos/" + vid)))
        self.playButton.setEnabled(True)
        return wid
    
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)           
    
    def open_webbrowser(self):
        global Link, index
        url = QUrl(var[16][a][index])
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
        global count
        count = counter        
        action = info_functions

        cartoonlist(self, var[17][count], action, var[0][count], var[7][count],
                    var[8][count], var[11][count], var[6][count], Gradient_clr[count],
                    var[5][count], var[4][count])

class __main__window__(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(1000, 800)
        self.setWindowTitle('Cartoon World')
        self.setWindowIcon(QIcon('Cartoon.ico'))
        self.setWindowOpacity(0.95)
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 1.2.0')
        self.back = QAction(QIcon('Images/back.png'), 'Back', self)
        self.back.setShortcut('Backspace')
        self.back.triggered.connect(self.action_back)

        self.toolbar = self.addToolBar('Back')
        self.toolbar.addAction(self.back)
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