# парсинг расписания сохраненного в ворде в формате HTM с фильтром
# отсеиваем остальное ненужное.  Надо с IDE

from bs4 import BeautifulSoup
import requests

file_htm = '01.htm'

with open (file_htm,'r') as f:
    html = BeautifulSoup(f.read(), 'html.parser')
filteredNews = []
allNews = []
#print(html)
pars1 = html.findAll('tr')

#print (pars1[0])
##for data in pars1:
##    if data.find('td') is not None:
##        filteredNews.append(data.text)
txtH="   <td style='text-align: center;'><span style='font-size: 14pt; color: #ff0000;'>"
print (txtH)
txtE="</td>\n"
txtR=""
for data in pars1:
#    if data.find('span') is not None:
        pars2 = data.findAll('td')

#        print(pars2[1])
        for txt in pars2:
            pars3 = txt.find('span').text
            txtR+=txtH+pars3+txtE
            # price = text.replace(' ', '').replace('₽', '')
            #print(txtH+pars3+txtE)
            tx=filteredNews.append(pars3)
            #print(txtH+tx+txtE)
            #txtR+=txtH+tx+txtE
            #print(tx)

ttx=txtR.replace('\n ',' ')
#надо убрать пробелы и разделить по дням
print(ttx)

#for data in filteredNews:
#    print(data)

#<table border="1">
#<tbody>
#<tr>
#<td style="text-align: center;" colspan="2" align="center" width="10%"><span style="font-size: 14pt;">Дата</span></td>
#<td style="text-align: center;" width="50%"><span style="font-size: 14pt;">Память святого или события</span></td>
#<td style="text-align: center;" width="20%"><span style="font-size: 14pt;">Утро</span></td>
#<td style="text-align: center;" width="20%"><span style="font-size: 14pt;">Вечер</span></td>
#</tr>
#<tr>
#<td style="text-align: center;"><span style="font-size: 14pt; color: #ff0000;">1</span></td>
#<td style="text-align: center;"><span style="font-size: 14pt; color: #ff0000;">Чт</span></td>
#<td style="text-align: center;"><span style="font-size: 14pt;"><span style="color: red;">Свщмч. Виктора Островидова, </span><span style="color: red;">епископа Глазовского </span></span></td>
#<td style="text-align: center;"><span style="font-size: 14pt;"><span style="color: red;">8-00 Литургия<br /></span><span style="color: #006600;">Молебен Свт. Виктору,<br /></span><span style="color: #006600;">еп. Глазовскому </span></span></td>
#<td style="text-align: center;"><span style="font-size: 14pt;"><span style="color: blue;">17-00 Вечерня. <br /></span><span style="color: blue;">Утреня с полиелеем</span></span></td>
#</tr>...
#...
#...</tbody>
#</table>
