インストール
================================================================

実行環境・必要なパッケージ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- python 3.6.8 以上

    - 必要なpythonパッケージ

        - tomli (>= 1.2)
        - numpy (>= 1.14)

- ODAT-SE version 3.0 以降


ダウンロード・インストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. ODAT-SE をインストールする

   - ソースコードからのインストール

     リポジトリから ODAT-SE のソースファイルを取得します。

     .. code-block:: bash

	$ git clone -b update https://github.com/issp-center-dev/ODAT-SE.git

     pip コマンドを実行してインストールします。

     .. code-block:: bash

	$ cd ODAT-SE
	$ python3 -m pip install .

	
     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。
	    
     ``python3 -m pip install .[all]`` を実行するとオプションのパッケージも同時にインストールします。
	  
2. ODAT-SE-template をインストールする

   - ソースコードからのインストール

     ODAT-SE-template のソースファイルは GitHub リポジトリから取得できます。リポジトリをクローンしてソースファイルを取得した後、pip コマンドを実行してインストールします。

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE-template.git
	$ cd ODAT-SE-template
	$ python3 -m pip install .

     ``--user`` オプションを付けるとローカル (``$HOME/.local``) にインストールできます。
	    
     ODAT-SE-template のライブラリがインストールされます。


実行方法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODAT-SE では順問題ソルバと逆問題解析アルゴリズムを組み合わせて解析を行います。
ODAT-SE-template に用意された関数の最適化問題の解析を行うには、ODAT-SE-template ライブラリと ODAT-SE フレームワークを用いてプログラムを作成し、解析を行います。逆問題解析アルゴリズムは import するモジュールで選択します。プログラム中に入力データの生成を組み込むなど、柔軟な使い方ができます。
ライブラリの利用方法については以降の章で説明します。


アンインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODAT-SE-template モジュールおよび ODAT-SE モジュールをアンインストールするには、以下のコマンドを実行します。

.. code-block:: bash

    $ python3 -m pip uninstall ODAT-SE-template ODAT-SE
