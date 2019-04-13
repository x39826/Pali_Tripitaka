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
