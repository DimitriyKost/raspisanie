import item as item
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import sys
import pyperclip

sg.theme('DarkGrey2')


def pars(file_htm):
    # парсинг расписания сохраненного в ворде в формате HTM с фильтром
    # отсеиваем остальное ненужное.
    # данные для формирования таблицы
    txtR = "<table border='1'>\n\t<tbody>\n\t\t<tr>\n\
                <td style='text-align: center;' colspan='2' align='center' width='10%'><span style='font-size: 14pt;'>Дата</span></td>\n\
                <td style='text-align: center;' width='50%'><span style='font-size: 14pt;'>Память святого или события</span></td>\n\
                <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Утро</span></td>\n\
                <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Вечер</span></td>\n\
            </tr>\n"
    txtH = "            <td style='text-align: center;'><span style='font-size: 14pt;'>"
    txtE = "</td>\n"

    # читаем файл и парсим его
    with open(file_htm, 'r') as f:
        html = BeautifulSoup(f.read(), 'html.parser')
    # выделяем только строки с таблицы
    pars1 = html.findAll('tr')
    for i in range(len(pars1)):
        pars2 = pars1[i].findAll('td')
        txtR += "\t\t<tr>\n"
        ttx = " "
        for j in range(len(pars2)):
            it = pars2[j].findAll('span')
            tc = pars2[j].span.get('style')
            tcc = tc.find('color')
            txtR += "\t\t\t<td>"
            for dat in it:
                tt = dat.text
                tt = tt.replace('\n ', ' ')
                tt = tt.replace('  ', ' ')
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
    txtR += "\t</tbody>\n</table>"
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
