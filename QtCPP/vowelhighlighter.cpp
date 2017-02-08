#include "options.h"
#include "vowelhighlighter.h"
#include <QString>
#include <QSyntaxHighlighter>
#include <QTextCharFormat>

VowelHighlighter::VowelHighlighter(QTextDocument *document, options *config) :
    QSyntaxHighlighter(document)
{
    cnf = config;
    bool ok;
    QColor colorTmp = QColor(cnf->config->value("DEFAULT/color", "").toString().toUInt(&ok, 16));
    if (ok && colorTmp.isValid())
        color = colorTmp;
    else
        color = QColor(0, 160, 0);
}

void VowelHighlighter::highlightBlock(const QString &text)
{
    QTextCharFormat TextFormat = QTextCharFormat();
    TextFormat.setForeground(color);
    int index = cnf->expression.indexIn(text);
    while (index >= 0)
    {
        index = cnf->expression.pos();
        int length = cnf->expression.cap().length();
        setFormat(index, length, TextFormat);
        index = cnf->expression.indexIn(text, index + length);
    }
}
