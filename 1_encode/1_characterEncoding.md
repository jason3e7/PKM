# ASCII #
American Standard Code for Information Interchange

character encoding standard

# Unicode #
Unicode is a computing industry standard for the consistent encoding

# UTF-8 #
8-bit Unicode Transformation Format

= selfExperience =
以上三種都是字元編碼法

* ASCII
  * 用 bit 存 
  * 8 bits
  * 主要顯示英文, 符號
* Unicode
  * Unicode 9
    * ISO/IEC 10646:2014 plus Amendments 1 and 2
  * 用數字存 
  * 定義字元to數字(table)  
  * 通常指UCS-2
    * UCS-2 vs UTF-16
	* UTF-16可看成是UCS-2的父集。在沒有輔助平面字元（surrogate code points）前，UTF-16與UCS-2所指的是同一的意思。但當引入輔助平面字元後，就稱為UTF-16了。現在若有軟體聲稱自己支援UCS-2編碼，那其實是暗指它不能支援在UTF-16中超過2位元組的字集。對於小於0x10000的UCS碼，UTF-16編碼就等於UCS碼。
* UTF-8
  * 用 bit 存
  * UTF-8是UNICODE的一種變長度的編碼表達方式
  * ASCII是UTF-8的一個子集。因為一個純ASCII字符串也是一個合法的UTF-8字符串，所以現存的ASCII文本不需要轉換。


# notepad.exe #
* ANSI(英文是ASCII編碼，繁體中文用Big5碼）
* Unicode(UCS-2 little endian)
* Unicode big endian
* UTF-8

= Next =
* GBK
* Big5
* BOM(Byte Order Mark)
* BMP(Basic Multilingual Plane)
