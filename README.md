# QueryCorrection
self complemented SpellCorrection based pinyin similairity, edit distance ，基于用户词表，拼音相似度与编辑距离的查询纠错。

# 关于查询纠错
![Image text](https://github.com/liuhuanyong/QueryCorrection/blob/master/img/query_error.png)


# 项目介绍
对于搜索中的query纠错功能，纠错过程主要分为以下3个过程:  
1， Query纠错判断。对于常见错误，例如常见的拼写错误，使用事先挖掘好的错误query字典，当query在此字典中时纠错。如果用户输入的query查询无结果或结果较少于一定阈值时，尝试纠错，可以根据不同领域的策略和容忍度，配置最少结果数阈值。  
2，不同策略独立纠错。Query有多种纠错策略，包括拼音纠错和编辑距离纠错，模糊音形近字二次纠错等其他纠错策略等。同音策略是用户输入的错误query和候选纠错query有相同的拼音。编辑距离策略就是错误query和候选query之间编辑距离小于一定阈值，并配合其他条件进行过滤。  
3，候选词结果选择。因为每个策略比较独立，不同策略会给出不同的候选词，因此对于候选词的选取，每个策略有所不同。不同策略之间，不同策略内部需要使用不同的评估方式，来选择最优结果。  




