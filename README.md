# ロボットシステム学 課題2
 
ROSを用いたプログラムです。
Pythonを使用しています。

# デモ動画
https://www.youtube.com/watch?v=ajRvr5sO400

# 特徴
cout.py : 1秒間に10ずつ大きくなる数字を出力する。  
twice.py : cout.pyの数字を倍にして出力する。
 
# 必要品
 
* Ubuntu
* Raspberry Pi
* LANケーブル
* ルーター
* USB Micro-B

# 使用法
## その①
ubuntuの端末を4つ起動し以下を実行
```bash
端末1$ rosecore
端末2$ chmod +x count.py
端末3$ rosrun myplg count.py
端末4$ rostopic echo /count_up
```
## その②
同様に端末を3つ起動し以下を実行
```bash
端末1$ rosecore
端末2$ chmod +x twice.py
端末3$ rosrun myplg twice.py
```

# 著者
Daigo Takano + Ryuichi Ueda
 
# ライセンス
GNU General Public License v3.0(GPL-3.0)
