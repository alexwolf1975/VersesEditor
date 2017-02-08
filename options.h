#ifndef OPTIONS_H
#define OPTIONS_H

#include <QRegExp>
#include <QSettings>

class options
{
public:

    options();
    static QSettings* config;
    static QRegExp expression;

};

#endif // OPTIONS_H
