#えろすけにSQLをブチ込んでCSVを出力するプログラム

import sys
import csv
import requests
from bs4 import BeautifulSoup

url = 'https://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/sql_for_erogamer_form.php'

header = {
        'Accept': 'text/html,application/xhtml+xm…ml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language': 'ja,en-US;q=0.7,en;q=0.3',
        'Origin': 'https://erogamescape.dyndns.org',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'https://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/sql_for_erogamer_form.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
        }


def erosukeSQL(sql_pass):
    try:
        with open(sql_pass, encoding="utf-8") as sql_file:
            sql_statement = sql_file.read()
    except:
        print('パスが間違ってるかUTF-8N(BOM無し)でエンコードされてないため，SQLファイルが読み込めません')
        sys.exit()        

    response = requests.post(url, data={'sql': sql_statement}, params=header)
    print("Status:" + str(response.status_code)) #HTTPのステータスコード取得

    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup)
    query_result = soup.find('div', id="query_result")

    query_result_header = query_result.find('div', id="query_result_header").text
    print(query_result_header)

    if("エラー" in query_result_header):
        query_result_main = query_result.find('div', id="query_result_main").text
        print(query_result_main)
    else:
        table = query_result.find("table")
        #print(table)

        # CSVで保存
        csv_pass = sql_pass.replace('.sql', '_result.csv')
        with open(csv_pass, "w", newline="", encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            rows = table.find_all("tr")
            for row in rows:
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text())
                writer.writerow(csvRow)

        with open(csv_pass, encoding="utf-8") as csv_file:
            print(csv_file.read())


if __name__ == '__main__':
    args = sys.argv
    try:
        sql_pass = args[1]
    except:
        print('SQLファイルを指定してください コマンド例> python erosukeSQL.py hoge.sql')
        sys.exit()
    else:
        if(".sql" not in sql_pass):
            print('SQLファイルを指定してください コマンド例> python erosukeSQL.py hoge.sql')
            sys.exit()

    erosukeSQL(sql_pass)
