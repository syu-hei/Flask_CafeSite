# Flask_CafeSite
URL : https://cryptic-refuge-64692.herokuapp.com/  
  
## フロント側
•HTML/CSS  
•jinja2  
•bootstrap  
•font awesome
## サーバー側
•Flask  
•Postgresql  
•Gunicorn  
•Heroku
## 実装機能
### Model
•classによるmodel定義  
•参照されたときの処理  
•データベースへのモデルの反映をスクリプトで簡略化  
### Template
•カフェ専用サイト作成(top, news, menu, contact)  
•新規登録ページ作成  
•ログインページ作成  
•記事投稿ベージ作成  
•記事閲覧ページ作成  
•記事内容詳細ページ作成  
### View
•HTMLをプラウザに渡す  
•ログイン,ログアウト機能のデコレータ作成  
•ログイン認証機能  
•記事投稿, データベースからの記事取得, 記事閲覧,  
記事内容詳細, 記事編集, 記事削除の機能導入  
•ビューを分割(cafe, loging, review, users)  
•flash機能('ログインしました'など、ユーザーにメッセージを表示する)  
### その他
•configファイルで設定を1つにまとめる(databaseURL, シークレットキーなど)
