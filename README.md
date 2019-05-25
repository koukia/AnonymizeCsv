# AnonymizeCsv

## Overview
CSVファイルの特定の項目をハッシュ化することで匿名化する．

## Environment
- python3系
- 標準ライブラリのみ使用

## HOW to Use
1. csv_anonymizer.pyのパラメータ確認
   1. グローバル変数target_key: ハッシュ化するCSVファイルのヘッダを編集
   2. csv_file：匿名化するファイルの名前
   3. out_file：匿名化後のファイル名
   
2. 以下を実行
   - `python3 csv_anonymizer.py`

3. 匿名化するカラムの編集
   1. 匿名化するカラムのインデックスをグローバル変数INDEX_{hoge}に定義.
   2. 匿名化するインデックスをグローバル変数TARGET_INDEXESに定義.
