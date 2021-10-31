from bs4 import BeautifulSoup
import PySimpleGUI as sg
import sys
import pyperclip

sg.theme('DarkGrey2')


def pars(file_htm):
    # парсинг расписания сохраненного в ворде в формате HTM с фильтром
    # отсеиваем остальное ненужное.
    # данные для формирования таблицы
    txtR = "<p style='text-align: center;'><span style='color: #ff0000;'><strong>На мобильных устройствах расписание можно двигать как по вертикали, так и по горизонтали.</strong></span></p>\
<div style='max-width: 100%; overflow: scroll;'>\n\
<table border='1'>\n\t<tbody>\n\t\t<tr>\n\
\t\t\t<td style='text-align: center;' colspan='2' align='center' width='10%'><span style='font-size: 14pt;'>Дата</span></td>\n\
\t\t\t<td style='text-align: center;' width='50%'><span style='font-size: 14pt;'>Память святого или события</span></td>\n\
\t\t\t<td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Утро</span></td>\n\
\t\t\t<td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Вечер</span></td>\n\
\t\t</tr>\n"
    txtH = "\t\t\t<td style='text-align: center;'><span style='font-size: 14pt;'>"
    txtE = "</td>\n"

    # читаем файл и парсим его
    with open(file_htm, 'r') as f:
        html = BeautifulSoup(f.read(), 'html.parser')
    # выделяем только строки с таблицы
    pars1 = html.findAll('tr')
    for i in range(len(pars1)):
        pars2 = pars1[i].findAll('td')
        txtR += "\t\t<tr>\n"
        #ttx = " "
        for j in range(len(pars2)):
            it = pars2[j].findAll('span')
            txtR += "\t\t\t<td style='text-align: center; font-size: 14pt;'>"
            for dat in it:
                tt = dat.text
                tt = tt.replace('\n ', ' ')
                for uy in range(15):
                    tt = tt.replace(u'\xa0', u' ')
                    tt = tt.replace('  ', ' ')
                tt = tt.replace('Литургия', 'Литургия<br>')
                tt = tt.replace('Утреня.', 'Утреня.<br>')
                tc = dat.get('style')
                tcc = tc.find('color')
                if tcc != -1:
                    color = tc[tc.find('color:') + 6:]
                    if color == "black":
                        txtR += tt
                    else:
                        txtR += "<span style='color:" + color + "'>" + tt + "</span>"
                else:
                    txtR += tt
            txtR += "</td>\n"
        txtR += "\t\t</tr>\n"
    txtR += "\t</tbody>\n</table>\n</div>"
    return txtR


layout = [[sg.Text('Файл расписания: '), sg.Text(size=(25, 1), key='-OUTPUT-')],
          [sg.Button('Выбрать файл', size=(20, 2)), sg.Button('Конвертировать', size=(20, 2))]]

window = sg.Window('Чистильщик', layout)
while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Выбрать файл':
        if len(sys.argv) == 1:
            fname = sg.popup_get_file('Выберите файл')
        else:
            fname = sys.argv[1]
        window['-OUTPUT-'].update(fname)
        if not fname:
            sg.popup("Cancel", "Не выбрали файл")
            raise SystemExit("Cancelling: no filename supplied")
        file = fname
    if event == 'Конвертировать':
        textt = pars(file)
        sg.popup_scrolled(textt, title="Текст после очистки", size=(120, 40))
        pyperclip.copy(textt)
        sg.popup("Очищенный текст скопирован в буфер обмена")

window.close()
