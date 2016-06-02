# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Form implementation generated from reading ui file 'ejemploChido2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
#estados
q0 = 0
q1 = 1
q2 = 2
q3 = 3
q4 = 4
q5 = 5
q6 = 6
q7 = 7
q8 = 8
q9 = 9
q10 = 10
q11 = 11
q13 = 12
q15 = 13
q16 = 14
q17 = 15
q18 = 16
q19 = 17
q20 = 18
q21 = 19
q22 = 20
q23 = 21
q24 = 22
q25 = 23
q26 = 24
q27 = 25
q28 = 26
q29 = 27
q30 = 28
q31 = 29
q32 = 30
q33 = 31
q34 = 32
q35 = 33
q36 = 34
q37 = 35
#tokens
tokenId = 0
tokenNum = 1
tokenPlus = 2
tokenMinus = 3
tokenTimes = 4
tokenDivided = 5
tokenMod = 6
tokenGt = 7
tokenLt = 8
tokenNeg = 9
tokenEq = 10
tokenLEt = 11
tokenGEt = 12
tokenAsig = 13
tokenDif = 14
tokenPrL = 15
tokenPrR = 16
tokenKeyL = 17
tokenKeyR = 18
tokenEnd = 19
tokenComa = 20
tokenInv = 21
RW_SELECT = 22
RW_INT = 23
RW_IF = 24
RW_ELSE = 25
RW_FOR = 26
RW_WHILE = 27
RW_DO = 28
RW_RETURN = 29
RW_STRING = 30
RW_DOUBLE= 31
RW_FLOAT= 32
RW_CHAR=33
RW_BOOLEAN=34
RW_VOID=35
tokenAnd=36
tokenOr=37
tokenCadena=38
RW_SWITCH=39
RW_CASE=40
RW_DEFAULT=41
RW_BREAK=42
tokenAmpersand = 43
tokenVertical = 44
RW_OUT=45
RW_GET=46
#NO_TERMINALES
PROGRAMA=47
DECLARACION=48
FUNCIONVOID=49
ARGUMENTO=50
LISTAARGUMENTOS=51
LISTAARGUMENTOS2=52
FUNCIONDECLARACION=53
FUNCIONDECLARACION2=54
DECLARACIONVARIABLE=55
DECLARACIONVARIABLE2=56
LISTAVARIABLES=57
EXPRESIONARITMETICA=58
EXPRESIONARITMETICA1=59
EXPRESIONARITMETICA2=60
FACTOR=61
CIERREFUNCION=62
INSTRUCCION=63
INSTRUCCION2=64
ESTRUCTURAIDENTIFICADOR=65
LISTAEXPRESIONES=66
ESTRUCTURAIF=67
ESTRUCTURAIF2=68
EXPRESIONCOMPARACION=69
EXPRESIONCOMPARACION1=70
EXPRESIONCOMPARACION2=71
EXPRESIONCOMPARACION3=72
FACTORCOMPARACION=73
CIERREIF=74
POSIBILIDADELSE=75
POSIBILIDADELSE2=76
ESTRUCTURAFOR=77
ESTRUCTURAFOR2=78
ESTRUCTURAFOR3=79
ESTRUCTURAFOR4=80
ESTRUCTURAFOR5=81
CIERREFOR=82
ESTRUCTURADO=83
ESTRUCTURAWHILE=84
LOGICOSWHILE=85
ESTRUCTURASWITCH=86
ESTRUCTURASWITCH2=87
ESTRUCTURASWITCH3=88
OPCIONCASE=89
DECLARACIONVARIABLE3=90
LISTAVARIABLES2=91
ESTRUCTURARETURN=92
CIERREFUNCION2=93
#transiciones
Matrix = [[1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#0
    [1,27,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#1
    [4,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#2
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#3
    [4,4,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#4
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#5
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#6
    [1,2,3,5,21,10,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#7
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#8
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#9
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,0,11,28,11,11,11],#10
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,0,11,28,11,11,11],#11
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#12
    [1,2,3,5,6,7,8,15,16,18,14,9,12,23,24,25,0,0,26,28,29,31,33],#13
    [1,2,3,5,5,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#14
    [1,2,3,5,6,7,8,15,16,18,17,9,12,23,24,25,0,0,26,28,29,31,33],#15
    [1,2,3,5,6,7,8,15,16,18,19,9,12,23,24,25,0,0,26,28,29,31,33],#16
    [1,2,3,5,6,7,8,15,16,18,19,9,12,23,24,25,0,0,26,28,29,31,33],#17
    [1,2,3,5,6,7,8,15,16,18,20,9,12,23,24,25,0,0,26,28,29,31,33],#18
    [1,2,3,5,6,7,8,15,16,18,19,9,12,23,24,25,0,0,26,28,29,31,33],#19
    [1,2,3,5,6,7,8,15,16,18,19,9,12,23,24,25,0,0,26,28,29,31,33],#20
    [21,21,21,21,22,21,21,21,21,21,21,21,21,21,21,21,21,21,21,28,21,21,21],#21
    [21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,28,21,21,21],#22
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#23
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#24
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#25
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#26
    [1,27,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#27
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#28
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,30,31,33],#29
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#30
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,32,33],#31
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33],#32
    [34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,35],#33
    [34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,35],#34
    [1,2,3,5,6,7,8,15,16,18,13,9,12,23,24,25,0,0,26,28,29,31,33]]#35

#tablaSalidas
MatrixOutput = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q0
    [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#q1
    [-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],#q2
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],#q3
    [-1,-1,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21],#q4
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],#q5
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],#q6
    [5,5,5,5,-1,-1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],#q7
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],#q8
    [15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15],#q9
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q10
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q11
    [16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16],#q12
    [13,13,13,13,13,13,13,13,13,13,-1,13,13,13,13,13,13,13,13,13,13,13,13],#q13
    [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],#q14
    [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, -1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],#q15
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, -1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],#q16
    [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11],#q17
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, -1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],#q18
    [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12],#q19
    [14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14],#q20
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q21
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q22
    [17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17],#q23
    [18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18],#q24
    [19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19],#q25
    [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20],#q26
    [-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#q27
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#q28
    [43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-1,43,43],#29
    [36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36],#30
    [44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-1,44],#31
    [37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37],#32
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#33
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#34
    [38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38]]#35

global paReservadas
paReservadas=["select","double","boolean","char","float","void","int",
"string","while","for","do","if","else","switch","break","case","default",
"out","get","return"]

global diccionarioErrores
diccionarioErrores ={0: "Error se esperaba identificador", 53:"Error se esperaba funcion, declaracion o expresion", 1: "Error se esperaba numero", 2: "Error, se esperaba operador aritmetico", 3:"Error se esperaba operador aritmetico", 4:"Error se esperaba operador aritmetico", 5: "Error se esperaba operador aritmetico", 6:"Error se esperaba operador aritmetico", 7:"Error, se esperaba operador comparacion", 8:"Error, se esperaba operador comparacion", 9: "Error, se esperaba operador comparacion", 10:"Error, se esperaba operador comparacion", 11:"Error, se esperaba operador comparacion", 12:"Error, se esperaba operador comparacion", 13:"Error, se esperaba operador comparacion", 14:"Error, se esperaba operador comparacion", 15:"Error, se esperaba parentesis izquierdo", 16:"Error, se esperaba parentesis derecho", 17:"Error, se esperaba llave izquierda", 18:"Error, se esperaba llave derecha", 19:"Error, se esperaba punto y coma", 20:"Error, se esperaba token coma", 21:"Error, token invalido", 22:"Error, se esperaba palabra reservada", 23:"Error, se esperaba palabra reservada",
                     24:"Error, se esperaba palabra reservada", 25:"Error, se esperaba palabra reservada", 26:"Error, se esperaba palabra reservada", 27:"Error, se esperaba palabra reservada", 28:"Error, se esperaba palabra reservada",
                     29:"Error, se esperaba palabra reservada", 30:"Error, se esperaba palabra reservada", 31:"Error, se esperaba palabra reservada", 32:"Error, se esperaba palabra reservada", 33:"Error, se esperaba palabra reservada",
                     34:"Error, se esperaba palabra reservada", 35:"Error, se esperaba palabra reservada", 36:"Error, se esperaba token and", 37: "Error, se esperaba token or", 38: "Error, se esperaba token cadena", 39:"Error, se esperaba palabra reservada",
                     40:"Error, se esperaba palabra reservada", 41:"Error, se esperaba palabra reservada", 42:"Error, se esperaba palabra reservada", 43:"Error, se esperaba ampersand", 44:"Error, se esperaba token vertical",
                     45:"Error, se esperaba palabra reservada", 46:"Error, se esperaba palabra reservada", 48:"Error, se esperaba funcion declaracion o expresion", 49:"Error, se esperaba funcion declaracion o expresion",
                     50:"Error, se esperaba funcion declaracion o expresion", 51:"Error, se esperaba funcion declaracion o expresion", 52:"Error, se esperaba funcion declaracion o expresion", 54:"Error, se esperaba funcion declaracion o expresion",
                     55:"Error, se esperaba funcion declaracion o expresion", 56:"Error, se esperaba funcion declaracion o expresion", 57:"Error, se esperaba funcion declaracion o expresion", 58:"Error, se esperaba funcion declaracion o expresion",
                     59:"Error, se esperaba funcion declaracion o expresion", 60:"Error, se esperaba funcion declaracion o expresion", 61:"Error, se esperaba funcion declaracion o expresion",
                     62:"Error, se esperaba cerrar funcion", 63:"Error, se esperaba funcion, instruccion o expresion", 64:"Error, se esperaba funcion, instruccion o expresion", 65:"Error, se esperaba funcion, instruccion o expresion",
                     66:"Error, se esperaba funcion, instruccion o expresion", 67: "Error, se esperaba cerrar estructura if", 68: "Error, se esperaba cerrar estructura if", 69: "Error en expresion comparacion y factor comparacion" ,
                     70: "Error en expresion comparacion y factor comparacion", 71: "Error en expresion comparacion y factor comparacion", 72: "Error en expresion comparacion y factor comparacion", 73: "Error en expresion comparacion y factor comparacion",
                     74: "Erro se esperaba cierre funcion", 75: "Error en posibilidad de un else", 76: "Error en posibilidad de un else", 77: "Error, error en estructura for",78: "Error, error en estructura for",79: "Error, error en estructura for",80: "Error, error en estructura for",
                     81: "Error, error en estructura for", 82: "Error, error en estructura for", 83: "Error en estructura go",84: "Error en estructura while",85: "Error en estructura while",
                     86: "Error en switch",87: "Error en switch",88: "Error en switch",89: "Error en switch", 90: "Error en declaracion variable 3", 91: "Error en lista variables 2", 92: "Error en return", 93: "Error en cierre de funcion 2"}

global simbolos
simbolos = []
global tokensPro
tokensPro = []
global gramatica
gramatica = []
global fallos



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 1900)
        self.centralWidget = QtWidgets.QWidget(Dialog)
        self.centralWidget.setObjectName("centralWidget")

        self.botonExaminar = QtWidgets.QPushButton(Dialog)
        self.botonExaminar.setGeometry(QtCore.QRect(480, 400, 75, 23))
        self.botonExaminar.setObjectName("botonExaminar")

        self.botonAnalSintactico = QtWidgets.QPushButton(Dialog)
        self.botonAnalSintactico.setGeometry(QtCore.QRect(600, 400, 75, 23))
        self.botonAnalSintactico.setObjectName("botonAnalSintactico")

        self.botonAnalLexico = QtWidgets.QPushButton(Dialog)
        self.botonAnalLexico.setGeometry(QtCore.QRect(720,400,75,23))
        self.botonAnalLexico.setObjectName("botonAnalLexico")

        self.botonSimbTab = QtWidgets.QPushButton(Dialog)
        self.botonSimbTab.setGeometry(QtCore.QRect(730, 120, 95, 23))
        self.botonSimbTab.setObjectName("botonSimTab")

        self.text_generar = QtWidgets.QPlainTextEdit(Dialog)
        self.text_generar.setGeometry(QtCore.QRect(370, 30, 321, 351))
        self.text_generar.setObjectName("text_generar")

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 321, 351))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit3.setGeometry(QtCore.QRect(730, 30, 321, 351))
        self.plainTextEdit3.setObjectName("plainTextEdit3")

        self.plainTextEdit4 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit4.setGeometry(QtCore.QRect(10, 450, 1040, 200))
        self.plainTextEdit4.setObjectName("plainTextEdit4")

        self.botonExaminar.clicked.connect(self.examinarArchivo)
        self.botonAnalSintactico.clicked.connect(self.AnalizarSintaxis)
        self.botonAnalLexico.clicked.connect(self.analizarCadena)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        indio=0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.botonExaminar.setText(_translate("Dialog", "Examinar"))
        self.botonAnalLexico.setText(_translate("Dialog", "Lexico"))
        self.botonAnalSintactico.setText(_translate("Dialog","Sintactico"))
        self.botonSimbTab.setText(_translate("Dialog","Tabla simbolos"))

    def examinarArchivo(self):
        Archivo = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', 'datos.txt')

        if Archivo[0]:
                Contenido = open(Archivo[0], 'r')
                Contenido = Contenido.read() + "\n"
                self.plainTextEdit.setPlainText(str(Contenido))
                self.analizarCadena(Contenido)
                self.AnalizarSintaxis()

    def analizarCadena(self,clinea):
        print(paReservadas[:])
        print("muere?")
        #del tokensPro[:]
        clinea=self.plainTextEdit.toPlainText()+" "
        caracaterCadena=""
        copiaCadena=""
        i=0
        j=0
        tamCad=len(clinea)
        estado=0

        bandera = False;
        for i in range(0,tamCad):
            caracterCadena=clinea[i]
            print("1 CARACTER CADENA = ",caracterCadena)
            print("2 COPIA CADENA = ",copiaCadena)
            print("3 LLEGO A CLASIFICAR CADENA")
            entrada=(self.clasificarCadena(caracterCadena))
            print("Entrada = ",entrada)
            print("Estado = ",estado)
            salida=MatrixOutput[estado][entrada]
            print("SALIDA = ",salida)

            if salida!=-1:

                if salida==0:

                    for j in range(0,len(paReservadas)):
                        if copiaCadena==paReservadas[j]:
                            bandera=True
                            break

                    if bandera:
                        self.TomarReservada(copiaCadena)
                        self.text_generar.appendPlainText(copiaCadena+"   Palabra resevadar")
                        copiaCadena=""
                    else:
                        tokensPro.append(tokenId)
                        self.text_generar.appendPlainText(copiaCadena+"   identificador")
                        self.tabladeSimbolos(copiaCadena)
                        copiaCadena=""
                elif salida==1:
                    tokensPro.append(tokenNum)
                    self.text_generar.appendPlainText(copiaCadena+"   numero")
                    copiaCadena=""
                elif salida==2:
                    tokensPro.append(tokenPlus)
                    self.text_generar.appendPlainText(copiaCadena+"   operador aritmetico suma")
                    copiaCadena=""
                elif salida==3:
                    tokensPro.append(tokenMinus)
                    self.text_generar.appendPlainText(copiaCadena+"   op ar resta")
                    copiaCadena=""
                elif salida==4:
                    tokensPro.append(tokenTimes)
                    self.text_generar.appendPlainText(copiaCadena+"   op multi")
                    copiaCadena=""
                elif salida==5:
                    tokensPro.append(tokenDivided)
                    self.text_generar.appendPlainText(copiaCadena+"   division")
                    copiaCadena=""
                elif salida==6:
                    tokensPro.append(tokenMod)
                    self.text_generar.appendPlainText(copiaCadena+"   Modulo")
                    copiaCadena=""
                elif salida==7:
                    tokensPro.append(tokenGt)
                    self.text_generar.appendPlainText(copiaCadena+"   op mayor que")
                    copiaCadena=""
                elif salida==8:
                    tokensPro.append(tokenLt)
                    self.text_generar.appendPlainText(copiaCadena+"   op menor que ")
                    copiaCadena=""
                elif salida==9:
                    tokensPro.append(tokenNeg)
                    self.text_generar.appendPlainText(copiaCadena+"   op negacion")
                    copiaCadena=""
                elif salida==10:
                    tokensPro.append(tokenEq)
                    self.text_generar.appendPlainText(copiaCadena+"   igual")
                    copiaCadena=""
                elif salida==11:
                    tokensPro.append(tokenLEt)
                    self.text_generar.appendPlainText(copiaCadena+"   op menor igual")
                    copiaCadena=""
                elif salida==12:
                    tokensPro.append(tokenGEt)
                    self.text_generar.appendPlainText(copiaCadena+"   op mayor igual")
                    copiaCadena=""
                elif salida==13:
                    tokensPro.append(tokenAsig)
                    self.text_generar.appendPlainText(copiaCadena+"   asignacion")
                    copiaCadena=""
                elif salida==14:
                    tokensPro.append(tokenDif)
                    self.text_generar.appendPlainText(copiaCadena+"   diferente")
                    copiaCadena=""
                elif salida==15:
                    tokensPro.append(tokenPrL)
                    self.text_generar.appendPlainText(copiaCadena+"   parentesis izquierdo")
                    copiaCadena=""
                elif salida==16:
                    tokensPro.append(tokenPrR)
                    self.text_generar.appendPlainText(copiaCadena+"   parentesis derecho")
                    copiaCadena=""
                elif salida==17:
                    tokensPro.append(tokenKeyL)
                    self.text_generar.appendPlainText(copiaCadena+"   llave izquierda")
                    copiaCadena=""
                elif salida==18:
                    tokensPro.append(tokenKeyR)
                    self.text_generar.appendPlainText(copiaCadena+"   llave derecha")
                    copiaCadena=""
                elif salida==19:
                    tokensPro.append(tokenEnd)
                    self.text_generar.appendPlainText(copiaCadena+"   punto y coma")
                    copiaCadena=""
                elif salida==20:
                    tokensPro.append(tokenComa)
                    self.text_generar.appendPlainText(copiaCadena+"   coma")
                    copiaCadena=""
                elif salida==21:
                    tokensPro.append(tokenInv)
                    self.text_generar.appendPlainText(copiaCadena+"   invalido")
                    copiaCadena=""
                elif salida==36:
                    tokensPro.append(tokenAnd)
                    self.text_generar.appendPlainText(copiaCadena+"...and")
                    copiaCadena=""
                elif salida==37:
                    tokensPro.append(tokenOr)
                    self.text_generar.appendPlainText(copiaCadena+"...or")
                    copiaCadena=""
                elif salida==38:
                    tokensPro.append(tokenCadena)
                    self.text_generar.appendPlainText(copiaCadena+"...cadena")
                    copiaCadena=""
                elif salida==43:
                    tokensPro.append(tokenAmpersand)
                    self.text_generar.appendPlainText(copiaCadena+"...Ampersand")
                    copiaCadena=""
                elif salida==44:
                    tokensPro.append(tokenVertical)
                    self.text_generar.appendPlainText(copiaCadena+"...Vertical")
                    copiaCadena=""
                else:
                    self.text_generar.appendPlainText(copiaCadena+"   error")
                    copiaCadena=""
            estado=Matrix[estado][entrada]

            if (caracterCadena!="\t" and caracterCadena!= " "  and caracterCadena!="\n" and estado!=21 and estado!=10 and estado!=11 and estado!=22):
                print("CONCATENO")
                copiaCadena+=caracterCadena
                print("COPIA CADENA CONCAT",copiaCadena)
                if estado==28:
                    print("Estado error")
                    self.text_generar.appendPlainText(copiaCadena+"   error")
                    copiaCadena=""
            else:
                print("Else FALSE")
                copiaCadena=""
            bandera=False

    def AnalizarSintaxis(self):
        del gramatica[:]
        terminal = 0
        noTerminal = 0
        fallos = 0
        gramatica.insert(0,PROGRAMA)
        while len(gramatica)is not 0:
            print("Valor de gramatica: ",gramatica[:])
            if len(tokensPro)is not 0:
                print("Valor tokens pro ", tokensPro[:])
                noTerminal = self.ClasificarNoTerminales()
                print("Salgo de no terminales pls??")
                #print("gramatica despues de eliminacion: ",gramatica[:])
                terminal = self.ClasificarTerminales()
                print("terminal: ",terminal)
                print("No terminal",noTerminal)
                if  noTerminal==False and terminal==False:
                    self.FuncionErrores(gramatica[0])
                    print("sale del error")
                    gramatica.clear()
                else:
                    print("Entro")
                    noTerminal = 0
                    terminal = 0
                    print("Entro 2")
            else:
                if len(gramatica) is not 1:
                    self.FuncionErrores(gramatica[0])
                    print("sale del error 2")
                    gramatica.clear()
                gramatica.clear()
        if self.plainTextEdit4.toPlainText()=="":
            self.plainTextEdit4.setPlainText("Sintaxis correcta")

    def TomarReservada(self, copiaCadena):
        print("Entra a reservada")
        if (copiaCadena == "void"):
            tokensPro.append(RW_VOID)
        if (copiaCadena == "int"):
            tokensPro.append(RW_INT)
        if (copiaCadena == "if"):
            tokensPro.append(RW_IF)
        if (copiaCadena == "else"):
            tokensPro.append(RW_ELSE)
        if (copiaCadena == "for"):
            tokensPro.append(RW_FOR)
        if (copiaCadena == "while"):
            tokensPro.append(RW_WHILE)
        if (copiaCadena == "do"):
            tokensPro.append(RW_DO)
        if (copiaCadena == "return"):
            tokensPro.append(RW_RETURN)
        if (copiaCadena == "select"):
            tokensPro.append(RW_SELECT)
        if (copiaCadena == "string"):
            tokensPro.append(RW_STRING)
        if (copiaCadena == "double"):
            tokensPro.append(RW_DOUBLE)
        if (copiaCadena == "float"):
            tokensPro.append(RW_FLOAT)
        if (copiaCadena == "char"):
            tokensPro.append(RW_CHAR)
        if (copiaCadena == "boolean"):
            tokensPro.append(RW_BOOLEAN)
        if (copiaCadena == "switch"):
            tokensPro.append(RW_SWITCH)
        if (copiaCadena == "case"):
            tokensPro.append(RW_CASE)
        if (copiaCadena == "default"):
            tokensPro.append(RW_DEFAULT)
        if (copiaCadena == "break"):
            tokensPro.append(RW_BREAK)
        if (copiaCadena == "out"):
            tokensPro.append(RW_OUT)
        if (copiaCadena == "get"):
            tokensPro.append(RW_GET)

    def ClasificarNoTerminales(self):
        print("Ando en clasificar no term")
        print("Valor gramatica???",gramatica[0])
        if (int(gramatica[0]) == DECLARACIONVARIABLE3):
            self.DeclaracionVariable3()
        if gramatica[0] == PROGRAMA:
            return self.Programa()
        if gramatica[0] == DECLARACION:
            return self.Declaracion()
        if gramatica[0] == FUNCIONVOID:
            return self.FuncionVoid()
        if gramatica[0] == ARGUMENTO:
            return self.Argumento()
        if gramatica[0] == LISTAARGUMENTOS:
            return self.ListaArgumentos()
        if gramatica[0] == LISTAARGUMENTOS2:
            return self.ListaArgumentos2()
        if gramatica[0] == FUNCIONDECLARACION:
            return self.FuncionDeclaracion()
        if gramatica[0] == FUNCIONDECLARACION2:
            return self.FuncionDeclaracion2()
        if gramatica[0] == DECLARACIONVARIABLE:
            return self.DeclaracionVariable()
        if gramatica[0] == DECLARACIONVARIABLE2:
            return self.DeclaracionVariable2()


        if gramatica[0] == LISTAVARIABLES:
            return self.ListaVariables()
        if gramatica[0] == EXPRESIONARITMETICA:
            return self.ExpresionAritmetica()
        if gramatica[0] == EXPRESIONARITMETICA1:
            return self.ExpresionAritmetica1()
        if gramatica[0] == EXPRESIONARITMETICA2:
            return self.ExpresionAritmetica2()
        if gramatica[0] == FACTOR:
            return self.Factor()
        if gramatica[0] == CIERREFUNCION:
            return self.CierreFuncion()
        if gramatica[0] == INSTRUCCION:
            print("entra Instruccion")
            return self.Instruccion()
        if gramatica[0] == INSTRUCCION2:
            return self.Instruccion2()
        if gramatica[0] == ESTRUCTURAIDENTIFICADOR:
            return self.EstructuraIdentificador()
        if gramatica[0] == LISTAEXPRESIONES:
            return self.ListaExpresiones()
        if gramatica[0] == ESTRUCTURAIF:
            return self.EstructuraIF()
        if gramatica[0] == ESTRUCTURAIF2:
            return self.EstructuraIF2()
        if gramatica[0] == EXPRESIONCOMPARACION:
            return self.ExpresionComparacion()
        if gramatica[0] == EXPRESIONCOMPARACION1:
            return self.ExpresionComparacion1()
        if gramatica[0] == EXPRESIONCOMPARACION2:
            return self.ExpresionComparacion2()
        if gramatica[0] == EXPRESIONCOMPARACION3:
            return self.ExpresionComparacion3()
        if gramatica[0] == FACTORCOMPARACION:
            return self.FactorComparacion()
        if gramatica[0] == CIERREIF:
            return self.CierreIF()
        if gramatica[0] == POSIBILIDADELSE:
            return self.PosibilidadElse()
        if gramatica[0] == POSIBILIDADELSE2:
            return self.PosibilidadElse2()
        if gramatica[0] == ESTRUCTURAFOR:
            return self.EstructuraFor()
        if gramatica[0] == ESTRUCTURAFOR2:
            return self.EstructuraFor2()
        if gramatica[0] == ESTRUCTURAFOR3:
            return self.EstructuraFor3()
        if gramatica[0] == ESTRUCTURAFOR4:
            return self.EstructuraFor4()
        if gramatica[0] == ESTRUCTURAFOR5:
            return self.EstructuraFor5()
        if gramatica[0] == CIERREFOR:
            return self.CierreFor()
        if gramatica[0] == ESTRUCTURADO:
            return self.EstructuraDo()
        if gramatica[0] == ESTRUCTURAWHILE:
            return self.EstructuraWhile()
        if gramatica[0] == LOGICOSWHILE:
            return self.LogicosWhile()
        if gramatica[0] == ESTRUCTURASWITCH:
            return self.EstructuraSwitch()
        if gramatica[0] == ESTRUCTURASWITCH2:
            return self.EstructuraSwitch2()
        if gramatica[0] == ESTRUCTURASWITCH3:
            return self.EstructuraSwitch3()
        if gramatica[0] == OPCIONCASE:
            return self.OpcionCase()
        if gramatica[0] == DECLARACIONVARIABLE3:
            printf("Declaracion variable 3")
            return self.DeclaracionVariable3()
        if gramatica[0] == LISTAVARIABLES2:
            return self.ListaVariables2()
        if gramatica[0] == ESTRUCTURARETURN:
            return self.EstructuraReturn()
        if gramatica[0] == CIERREFUNCION2:
            return self.CierreFuncion2()
        print("Salgo de no term")
        return 0

    def ClasificarTerminales(self):
        print("contenido del vector: ", tokensPro[:])
        print("contenido de la gramatica", gramatica[:])

        if tokensPro[0] == gramatica[0]:
            tokensPro.pop(0)
            gramatica.pop(0)
            return 1
        return 0
    def Programa(self):
        print("gramatica en el inicio",gramatica[:])
        if tokensPro[0] != 0:
            gramatica.pop(0)
            print("gramatica en el despues", gramatica[:])
            gramatica.insert(0, PROGRAMA)
            gramatica.insert(0, DECLARACION)
            return 1
        gramatica.pop(0)
        return 1

    def Declaracion(self):
        print("entra al Declaracion")
        if tokensPro[0] == RW_VOID:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONVOID)
            gramatica.insert(0, RW_VOID)
            return 1
        if tokensPro[0] == RW_INT:
            gramatica.pop()
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == RW_FLOAT:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_FLOAT)
            return 1
        if tokensPro[0] == RW_STRING:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0, RW_STRING)
            return 1
        if tokensPro[0] == RW_CHAR:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_CHAR)
            return 1
        if tokensPro[0] == RW_DOUBLE:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_DOUBLE)
            return 1
        if tokensPro[0] == RW_BOOLEAN:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_BOOLEAN)
            return 1
        if tokensPro[0] == RW_SELECT:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_SELECT)
            return 1
        return 0

    def FuncionVoid(self):
        print("entra a funcion void?")
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0, CIERREFUNCION)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, ARGUMENTO)
            gramatica.insert(0, tokenPrL)
            gramatica.insert(0, tokenId)
            return 1
        return 0

    def Argumento(self):
        if tokensPro[0] == RW_INT:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == RW_FLOAT:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_FLOAT)
            return 1
        if tokensPro[0] == RW_DOUBLE:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_DOUBLE)
            return 1
        if tokensPro[0] == RW_CHAR:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_CHAR)
            return 1
        if tokensPro[0] == RW_STRING:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_STRING)
            return 1
        if tokensPro[0] == RW_BOOLEAN:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_BOOLEAN)
            return 1
        gramatica.pop(0)
        return 1

    def ListaArgumentos(self):
        if tokensPro[0] == tokenComa:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS2)
            gramatica.insert(0, tokenComa)
            return 1
        gramatica.pop(0)
        return 1

    def ListaArgumentos2(self):
        if tokensPro[0] == RW_INT:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == RW_FLOAT:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_FLOAT)
            return 1
        if tokensPro[0] == RW_DOUBLE:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_DOUBLE)
            return 1
        if tokensPro[0] == RW_CHAR:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_CHAR)
            return 1
        if tokensPro[0] == RW_STRING:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_STRING)
            return 1
        if tokensPro[0] == RW_BOOLEAN:
            gramatica.pop(0)
            gramatica.insert(0, LISTAARGUMENTOS)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_BOOLEAN)
            return 1
        return 0

    def CierreFuncion(self):
        if tokensPro[0] == tokenEnd:
            gramatica.pop(0)
            gramatica.insert(0, tokenEnd)
            return 1
        if tokensPro[0] == tokenKeyL:
            gramatica.pop(0)
            gramatica.insert(0, tokenKeyR);
            gramatica.insert(0, INSTRUCCION);
            gramatica.insert(0, tokenKeyL);
            return 1
        return 0

    def FuncionDeclaracion(self):
        if tokensPro[0] == tokenId:
            gramatica.pop(0);
            gramatica.insert(0,FUNCIONDECLARACION2);
            gramatica.insert(0,tokenId);
            return 1
        return 0

    def FuncionDeclaracion2(self):
        if tokensPro[0] == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0,CIERREFUNCION)
            gramatica.insert(0,tokenPrR)
            gramatica.insert(0,ARGUMENTO)
            gramatica.insert(0,tokenPrL)
            return 1
        gramatica.pop(0)
        gramatica.insert(0,DECLARACIONVARIABLE)
        return 1

    def DeclaracionVariable(self):
        if(tokensPro[0] == tokenEnd ):
            gramatica.pop(0)
            gramatica.insert(0, tokenEnd)
            return 1
        if(tokensPro[0] == tokenAsig ):
            gramatica.pop(0)
            gramatica.insert(0,tokenEnd)
            gramatica.insert(0,LISTAVARIABLES2)
            gramatica.insert(0,EXPRESIONARITMETICA)
            gramatica.insert(0,tokenAsig)
            return 1;
        if(tokensPro[0]==tokenComa):
            gramatica.pop(0)
            gramatica.insert(0,LISTAVARIABLES);
            gramatica.insert(0,tokenComa);
            return 1
        return 0

    def DeclaracionVariable2(self):
        if tokensPro[0] == tokenEnd:
            gramatica.pop(0)
            gramatica.insert(0, tokenEnd)
            return 1
        if tokensPro[0] == tokenAsig:
            gramatica.pop(0)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, LISTAVARIABLES2)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenAsig)
            return 1
        if tokensPro[0] == tokenComa:
            gramatica.pop(0)
            gramatica.insert(0, LISTAVARIABLES)
            gramatica.insert(0, tokenComa)
            return 1
        return 0

    def DeclaracionVariable3(self):
        print("te doy?")
        print(tokensPro[0])
        print(tokenAsig)
        try:
            pass
            #print("-- " + tokensPro.at(0))
            #print("-- "+ tokenComa)
        except Exception as e:
            print("Error " , sys.exc_info())
            raise


        if(tokensPro[0]==tokenAsig):
            gramatica.pop(0)
            gramatica.insert(0,LISTAVARIABLES2)
            gramatica.insert(0,EXPRESIONARITMETICA)
            gramatica.insert(0,tokenAsig)
            return 1
        if(tokensPro[0]==tokenComa):
            gramatica.pop(0)
            gramatica.insert(0, DECLARACIONVARIABLE3)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, tokenComa)
            return 1
        gramatica.pop(0)
        return 1

    def ListaVariables(self):
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0, DECLARACIONVARIABLE2)
            gramatica.insert(0 ,tokenId)
            return 1
        return 0

    def ListaVariables2(self):
        if(tokensPro[0] == tokenComa):
            gramatica.pop(0)
            gramatica.insert(0, DECLARACIONVARIABLE3)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, tokenComa)
            return 1
        gramatica.pop(0)
        return 1

    def ExpresionAritmetica(self):
        gramatica.pop(0)
        gramatica.insert(0, EXPRESIONARITMETICA2)
        gramatica.insert(0, FACTOR)
        return 1

    def ExpresionAritmetica1(self):
        if tokensPro[0] == tokenTimes:
            gramatica.pop(0)
            gramatica.insert(0, FACTOR)
            gramatica.insert(0, tokenTimes)
            return 1
        if tokensPro[0] == tokenDivided:
            gramatica.pop(0)
            gramatica.insert(0, FACTOR)
            gramatica.insert(0, tokenDivided)
            return 1
        if tokensPro[0] == tokenMod:
            gramatica.pop(0)
            gramatica.insert(0, FACTOR)
            gramatica.insert(0, tokenMod)
            return 1
        gramatica.pop(0)
        return 1

    def ExpresionAritmetica2(self):
        if tokensPro[0] == tokenPlus:
            gramatica.pop(0)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenPlus)
            return 1
        if tokensPro[0] == tokenMinus:
            gramatica.pop(0)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenMinus)
            return 1
        gramatica.pop(0)
        return 1

    def Factor(self):
        print("etra a factor")
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0, EXPRESIONARITMETICA1)
            gramatica.insert(0, tokenId)
            return 1
        if tokensPro[0] == tokenNum:
            gramatica.pop(0)
            gramatica.insert(0, EXPRESIONARITMETICA1)
            gramatica.insert(0, tokenNum)
            return 1
        if tokensPro[0] == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenPrL)
            return 1
        return 0

    def Instruccion(self):
        print("murio")
        if tokensPro[0] == RW_VOID:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,FUNCIONVOID)
            gramatica.insert(0,RW_VOID)
            return 1
        if tokensPro[0] == RW_INT:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == RW_FLOAT:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_FLOAT)
            return 1
        if tokensPro[0] == RW_STRING:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_STRING)
            return 1
        if tokensPro[0] == RW_CHAR:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_CHAR)
            return 1
        if tokensPro[0] == RW_DOUBLE:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_DOUBLE)
            return 1
        if tokensPro[0] == RW_BOOLEAN:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_BOOLEAN)
            return 1
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,ESTRUCTURAIDENTIFICADOR)
            gramatica.insert(0,tokenId)
            return 1
        if tokensPro[0] == RW_IF:
            gramatica.pop(0)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, ESTRUCTURAIF)
            gramatica.insert(0, RW_IF)
            return 1
        if tokensPro[0] == RW_FOR:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,ESTRUCTURAFOR)
            gramatica.insert(0,RW_FOR)
            return 1
        if tokensPro[0] == RW_DO:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,ESTRUCTURADO)
            gramatica.insert(0,RW_DO)
            return 1
        if tokensPro[0] == RW_WHILE:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,ESTRUCTURAWHILE)
            gramatica.insert(0,RW_WHILE)
            return 1
        if tokensPro[0] == RW_GET:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,tokenEnd)
            gramatica.insert(0,tokenId)
            gramatica.insert(0,RW_GET)
            return 1
        if tokensPro[0] == RW_OUT:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,tokenEnd)
            gramatica.insert(0,tokenCadena)
            gramatica.insert(0,RW_OUT)
            return 1
        if tokensPro[0] == RW_SWITCH:
            gramatica.pop(0)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,ESTRUCTURASWITCH)
            gramatica.insert(0,RW_SWITCH)
            return 1
        print("murio2")
        gramatica.pop(0)
        return 1

    def Instruccion2(self):
        if tokensPro[0] == FUNCIONVOID:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONVOID)
            gramatica.insert(0,RW_VOID)
            return 1
        if tokensPro[0] == RW_INT:
            gramatica.pop(0)
            gramatica.insert(0, FUNCIONDECLARACION)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == RW_FLOAT:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_FLOAT)
            return 1
        if tokensPro[0] == RW_STRING:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_STRING)
            return 1
        if tokensPro[0] == RW_CHAR:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_CHAR)
            return 1
        if tokensPro[0] == RW_DOUBLE:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_DOUBLE)
            return 1
        if tokensPro[0] == RW_BOOLEAN:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_BOOLEAN)
            return 1
        if tokensPro[0] == RW_SELECT:
            gramatica.pop(0)
            gramatica.insert(0,FUNCIONDECLARACION)
            gramatica.insert(0,RW_SELECT)
            return 1
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0,ESTRUCTURAIDENTIFICADOR)
            gramatica.insert(0,tokenId)
            return 1
        if tokensPro[0] == RW_IF:
            gramatica.pop(0)
            gramatica.insert(0,ESTRUCTURAIF)
            gramatica.insert(0,RW_IF)
            return 0
        if tokensPro[0] == RW_FOR:
            gramatica.pop(0)
            gramatica.insert(0,ESTRUCTURAFOR)
            gramatica.insert(0,RW_FOR)
            return 1
        if tokensPro[0]== RW_DO:
            gramatica.pop(0)
            gramatica.insert(0,ESTRUCTURADO)
            gramatica.insert(0,RW_DO)
            return 1
        if tokensPro[0]== RW_WHILE:
            gramatica.pop(0)
            gramatica.insert(0,ESTRUCTURAWHILE)
            gramatica.insert(0,RW_WHILE)
            return 1
        gramatica.pop(0)
        return 1

    def EstructuraIdentificador(self):

        if tokensPro[0] == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0,tokenEnd)
            gramatica.insert(0,LISTAEXPRESIONES)
            gramatica.insert(0,EXPRESIONARITMETICA)
            gramatica.insert(0,tokenPrL)
            return 1
        if tokensPro[0] == tokenAsig:
            gramatica.pop(0)
            gramatica.insert(0,tokenEnd)
            gramatica.insert(0,EXPRESIONARITMETICA)
            gramatica.insert(0,tokenAsig)
            return 1
        return 0

    def ListaExpresiones(self):
        if tokensPro[0]  == tokenComa:
            gramatica.pop(0)
            gramatica.insert(0,LISTAEXPRESIONES)
            gramatica.insert(0,EXPRESIONARITMETICA)
            gramatica.insert(0,tokenComa)
            return 1
        gramatica.pop(0)
        return 1

    def EstructuraIF(self):
        if tokensPro[0] == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0,CIERREIF)
            gramatica.insert(0,tokenPrR)
            gramatica.insert(0,EXPRESIONCOMPARACION3)
            gramatica.insert(0,ESTRUCTURAIF2)
            gramatica.insert(0,tokenPrL)
            return 1
        return 0

    def EstructuraIF2(self):
        if tokensPro== tokenNeg:
            gramatica.insert(0,tokenPrR)
            gramatica.insert(0,EXPRESIONCOMPARACION)
            gramatica.insert(0,tokenPrL)
            gramatica.insert(0,tokenNeg)
            return 1
        gramatica.pop(0)
        gramatica.insert(0,EXPRESIONCOMPARACION)
        return 1

    def ExpresionComparacion(self):
        gramatica.pop(0)
        gramatica.insert(0,EXPRESIONCOMPARACION2)
        gramatica.insert(0,FACTORCOMPARACION)
        return 1

    def ExpresionComparacion1(self):
        if tokensPro[0]==tokenGt:
            gramatica.pop(0)
            gramatica.insert(0,FACTORCOMPARACION)
            gramatica.insert(0,tokenGt)
            return 1
        if tokensPro[0]==tokenLt:
            gramatica.pop(0)
            gramatica.insert(0,FACTORCOMPARACION)
            gramatica.insert(0,tokenLt)
            return 1
        if tokensPro[0]==tokenGEt:
            gramatica.pop(0)
            gramatica.insert(0,FACTORCOMPARACION)
            gramatica.insert(0,tokenGEt)
            return 1
        if tokensPro[0]==tokenLEt:
            gramatica.pop(0)
            gramatica.insert(0,FACTORCOMPARACION)
            gramatica.insert(0,tokenLEt)
            return 1
        gramatica.pop(0)
        return 1
    def ExpresionComparacion2(self):
        if tokensPro[0]==tokenEq:
            gramatica.pop(0)
            gramatica.insert(0,EXPRESIONCOMPARACION)
            gramatica.insert(0,tokenEq)
            return 1
        if tokensPro[0]==tokenDif:
            gramatica.pop(0)
            gramatica.insert(0,EXPRESIONCOMPARACION)
            gramatica.insert(0,tokenDif)
            return 1
        gramatica.pop(0)
        return 1

    def ExpresionComparacion3(self):
        if tokensPro[0]==tokenOr:
            gramatica.pop(0)
            gramatica.insert(0,EXPRESIONCOMPARACION3)
            gramatica.insert(0,ESTRUCTURAIF2)
            gramatica.insert(0,tokenOr)
            return 1
        if tokensPro[0]==tokenAnd:
            gramatica.pop(0)
            gramatica.insert(0,EXPRESIONCOMPARACION3)
            gramatica.insert(0,ESTRUCTURAIF2)
            gramatica.insert(0,tokenAnd)
            return 1
        gramatica.pop(0)
        return 1

    def FactorComparacion(self):
        if tokensPro==tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0,tokenPrR)
            gramatica.insert(0,EXPRESIONCOMPARACION)
            gramatica.insert(0,tokenPrL)
            return 1
        gramatica.pop(0)
        gramatica.insert(0,EXPRESIONCOMPARACION1)
        gramatica.insert(0,EXPRESIONARITMETICA)
        return 1

    def CierreIF(self):
        if tokensPro[0]==tokenKeyL:
            gramatica.pop(0)
            gramatica.insert(0,POSIBILIDADELSE)
            gramatica.insert(0,tokenKeyR)
            gramatica.insert(0,INSTRUCCION)
            gramatica.insert(0,tokenKeyL)
            return 1
        gramatica.pop(0)
        gramatica.insert(0,POSIBILIDADELSE)
        gramatica.insert(0,INSTRUCCION2)
        return 1

    def PosibilidadElse(self):
        if tokensPro[0] == RW_ELSE:
            gramatica.pop(0)
            gramatica.insert(0, POSIBILIDADELSE2)
            gramatica.insert(0, RW_ELSE)
            return 1
        gramatica.pop(0)
        return 1

    def PosibilidadElse2(self):
        if tokensPro == tokenKeyL:
            gramatica.pop(0)
            gramatica.insert(0, tokenKeyR)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, tokenKeyL)
            return 1
        gramatica.pop(0)
        gramatica.insert(0, INSTRUCCION2)
        return 1

    def EstructuraFor(self):
        if tokensPro == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0, CIERREFOR)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, ESTRUCTURAFOR2)
            gramatica.insert(0, tokenPrL)
            return 1
        return 0

    def EstructuraFor2(self):
        if tokensPro == RW_INT:
            gramatica.pop(0)
            gramatica.insert(0, ESTRUCTURAFOR3)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenAsig)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, RW_INT)
            return 1
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0, ESTRUCTURAFOR3)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenAsig)
            gramatica.insert(0, tokenId)
            return 1
        return 0

    def EstructuraFor3(self):
        gramatica.pop(0)
        gramatica.insert(0, ESTRUCTURAFOR4)
        gramatica.insert(0, tokenEnd)
        gramatica.insert(0, EXPRESIONCOMPARACION)
        return 1

    def EstructuraFor4(self):
        gramatica.pop(0)
        gramatica.insert(0, ESTRUCTURAFOR5)
        gramatica.insert(0, tokenId)
        return 1

    def EstructuraFor5(self):
        if tokensPro[0] == tokenAsig:
            gramatica.pop(0)
            gramatica.insert(0, EXPRESIONARITMETICA)
            gramatica.insert(0, tokenAsig)
            return 1
        if tokensPro[0] == tokenPlus:
            gramatica.pop(0)
            gramatica.insert(0, tokenPlus)
            gramatica.insert(0, tokenPlus)
            return 1
        if tokensPro[0] == tokenMinus:
            gramatica.pop(0)
            gramatica.insert(0, tokenMinus)
            gramatica.insert(0, tokenMinus)
            return 1
        return 0

    def CierreFor(self):
        if tokensPro[0] == tokenKeyL:
            gramatica.pop(0)
            gramatica.insert(0, tokenKeyR)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, tokenKeyL)
            return 1
        gramatica.pop(0)
        gramatica.insert(0, INSTRUCCION2)
        return 1

    def EstructuraDo(self):
        if tokensPro[0] == tokenKeyL:
            gramatica.pop(0)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, LOGICOSWHILE)
            gramatica.insert(0, EXPRESIONCOMPARACION)
            gramatica.insert(0, tokenPrL)
            gramatica.insert(0, RW_WHILE)
            gramatica.insert(0, tokenKeyR)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, tokenKeyL)
            return 1
        return 0

    def EstructuraWhile(self):
        if tokensPro[0] == tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0, tokenKeyR)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, tokenKeyL)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, LOGICOSWHILE)
            gramatica.insert(0, EXPRESIONCOMPARACION)
            gramatica.insert(0, tokenPrL)
            return 1
        return 0

    def LogicosWhile(self):
        if tokensPro[0] == tokenOr:
            gramatica.pop(0)
            gramatica.insert(0, LOGICOSWHILE)
            gramatica.insert(0, EXPRESIONCOMPARACION)
            gramatica.insert(0, tokenOr)
            return 1
        if tokensPro[0] == tokenAnd:
            gramatica.pop(0)
            gramatica.insert(0, LOGICOSWHILE)
            gramatica.insert(0, EXPRESIONCOMPARACION)
            gramatica.insert(0, tokenEnd)
            return 1
        return 0
    def EstructuraSwitch(self):
        if tokensPro[0]==tokenPrL:
            gramatica.pop(0)
            gramatica.insert(0, tokenKeyR)
            gramatica.insert(0, ESTRUCTURASWITCH2)
            gramatica.insert(0, tokenKeyL)
            gramatica.insert(0, tokenPrR)
            gramatica.insert(0, tokenId)
            gramatica.insert(0, tokenPrL)
            return 1
        return 0

    def EstructuraSwitch2(self):
        if tokensPro[0] == RW_CASE:
            gramatica.pop(0)
            gramatica.insert(0, ESTRUCTURASWITCH3)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, RW_BREAK)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, OPCIONCASE)
            gramatica.insert(0, RW_CASE)
            return 1
        return 0

    def EstructuraSwitch3(self):
        if tokensPro[0] == RW_CASE:
            gramatica.pop(0)
            gramatica.insert(0, ESTRUCTURASWITCH3)
            gramatica.insert(0, tokenEnd)
            gramatica.insert(0, RW_BREAK)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, OPCIONCASE)
            gramatica.insert(0, RW_CASE)
            return 1
        if tokensPro[0]==RW_DEFAULT:
            gramatica.pop(0)
            gramatica.insert(0, RW_BREAK)
            gramatica.insert(0, INSTRUCCION)
            gramatica.insert(0, RW_DEFAULT)
            return 1
        gramatica.pop(0)
        return 1

    def OpcionCase(self):
        if tokensPro[0] == tokenId:
            gramatica.pop(0)
            gramatica.insert(0, tokenId)
            return 1
        if tokensPro[0] == tokenNum:
            gramatica.pop(0)
            gramatica.insert(0, tokenNum)
            return 1
        return 0

    def FuncionErrores(self, fail):
        print("Valor fail", fail)
        self.plainTextEdit4.setPlainText(diccionarioErrores[fail])
        del gramatica[:]
        fail = 0

        '''   print("entra a Errores")
   print("Fail: ", fail)
   try:
       if int(fail) == 53:
           print("mevoy")
       #pass
       print("-- ", fail)
   except Exception as e:
       print("Error ", sys.exc_info())
       raise
   if fail == 0:

       print("Error se esperaba identificador")
       self.plainTextEdit4.setPlainText("Error se esperaba identificador")
       print("Grammar", gramatica[:])
       del gramatica[:]

   elif fail == 1:

       print("Error se esperaba numero")
       self.plainTextEdit4.setPlainText("Error se esperaba numero")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 2 or fail == 3 or fail == 4 or fail == 5 or fail == 6:

       print("Error se esperaba Op aritmetica")
       self.plainTextEdit4.setPlainText("Error se esperaba Op aritmetica")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 7 or fail == 8 or fail == 9 or fail == 10 or fail == 11 or fail == 12 or fail == 13 or fail == 14:

       print("Error se esperaba OP comparacion")
       self.plainTextEdit4.setPlainText("Error se esperaba Op comparacion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 15 or fail == 16:

       print("Error se esperaba parentesis")
       self.plainTextEdit4.setPlainText("Error se esperaba Parentesis ")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 17 or fallos == 18:

       print("Error se esperaba llaves")
       self.plainTextEdit4.setPlainText("Error se esperaba Llaves")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 19:

       print("Error se esperaba punto y coma")
       self.plainTextEdit4.setPlainText("Error se esperaba punto y coma")
       print("Grammar", gramatica[:])
       del gramatica[:]

   elif fail == 53:

       print("Error se esperaba punto y coma")
       self.plainTextEdit4.setPlainText("Error se esperaba punto y coma")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 20:

       print("Error se esperaba coma")
       self.plainTextEdit4.setPlainText("Error se esperaba Coma")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 21:

       print("Error token invalido")
       self.plainTextEdit4.setPlainText("Error token invalido")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 22 or fail == 23 or fail == 24 or fail == 25 or fail == 26 or fail == 27 or fail == 28 or fail == 29 or fail == 30 or fail == 31 or fail == 32 or fail == 33 or fail == 34 or fail == 35:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba Palabra REservada")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 39 or fail == 40 or fail == 41 or fail == 42:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba palabra reservada")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 45 or fail == 46:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba palabra reservada")
       print("Grammar", gramatica[:])
       del gramatica[:]


   elif (fail == 48) or (fail == 49) or (fail == 50) or (fail == 51) or (fail == 52) or (fail[0] == 53) or (fail == 54) or (fail == 55) or (fail == 56) or (fail == 57) or (fail == 58) or (fail == 59) or (fail == 60) or (fail == 61):

       print("Muere")
       print("Error se esperaba funcion, declaracion o expresion")
       self.plainTextEdit4.setPlainText("Error se esperaba Funcion, decalracio o expresion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 62:

       print("Error se esperaba cerrar la funcion")
       self.plainTextEdit4.setPlainText("Error se esperaba Cerrar la funcion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 63 or fail == 64 or fail == 65 or fail == 66:

       print("Error se esperaba funcion, instruccion2 o expresion")
       self.plainTextEdit4.setPlainText("Error se esperaba Funcion, instruccion2 o expresion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 67 or fail == 68:

       print("Error en estructura if")
       self.plainTextEdit4.setPlainText("Error em estructura if")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 70 or fail == 71 or fail == 72 or fail == 73:

       print("Error en expresion comparacion y factor comparacion")
       self.plainTextEdit4.setPlainText("Error en expresion comparacion y factor comparacion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 74:

       print("Error se esperaba cierre if")
       self.plainTextEdit4.setPlainText("Error se esperaba cierre if")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 75 or fail == 76:

       print("Error posibilidad else")
       self.plainTextEdit4.setPlainText("Error posibilidad else")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 77 or fail == 78 or fail == 79 or fail == 80 or fail == 81 or fail == 82:

       print("Error estructura for")
       self.plainTextEdit4.setPlainText("Error estructura for")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 83:

       print("Error en estructura do")
       self.plainTextEdit4.setPlainText("Error en estructura do")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 84 or fail == 85:

       print("Error en estructura while")
       self.plainTextEdit4.setPlainText("Error en estructura while")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 86 or fail == 87 or fail == 88 or fail == 89:

       print("Error en el switch")
       self.plainTextEdit4.setPlainText("Error en el switch")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 90:

       print("Error declaracionvar3")
       self.plainTextEdit4.setPlainText("Error declaracionvar3")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 91:

       print("Error se esoeraba listavar2")
       self.plainTextEdit4.setPlainText("Error se esperaba listavar2")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 92:

       print("Error en el return")
       self.plainTextEdit4.setPlainText("Error en el return")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 93:

       print("Error cierre funcion 02")
       self.plainTextEdit4.setPlainText("Error cierrefuncion 02")
       print("Grammar", gramatica[:])
       del gramatica[:]
       print("entra a Errores")
       print("Fail: ",fail)
   if fail == 0:

       print("Error se esperaba identificador")
       self.plainTextEdit4.setPlainText("Error se esperaba identificador")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 1:

       print("Error se esperaba numero")
       self.plainTextEdit4.setPlainText("Error se esperaba numero")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 2 or fail == 3 or fail == 4 or fail == 5 or fail == 6:

       print("Error se esperaba Op aritmetica")
       self.plainTextEdit4.setPlainText("Error se esperaba Op aritmetica")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 7 or fail == 8 or fail == 9 or fail == 10 or fail == 11 or fail == 12 or fail == 13 or fail == 14:

       print("Error se esperaba OP comparacion")
       self.plainTextEdit4.setPlainText("Error se esperaba Op comparacion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 15 or fail == 16:

       print("Error se esperaba parentesis")
       self.plainTextEdit4.setPlainText("Error se esperaba Parentesis ")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 17 or fallos == 18:

       print("Error se esperaba llaves")
       self.plainTextEdit4.setPlainText("Error se esperaba Llaves")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 19:

       print("Error se esperaba punto y coma")
       self.plainTextEdit4.setPlainText("Error se esperaba punto y coma")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 20:

       print("Error se esperaba coma")
       self.plainTextEdit4.setPlainText("Error se esperaba Coma")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 21:

       print("Error token invalido")
       self.plainTextEdit4.setPlainText("Error token invalido")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 22 or fail == 23 or fail == 24 or fail == 25 or fail == 26 or fail == 27 or fail == 28 or fail == 29 or fail == 30 or fail == 31 or fail == 32 or fail == 33 or fail == 34 or fail == 35:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba Palabra REservada")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 39 or  fail == 40 or fail == 41 or fail == 42:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba palabra reservada")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 45 or fail == 46:

       print("Error se esperaba palabra reservada")
       self.plainTextEdit4.setPlainText("Error se esperaba palabra reservada")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 48 or fail == 49 or fail == 50 or fail == 51 or fail == 52 or fail == 53 or fail == 54 or fail == 55 or fail == 56 or fail == 57 or fail == 58 or fail == 59 or fail == 60 or fail == 61:

       print("Muere")
       print("Error se esperaba funcion, declaracion o expresion")
       self.plainTextEdit4.setPlainText("Error se esperaba Funcion, decalracio o expresion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 62:

       print("Error se esperaba cerrar la funcion")
       self.plainTextEdit4.setPlainText("Error se esperaba Cerrar la funcion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail >= 63 or fail == 64 or fail == 65 or  fail <= 66:

       print("Error se esperaba funcion, instruccion2 o expresion")
       self.plainTextEdit4.setPlainText("Error se esperaba Funcion, instruccion2 o expresion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 67 or fail == 68:

       print("Error en estructura if")
       self.plainTextEdit4.setPlainText("Error em estructura if")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail >= 70 or fail == 71 or fail == 72 or fail <= 73:

       print("Error en expresion comparacion y factor comparacion")
       self.plainTextEdit4.setPlainText("Error en expresion comparacion y factor comparacion")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 74:

       print("Error se esperaba cierre if")
       self.plainTextEdit4.setPlainText("Error se esperaba cierre if")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 75 or fail == 76:

       print("Error posibilidad else")
       self.plainTextEdit4.setPlainText("Error posibilidad else")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 77 or fail == 78 or fail == 79 or fail == 80 or fail == 81 or fail == 82:

       print("Error estructura for")
       self.plainTextEdit4.setPlainText("Error estructura for")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 83:

       print("Error en estructura do")
       self.plainTextEdit4.setPlainText("Error en estructura do")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 84 or fail == 85:

       print("Error en estructura while")
       self.plainTextEdit4.setPlainText("Error en estructura while")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 86 or fail == 87 or fail == 88 or fail == 89:

       print("Error en el switch")
       #self.plainTextEdit4.setPlainText("Error en el switch")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 90:

       print("Error declaracionvar3")
       #self.plainTextEdit4.setPlainText("Error declaracionvar3")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 91:

       print("Error se esoeraba listavar2")
       #self.plainTextEdit4.setPlainText("Error se esperaba listavar2")
       print("Grammar", gramatica[:])
       del gramatica[:]
   elif fail == 92:

       print("Error en el return")
       #self.plainTextEdit4.setPlainText("Error en el return")
       print("Grammar",gramatica[:])
       del gramatica[:]
   elif fail == 93:

       print("Error cierre funcion 02")
       #self.plainTextEdit4.setPlainText("Error cierrefuncion 02")
       print("Grammar",gramatica[:])
       del gramatica[:]'''
    def clasificarCadena(self, sim):

        if (sim >= "a" and sim <= "z"):
            return 0

        elif(sim>="A" and sim<="Z"):
            return 0

        elif sim=="_":
            return 0

        elif(sim>="0" and sim<="9"):
            return 1

        elif(sim=="+"):
            return 2

        elif(sim=="-"):
            return 3

        elif(sim=="*"):
            return 4

        elif(sim=="/"):
            return 5

        elif(sim=="%"):
            return 6

        elif(sim=="<"):
            return 7

        elif(sim==">"):
            return 8

        elif(sim=="!"):
            return 9

        elif(sim=="="):
            return 10

        elif(sim=="("):
            return 11

        elif(sim==")"):
            return 12

        elif(sim=="{"):
            return 13

        elif(sim=="}"):
            return 14

        elif(sim==";"):
            return 15

        elif(sim==" " or sim=="\t"):
            return 16

        elif(sim=="\n"):
            return 17

        elif(sim==","):
            return 18

        elif(sim=="&"):
            return 20

        elif(sim=="|"):
            return 21

        elif(sim=="'"):
            return 22

        else:
            return 19

    def tabladeSimbolos(self, copiaCadena):
        print("Entro a tabla de simbolos")
        bandera = False
        i = 0
        if len(simbolos) == 0:
            simbolos.append(copiaCadena)
        else:
            while i<len(simbolos):
                if simbolos[i] == copiaCadena:
                    self.plainTextEdit3.setPlainText(str(simbolos))
                    bandera=True
                i+=1
            if bandera == False:

                simbolos.append(copiaCadena)

                self.plainTextEdit3.setPlainText(str(simbolos))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
