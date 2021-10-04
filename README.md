# Webサイトの画像を上から順に抽出するプログラム

calibreでうまくPDF化できない場合に用いる場合がある。

## 環境構築

```bash
pip install -r requirements.txt
```

## 使い方

1. calibre内で`*.htmlz`に変換し、拡張子を`.zip`に変更して解凍する。
2. 内部の`index.html`と`images/`を取り出す。
  この際、`images/`内が連番でページ遷移に対応している場合は、これで作業完了。
  連番画像がその順で製本されていない場合は、Html内の指定順で引き出す必要があるため先の作業に移る。
3. 何らかの方法でWebサーバを立てて、`index.html`を表示する。(`docker run --rm -p 8080:80 -v $PWD:/usr/share/nginx/html nginx`がおすすめ。)
5. `main.py`を実行する。
6. `extracted_images`に連番画像が出力される。
