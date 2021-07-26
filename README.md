# scraping
pythonで実装したスクレイピングのソースコードです。

## tabelogディレクトリ
tabelog.comでスクレイピングを行うためのプロジェクトです。  
エリア、キーワードを指定してスクレイピングを行うことができます。  
csvに出力することも可能です。  
取得項目は以下です。  
「店舗の食べログurl、店舗住所、店名、食べ物のジャンル、電話番号、店舗のホームページ、予約可能かどうか、交通手段、星評価数、予算、お店のPR、ドリンクの種類、喫煙禁煙どちらか」  
## Usage
tabelog/tabelog/spidersディレクトリ内で、以下のコマンドを実行してください。  
scrapy crawl tabelogspider -a area=お好きなエリア -a keyword=お好きなキーワード -o お好きなファイル名.csv  
お好きなエリアには、調べたいエリアを入力してください。調べたいエリアがない場合には、「-a area=お好きなエリア」を除いてください。  
お好きなキーワードには、調べたいキーワードを入力してください。調べたいキーワードがない場合には、「-a keyword=お好きなキーワード」を除いてください。  
お好きなファイル名には、出力したいcsvファイル名を入力してください。スクレイピングの結果を出力できます。csvに書き出す必要がない場合は、「-o お好きなファイル名.csv」を除いてください。  
（例）  
scrapy crawl tabelogspider -a area=京都府 -a keyword=魚  
scrapy crawl tabelogspider -a keyword=ベジタリアン  
scrapy crawl tabelogspider -a area=世田谷区  
scrapy crawl tabelogspider  
scrapy crawl tabelogspider -o tabelog.csv  
scrapy crawl tabelogspider -a area=東京都 -o tabelog.csv  
## Attention
requirements.txtに記述しているchromedriver-binaryはローカルのchromeのバージョンによってインストールするバージョンが異なります。