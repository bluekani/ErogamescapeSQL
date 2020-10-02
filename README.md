# ErogamescapeSQL

## なにこれ
えろすけのSQLを実行して結果をCSV形式で保存します

## 導入
Python 3系で動作します  
Beautiful Soupが必要です
> pip install beautifulsoup4

## 使用方法
実行したいsqlファイルを指定して実行すると，同じ場所にファイル名_result.csvが生成されます
> python erosukeSQL.py example/kyouen.sql

こんな使い方もできる  

```
from erosukeSQL import erosukeSQL

sql_path = "example/kyouen.sql"
csv_path = erosukeSQL(sql_path) #実行
```

## sqlファイル
UTF-8N(BOM無し)で保存したものを使ってね

## 注意
本プログラムを使用してもしなくとも，サーバーに過剰なアクセスを行い負荷を掛ける行為は絶対におやめ下さい．

## お問い合わせ先
<https://www.brighter-than-dawning.blue/about/>