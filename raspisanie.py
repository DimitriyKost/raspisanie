# парсинг расписания сохраненного в ворде в формате HTM с фильтром
# отсеиваем остальное ненужное.  Надо с IDE

from bs4 import BeautifulSoup
import requests

file_htm = '01.htm'

with open (file_htm,'r') as f:
    html = BeautifulSoup(f.read(), 'html.parser')
#filteredNews = []
#allNews = []
#print(html)
pars1 = html.findAll('tr')
txtH="            <td style='text-align: center;'><span style='font-size: 14pt;'>"
#print (txtH)
txtE="</td>\n"
txtR="<table border='1'>\n    <tbody>\n        <tr>\n\
            <td style='text-align: center;' colspan='2' align='center' width='10%'><span style='font-size: 14pt;'>Дата</span></td>\n\
            <td style='text-align: center;' width='50%'><span style='font-size: 14pt;'>Память святого или события</span></td>\n\
            <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Утро</span></td>\n\
            <td style='text-align: center;' width='20%'><span style='font-size: 14pt;'>Вечер</span></td>\n\
        </tr>\n"
for i in range (len(pars1)):
        pars2 = pars1[i].findAll('td')
        txtR+="        <tr>\n"
        for j in range (len(pars2)):
            pars3 = pars2[j].find('span').text
            pars3=pars3.replace('\n ',' ')
            pars3=pars3.replace('  ',' ')
            txtR+=txtH+pars3+txtE
        txtR+="        </tr>\n"
txtR+="    </tbody>\n</table>"
print(txtR)

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
