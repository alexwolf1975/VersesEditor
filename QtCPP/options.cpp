#include "options.h"
#include <QRegularExpression>
#include <QSettings>

options::options()
{

}

QSettings* options::config = new QSettings("VersesEditor.ini", QSettings::IniFormat);
QRegularExpression options::expression = QRegularExpression("[АаЕеЁёИиОоУуЫыЭэЮюЯя]");
