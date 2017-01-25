# RFID # 
Radio Frequency Identification

# proxmark3 # 
* 可以flash掉內容, 有點像android
  * devkitARM
* 那底層OS是什麼呢? linux? 
  * https://github.com/Proxmark/proxmark3/wiki/compiling
* https://github.com/Proxmark/proxmark3/wiki/commands

# 需求 #
* 可以複製卡片, 並將原來的卡片資料保留, 可再寫回去
  * 有 vim 或是類似的工具就能
  * 好像本來就放在 電腦裡了 QQ
* 先確認卡片型號
* 了解RFID運作原理

## RFID運作原理 ##
* Q1:RFID有沒有處理器?
  * 看起來是有微處理器

### RFID分類 ###
* 供電形式 : 有源、無源與半有源系統
* 資料傳輸方式 : 主動式、被動式與半主動式
* 標籤的工作頻率
  * 低頻、高頻、超高頻、微波
* 標籤可讀寫性
  * 唯讀、讀寫、一次寫入多次讀出

* 悠遊卡是RFID技術的應用, 感應頻率為13.56MHz, 規格為ISO-14443 Type A
* ISO-14443 Type A
* MIFARE ?
  * https://www.wikiwand.com/zh-tw/MIFARE
