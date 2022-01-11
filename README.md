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
```bash
git clone git@github.com:DaigoUniversity/Robot_System_Subject-assignment1.git
cd Robot_System_Subject-assignment1

//-----以下からプログラム実行-----//
make
sudo insmod myled.ko
sudo chmod 666 /dev/myled0

echo 1 > /dev/myled0 //LED点灯
echo 0 > /dev/myled0 //LED消灯

/-----後処理-----//
sudo rmmod myled
```

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
