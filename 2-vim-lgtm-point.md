# もくじ
0. [短距離走](./99-sample-rails.rb)
1. [私とVim](./1-vim-to-me.md)
2. [私的Vimのいいところ](./2-vim-lgtm-point.md)
3. [まとめ](./3-summary.md)

# 私的Vimのいいところ
1. モードの切り替えのおかげで修飾キーが少なくて済む
2. モーションでの移動が直感的で早い
3. テキストオブジェクトが直感的で早い

## モードの切替について
{{{
Vimのモードの概念 = 最初にぶち当たる壁
ざっくり4種類あります。

 --------    ESC    --------     v     --------
|        | ======> |        | ======> |        |
| Insert |         | Normal |         | Visual |
|        | <====== |        | <====== |        |
 --------     i     --------    ESC    --------
                      |  ^
                      |  |
             [: or /] |  | ESC
                      |  |
                      v  |
                 --------------
                | Command line |
                 --------------

- Normalモード
  - 編集する場所まで移動したり、
    コピーandペーストなどを行うためのモード
- Insertモード
  - 入力するためのモード
- Visualモード
  - 範囲指定するためのモード
- Command lineモード
  - 保存、終了、置換などを行うためのモード

Insertモードにずっといるとしんどい！Normalモードに基本的にいるようにする！
}}}

## モードの切り替えのおかげで修飾キーが少なくて済む
{{{

普段コピーandペーストを行う際にC-c、C-pなどで
使っている修飾キーが少なくて済みます。

|       y      |  d   |    p   |    x     |  :s  |  /   |
|--------------|------|--------|----------|------|------|
|コピー(ヤンク)| 削除 |貼り付け|一文字削除| 置換 | 検索 |


キーボード内で
「入力 => コピー => ペースト」
や
「検索 => 置換 => 移動」
などが完結するのが嬉しい。

ex.) [サンプル](./99-sample-rails.rb)

}}}

## モーションでの移動が直感的で早い
{{{
豊富に割り当てられているモーションの移動が便利。

(注) モーション ≒ カーソル移動

### 派手に動く

|   gg/G    |  g{num}   |     C-u    |     C-d    |
|-----------|-----------|------------|------------|
| 一番上/下 | {num}行目 |ページ半分上|ページ半分下|

### 単語単位
|      w/W     |     b/B      |      e/E     |
|--------------|--------------|--------------|
| 次単語の先頭 | 前単語の先頭 | 次単語の末尾 |

### 行内
|  0   |      ^       |   f/F{char}   |       t/T{char}      |
|------|--------------|---------------|----------------------|
| 行頭 | 行頭(非空白) | 左/右の{char} | 左/右の{char}の右/左 |
}}}

## テキストオブジェクトが直感的で早い
{{{

|    yiw     |   diw    |   ciw    |
|------------|----------|----------|
|単語のコピー|単語の削除|単語の変更|


|       yib      |     dib      |      cib     |
|----------------|--------------|--------------|
|ブロックのコピー|ブロックの削除|ブロックの変更|

つまり XXX 単位での編集や移動が行えるのが強い!

}}}
