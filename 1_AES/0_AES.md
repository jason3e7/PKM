# online tool  #
* https://blog.zhengxianjun.com/online-tool/crypto/aes/
  * 完整度高
* http://aesencryption.net/ 
  * AES_ECB
* https://www.ez2o.com/App/Coder/AES
  * AES_CBC_256
* https://www.tools4noobs.com/online_tools/encrypt/
  * rijndael(AES) iv:0000000000000000

# question #
AES mode
* CBC 
* ECB 
* CTR 
* OCB 
* CFB

[Block cipher mode of operation](https://www.wikiwand.com/en/Block_cipher_mode_of_operation)

## IV的功用是什麼 ? 每次都要用嗎 ? ##

## 常用的是哪個 ? ##
### 可以參考SSL/TLS, 那實際上運作呢? ###

SSL/TLS 使用 AES-CBC-128 的時候, IV的變化是什麼?

有使用AES_CBC_256

擴大經過身分驗證的加密密碼，主要用於GCM和CCM模式的AES加密的支援

### 可以參考Ransomware ###
RSA 2048 and AES 128

https://github.com/aaaddress1/my-Little-Ransomware

馬聖豪 的 cuteRansomware

http://bobao.360.cn/news/detail/3311.html

https://resources.netskope.com/h/i/271578954-cuteransomware-uses-google-docs-to-fly-under-radar

### 壓縮軟體 ###
RAR 2.0使用AES-128-cbc，（rar5.0以後為AES-256CBC)

zip zipCrypto
加密性

Compression level and Compression method ?
支援性 和最大壓縮率

https://www.peterdavehello.org/2014/06/zip-compress-algorithm-choice/

# padding #
PKCS5
8 bits

PKCS7
n bits
