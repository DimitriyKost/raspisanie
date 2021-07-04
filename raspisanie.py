from bs4 import BeautifulSoup
import requests


# парсинг расписания сохраненного в ворде в формате HTM с фильтром
# отсеиваем остальное ненужное.  Надо с IDE

# файл для парсинга, лежит в томже каталоге что и программа
file_htm = '01.htm'
# данные для формирования таблицы
txtR="<table border='1'>\n    <tbody>\n        <tr>\n\
            <td style='text-align: center;' colspan='2' align='center' width='10%'><span style='font-size: 14pt;'>Дата</span></td>\n\
            <td style='text-align: center;' width='50%'><span style='font-size: 14pt;'>Память святого или события</span></td>\n\
            <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Утро</span></td>\n\
            <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Вечер</span></td>\n\
        </tr>\n"
txtH = "            <td style='text-align: center;'><span style='font-size: 14pt;'>"
txtE = "</td>\n"
# читаем файл и парсим его
with open (file_htm,'r') as f:
    html = BeautifulSoup(f.read(), 'html.parser')
# выделяем только строки с таблицы
pars1 = html.findAll('tr')
for i in range (len(pars1)):
        pars2 = pars1[i].findAll('td')
        txtR+="        <tr>\n"
        ttx=" "
#        print(pars2)
        for j in range (len(pars2)):
            it = pars2[j].findAll('span')
            print(pars2[j])
            for dat in it:
#                it2=it.find({'style='})
#            item['style'].split("color:")
                print(it)
#            pars3 = pars2[j].findAll('span')
#            print(pars3)

#            for o in pars3:
#                ttx=o
#                print(ttx)
#                ttx+="\n"
#            pars3=ttx.replace('\n ',' ')
#            pars3=pars3.replace('  ',' ')
#            txtR+=txtH+pars3+txtE
#        txtR+="        </tr>\n"
#txtR+="    </tbody>\n</table>"
#print(txtR)

#for data in filteredNews:
#    print(data)


#item = soup.select_one('div.flex-embed-content.flex-embed-cover-image')
#item['style'].split("url('")[1][:-3]
