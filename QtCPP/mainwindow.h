#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "libraries.h"
#include "options.h"
#include "vowelhighlighter.h"
#include <QMainWindow>

namespace Ui
{
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
private slots:
    void on_Open_triggered();

    void on_Save_triggered();

    void on_Color_triggered();

    void on_text_textChanged();

    void resizeEvent(QResizeEvent *event);

    void on_About_triggered();

private:
    Ui::MainWindow *ui;
    options *cnf;
    VowelHighlighter *highlight;
    int lineCount;
};

#endif // MAINWINDOW_H
