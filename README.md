## MarkdowntoHTMLconverter
# 概要
マークダウン形式のテキストをHTMLに変換するプログラム．

シェルを通して `python3 MarkdowntoHTMLconverter.py markdown inputfile outputfile` というコマンドを実行することで変換する．

`markdown`　は実行するコマンド

`inputfile`　は入力するマークダウン形式のファイル

`outputfile`　は出力するHTML形式のファイル

###例
`python3 MarkdowntoHTMLconverter.py markdown inputfile.md outputfile.html`
## Guessthenumbergame
# 概要
シェルを通して `python3 Guessthenumbergame.py` というコマンドを実行することで開始する．

入力した最小値と最大値の範囲内で乱数を生成し，生成された乱数を正解するまで答え続ける．正解後，答えた回数を表示する．

入力は，最小値，最大値の順番で入力する．


## File_manuplator
# 概要
`python3 File_manuplator.py reverse inputpath outputpath`を実行することで `outputpath` に `inputpath` の内容を逆にした新しいファイルを作成する．

`python3 File_manuplator.py copy inputpath outputpath`を実行することで `inputpath` にあるファイルのコピーを作成し、`outputpath` として保存する．

`python3 File_manuplator.py duplicate-contents inputpath n`を実行することで `inputpath` にあるファイルの内容を読み込み、その内容を複製し、複製された内容を `inputpath` に n 回複製する．

`python3 File_manuplator.py replace-string inputpath word1 word2` を実行することで `inputpath` にあるファイルの内容から文字列 `word1` を検索し、`word1` の全てを `word2` に置き換えます。
