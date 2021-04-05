#ifndef OPTIONS_H
#define OPTIONS_H

#include <QRegularExpression>
#include <QSettings>

class options
{
public:

    options();
    static QSettings* config;
    static QRegularExpression expression;

};

#endif // OPTIONS_H
