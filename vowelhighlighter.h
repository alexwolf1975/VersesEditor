#ifndef VOWELHIGHLIGHTER_H
#define VOWELHIGHLIGHTER_H

#include "options.h"
#include <QColor>
#include <QString>
#include <QSyntaxHighlighter>

class VowelHighlighter : public QSyntaxHighlighter
{

public:

    QColor color;
    options *cnf;
    VowelHighlighter(QTextDocument *document, options *config);

private:

    void highlightBlock(const QString &text);

};

#endif // VOWELHIGHLIGHTER_H
