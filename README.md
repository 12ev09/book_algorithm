# 概要

講談社『問題解決力を鍛える!アルゴリズムとデータ構造』の演習問題をPythonを使って解いたもの


## 使用環境

macOS Catalina 10.15.7

pypy3.7-7.3.2


## 環境構築方法

pyenvをインストール
```
$ git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```

pyenvにPATHを通す
```
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

pyenvで該当するバージョンをインストール
```
$ pyenv install pypy3.7-7.3.2
```

使用するバージョンを指定(全体で使用したい場合は local -> global)
```
$ pyenv local pypy3.7-7.3.2
```
## 競技用プログラミングのスニペットの設定

↓をpython.jsonにコピペする(⚙マーク→コマンドパレット → Configure User Snipet → python.json)

```
{
    "import atcoder": {
        "prefix": "import atcoder",
        "body": [
            "def chmax(dp,i,j,x):", 
            "   if x> dp[i][j]:",
            "       dp[i][j]=x", 
            "       return True",
            "   return False",
            "def chmin(dp,i,j,x):",
            "   if x<dp[i][j]: ",
            "       dp[i][j]=x",
            "       return True",
            "   return False",
            "",
            "def main():",
            "    n = int(input())",
            "    print()",
            "",
            "if __name__ == '__main__':",
            "    main()",
            "",
        ],
        "description": ""
    },
}
```