# PKMrequirements #
特性
* clear[清楚]
* KISS(Keep it Simple and Stupid)[簡單]
* portable[可攜性]
* version control
  * git
  * git flow
* permission(public, protected, private)
  * protected
	0. 中英文的編碼(unicode to number ?)
	1. 位移和替換(ROT)(caesar and chinese cipher)
	2. qrcode(remove point)
    3. base64(change table) 
  * private
    * AES 256(CBC?)
* 強規則(方便轉移到下個版本)

## permission ##
public 
===

protected
===

private
===

## portable ##
* github
* dropbox
* evernote

## 強規則需求(naming) ##

### git ###
* git branch name
* commit message

### files ###
* name
* directory architecture
* index.txt(對檔案的描述)

### markdown ###
* 語法
* 語言和符號
* two spaces or tab or four spaces

#### temp ####
1. 使用中文, 英文, 底線(正規表示式word)
2. 語法使用 markdown
3. 使用多層次 tag

# git branch #
* master(發行版, 穩定版)
* develop(完成版, 驗證版)
* feature(新, 測試)

# 實務解決想一次完美的作法沒辦法 #
baseline to cycle 
