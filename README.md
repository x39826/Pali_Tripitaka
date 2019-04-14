# Pali_Tripitaka

Pali Buddhist scriptures of 15 countries and its parallel corpus  

 
巴利语大藏经覆盖的语言
--------------------------------------
语言        | 中文名      | 介绍  
---------- | :--------:  | :-------------:
Devanagari | 天城体梵语   | 天城体书写的梵文         
Gujarati   | 古吉拉特语   | 印度官方语言             
Kannada    | 埃纳德语     | 印度官方语言             
Malayalam  | 马拉雅拉姆语 | 印度宪法承认的语言       
Tamil      | 泰米尔语     | 印度宪法承认的语言       
Telugu     | 泰卢固语     | 印度宪法承认的语言       
Bengali    | 孟加拉语     | 孟加拉国和印度的官方语言 
Gurmukhi   | 旁遮普语     | 旁遮普人的语言           
Sinhala    | 僧伽罗语     | 斯里兰卡的主要官方语言   
Khmer      | 高棉语       | 柬埔寨的官方语言         
Myanmar    | 缅甸语       | 缅甸的官方语言           
Thai       | 泰语         | 东亚语系傣泰民族的语言   
Roman      | 罗马字体     | 巴利语罗马拼音音译       
Cyrillic   | 斯拉夫语     | 斯拉夫语族的语言         
Tibetan    | 藏语         | 汉藏语系藏缅语族藏语支   

-------------------------------

## 原始语料与处理后的语料

**sentence level alignment of the Pali scriptures**
```
tar -xzvf Data.tar.gz
```

**original documents of the Pali scriptures**
```
tar -xzvf Spider/all.html.tar.gz
```

**sample parallel corpus for machine translation**
```
python sample.py
```
**sentencepiece models for 15 Pali languages**
```
tar -xzvf model.tar.gz
```

## 语料介绍
我们从巴利语大藏经 Pali Tipiṭaka(http://www.tipitaka.org)上搜集了 15 种语言的藏经翻译。Pali Tipiṭaka 网页上提供原始佛经不同语言版本的段落级别对齐，但并不能直接构建平行语料用于构建机器翻译模型，一是因为文本中的注释各异需要处理掉，二是长段落文字数占总文字数比例超过 2/3，需要将段落分段切割成短句子。具体获取平行语料的过程如下:

1. 编写网络爬虫程序并行爬取 Pali Tipiṭaka 的佛经网页，按章节保存为 utf8 文本文件，并删除文本注释。
2. 用 SentencePiece10无监督文本预处理程序按照语言类别分别处理得到的文 本，得到分词后的文本，将长段落(所有语言中该句子包含 token 数大于 90)和短段落分开。
3. 切割长段落, 若其中有分句符号(除了标点符号以外，各语言有自己特殊 的分句符)，就在此处切割开，同一段落的句子用标记表示以区别与其它段 落。
4. 由于语言的区别，长段落切割后，不同语言句子数目不一致，以及切割点 不一致，需要重新对齐，使用特别设计的多语言句子对齐算法得到对齐后 的长段落。
5. 合并长短段落文本，构建多语言机器翻译平行语料。


