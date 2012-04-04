
flaskprojectのディレクトリに配置する


まずsettings.pyに自分のキーを入れる
settings.py
	key = "your cunsumar key"
	secret = "your cunsumar secret key"

appの最初に
from flask_twitter.TwitterPlugin import *
を書き

あとは、Twitterの認証の必要がある関数に
@twitter_login
を@app.routeの下に付け足すだけ
これを付ける関数には必ずapi=Noneという引数が必要


コールバックになる関数には
@twitter_callback
を付けること
あと、コールバックの関数は必ず
flask.Responseを返すこと

TODO
 まだ、app.routeでしかテストしてない
 コールバックの制約がおおい
