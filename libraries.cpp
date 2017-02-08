#include "libraries.h"

int VowelCount(QString s, QRegExp expression)
{
    int count = 0;
    int index = expression.indexIn(s);
    while (index >= 0)
    {
        index = expression.pos();
        int length = expression.cap().length();
        count += length;
        index = expression.indexIn(s, index + length);
    }
    return count;
}
