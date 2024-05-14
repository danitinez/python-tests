from bs4 import BeautifulSoup

def gather_data(rows):
    data = []
    row1 = rows[0]
    row2 = rows[1]

    # Skip first value in first row
    row1 = row1.find_all("td")[1:]
    values1 = [float(td.get_text().strip()) for td in row1]

    # Get values from second row
    row2 = row2.find_all("td")
    values2 = [float(td.get_text().strip()) for td in row2]

    # Append second value of second row
    data.append(values1[0])

    # Take third through length of values2 of values1 and average with corresponding values of values2
    for i in range(0, len(values2)):
        avg = (values1[i+1] + values2[i]) / 2
        data.append(avg)

    return data

with open("test.html", 'r') as f:   # Replace "path_to_your_file.html" with your file path
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find(id="body_TablaCaudales")
rows = table.find_all("tr")

dates = [str(td.get_text().strip()) for td in rows[1].find_all('td')]

portezuelo = gather_data(rows[2], rows[3])
el_chanar = gather_data(rows[4], rows[5])
picun = gather_data(rows[6], rows[7])
arroyito = gather_data(rows[8], rows[9])
chanar_arroyito = gather_data(rows[10], rows[11])

print('dates:', dates)
print('portezuelo:', portezuelo)
print('el_chanar:', el_chanar)
print('picun:', picun)
print('arroyito:', arroyito)
print('chanar_arroyito:', chanar_arroyito)