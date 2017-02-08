#include "aboutdialog.h"
#include "libraries.h"
#include "mainwindow.h"
#include "options.h"
#include "ui_mainwindow.h"
#include "vowelhighlighter.h"
#include <QColor>
#include <QColorDialog>
#include <QFileDialog>
#include <QTextStream>
#include <QTextBlock>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    cnf = new options();
    highlight = new VowelHighlighter(ui->text->document(), cnf);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_Open_triggered()
{
    QString FileName = QFileDialog::getOpenFileName(this, "Открыть", "", "*.txt");
    if (!FileName.isEmpty())
    {
        QFile file(FileName);
        file.open(QIODevice::ReadOnly);
        QTextStream in(&file);
        ui->text->setPlainText(in.readAll());
        file.close();
    }
}

void MainWindow::on_Save_triggered()
{
    QString FileName = QFileDialog::getSaveFileName(this, "Сохранить", "стихи.txt", "*.txt");
    if (!FileName.isEmpty())
    {
        QFile file(FileName);
        file.open(QIODevice::WriteOnly);
        QTextStream out(&file);
        out << ui->text->toPlainText();
        file.close();
    }
}

void MainWindow::on_Color_triggered()
{
    QColor colorTmp = QColorDialog::getColor(highlight->color, this);
    if (colorTmp.isValid())
    {
        highlight->color = colorTmp;
        cnf->config->setValue("DEFAULT/color", QString::number(highlight->color.rgba(), 16).toUpper());
        highlight->rehighlight();
    }
}

void MainWindow::on_text_textChanged()
{
    QTextDocument *document = ui->text->document();
    if (document->lineCount() != lineCount)
    {
        QString numbers;
        QString counts;
        int N = document->blockCount();
        for (int k=0; k<N; k++)
        {
            numbers.append( QString("%1\n").arg(k+1));
            QTextBlock block = document->findBlockByNumber(k);
            QString text = block.text();
            counts.append(text == "" ? "\n" : QString("%1\n").arg(VowelCount(text, cnf->expression)));
            for (int m=0; m < block.lineCount()-1; m++)
            {
                numbers.append("\n");
                counts.append("\n");
            }
        }
        ui->number->setText(numbers);
        ui->count->setText(counts);
        lineCount = document->lineCount();
    }
}

void MainWindow::on_About_triggered()
{
    AboutDialog ad(this);
    ad.exec();
}

void MainWindow::resizeEvent(QResizeEvent *event)
{
    on_text_textChanged();
}
