from snownlp import sentiment, SnowNLP

txt = '在尚未设计出合理的进项税抵扣机制之前，港口企业人工成本和非流动资产无法享受抵扣优惠，导致“营改增”试点中部分港口企业税负不降反升。' \
      '5月24日，财政部、国税总局发出《关于在全国开展交通运输业和部分现代服务业营业税改征增值税试点税收政策的通知》，规定自8 月1 日起，在全' \
      '国范围内开展交通运输业和部分现代服务业“营改增”试点。此次“营改增”试点，港口行业涉及的主要是现代服务业6%的税率。 营改增”试点前，港口企' \
      '业缴纳的流转税费主要包括营业税、增值税以及城建税、教育附加和地方教育附加费等，且以营业税为主。“营改增”试点后港口各项服务的税率变化如下：' \
      '装卸业务由3%改为6%；仓储业务由5%改为6%；理货业务由3%改为11%；运输业务由3%改为11%；向境外单位提供物流辅助服务（仓储除外）由原装卸3%和其他业务5%改为0%。 ' \
      '“营改增”的实施并非如想象中那样一帆风顺，试点的部分港口企业税负不降反升，这似乎与之前对“营改增”所希冀的减税效果背道而驰。几家欢喜几家愁' \
      '港口企业税负增加在之前一些机构和企业的调研中已有所体现。去年，在国家公布深圳市将纳入“营改增”试点后，深圳港口协会便迅速了解上海试点的情况，' \
      '并和深圳港口企业多次开会调研，得出的结论让人失望。以2011年财务数据为基础，“营改增”试点后，深圳东西部港区共增加税负约人民币7467万元，年增幅' \
      '为21%~33%，增幅最高的甚至高达40%。港口企业自身的估算也基本在这一增幅范围内，如天津港和广州港估算，如果不考虑重大固定资产购置进项税抵扣，仅考' \
      '虑日常经营成本中可抵扣的项目，其整体税负将增长 22%以上。 这一评估情况在试点地区的港口企业中已有验证。去年12月1日，浙江开始实施“营改增”。今年' \
      '上半年，嘉兴市港务管理局对嘉兴区域内港口服务企业调查显示，部分企业税负不减反增。嘉兴港区内选取的从事码头装卸、仓储、理货等12家企业，在浙江“营' \
      '改增”实施的半年内，有8家企业税负下降，4家企业税负上升，且税负上升幅度均超过50%（见下表）。'

s = SnowNLP(txt)
before = s.sentiments
print(before)
sentiment.train('neg.txt', 'pos.txt')
sentiment.save('sentiment.marshal')
after = s.sentiments
print(after)