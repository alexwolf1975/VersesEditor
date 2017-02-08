#include "options.h"
#include <QRegExp>
#include <QSettings>

options::options()
{

}

QSettings* options::config = new QSettings("VersesEditor.ini", QSettings::IniFormat);
QRegExp options::expression = QRegExp("[АаЕеЁёИиОоУуЫыЭэЮюЯя]");
