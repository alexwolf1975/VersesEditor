#-------------------------------------------------
#
# Project created by QtCreator 2017-02-01T13:38:34
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = VersesEditor
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    vowelhighlighter.cpp \
    options.cpp \
    libraries.cpp \
    aboutdialog.cpp

HEADERS  += mainwindow.h \
    libraries.h \
    vowelhighlighter.h \
    options.h \
    aboutdialog.h

FORMS    += mainwindow.ui \
    aboutdialog.ui
