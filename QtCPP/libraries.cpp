#include "libraries.h"

int VowelCount(QString s, QRegularExpression expression)
{
    int count = 0;
    QRegularExpressionMatch match = expression.match(s);
    int index = match.capturedStart();
    while (index >= 0)
    {
        count += match.capturedLength();
        match = expression.match(s, match.capturedEnd());
        index = match.capturedStart();
    }
    return count;
}
