# ロボットシステム学 課題2
 
LEDを光らせるデバイスドライバのプログラムです。
C言語を使用しています。
 
# デモ
### デモ動画
https://www.youtube.com/watch?v=6jj6drCYsUE

### 回路例

<img src="https://user-images.githubusercontent.com/93714969/146319800-2da83175-fd14-4953-8905-f17996abc907.jpg" width="640px">

### 回路図
<img src="https://user-images.githubusercontent.com/93714969/146628601-f4c1fe9a-c298-48c2-b96d-b8fa15b0b801.jpg" width="640px">

# 特徴
 
LEDを点灯または消灯せることができます。
 
# 必要品
 
* Ubuntu
* Raspberry Pi
* LANケーブル
* ルーター
* USB Micro-B
* LED
* 抵抗(200~300Ω)
* ジャンパーワイヤー(オス-メス)

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
