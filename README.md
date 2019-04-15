# Pali_Tripitaka

Pali Buddhist scriptures of 15 countries and its parallel corpus  

## 巴利三藏平行语料情况简介
目前网上存在的巴利三藏平行语料比较少，覆盖的语言种类基本上是印度 和东南亚语言，完整的其它国家语言如汉，英等版本的巴利三藏目前还没有，多 数语言中只有零散章节的翻译，可能由于历史原因，翻译依据的原始版本有差异，有些版本之间章节内容不一致，如北传汉文大藏经内容和南传巴利文大藏经许多篇章在形式上是不对齐的。比较可靠的平行语料主要有这些:
1. 庄春江居士工作站http://agama.buddhason.org/index.htm , 这里有对应的南北传四部阿含经经典以及现代汉语翻译
2. Sutta Central https://suttacentral.net/ ，这是一个自发组织的巴利文三藏 翻译，汇集了许多语言版本的翻译。
3. 上座部佛教巴利藏经 http://dhamma.sutta.org/index2.htm 提供了英文译 本巴利三藏和汉语译本巴利三藏。
4. 阿含学苑 http://www.agamarama.com/cityzen/jiangtan/AHAN/ahan.htm 提供了汉译南传三藏和汉译北传三藏。
5. Pali Tipiṭaka http://www.tipitaka.org 包含第六次结集版巴利三藏(含注、 疏、藏外、校勘记、斯缅泰及 PTS 页码、多国字体显示)。

 
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

## 语料处理介绍
我们从巴利语大藏经 Pali Tipitaka ([http://www.tipitaka.org](http://www.tipitaka.org))上搜集了 15 种语言的藏经翻译。Pali Tipitaka 网页上提供原始佛经不同语言版本的段落级别对齐，但并不能直接构建平行语料用于构建机器翻译模型，一是因为文本中的注释各异需要处理掉，二是长段落文字数占总文字数比例超过 2/3，需要将段落分段切割成短句子。具体获取平行语料的过程如下:

1. 编写网络爬虫程序并行爬取 Pali Tipitaka 的佛经网页，按章节保存为utf8 文本文件，并删除文本注释。
2. 用 [SentencePiece](https://github.com/google/sentencepiece)无监督文本预处理程序按照语言类别分别处理得到的文本，得到分词后的文本，将长段落(所有语言中该句子包含token数大于 90)和短段落分开。
3. 切割长段落, 若其中有分句符号(除了标点符号以外，各语言有自己特殊的分句符)，就在此处切割开，同一段落的句子用标记表示以区别与其它段落。
4. 由于语言的区别，长段落切割后，不同语言句子数目不一致，以及切割点不一致，需要重新对齐，使用特别设计的多语言句子对齐算法得到对齐后的长段落。
5. 合并长短段落文本，构建多语言机器翻译平行语料。




