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
##①
ubuntuの端末を4つ起動し以下を実行
```bash
端末1$ rosecore
端末2$ chmod +x count.py
端末3$ rosrun myplg count.py
端末4$ rostopic echo /count_up
```
##②

# 注意
```bash
sudo rmmod myled
```
を実行した際に
```bash
insmod: ERROR - could not insert module myled.ko 
```
というエラーが起きる場合があることが確認されています。  その際は、
```bash
make clean
```
を実行後に上記プログラムのmakeからやり直してください

# 著者
Daigo Takano + Ryuichi Ueda
 
# ライセンス
GNU General Public License v3.0(GPL-3.0)
