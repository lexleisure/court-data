# coding=utf8
'''
Created on 2015-8-23

@author: lex
'''
# {"id":1818535,"iname":"孙荣","caseCode":"(2014)滨法执一字第01070号","age":35,"sexy":"女","cardNum":"3723211980****0025","courtName":"滨城区人民法院","areaName":"山东","partyTypeName":"580","gistId":"(2013)滨商初字第513号","regDate":"2014年11月17日","gistUnit":"山东省滨州市滨城区人民法院","duty":"一、被告山东天合牧业有限公司于本判决生效后十日内支付原告滨州信和担保有限公司垫付款1 133 031.89元，利息41 025.08元，共计1 174 056.97元及利息（利息时间从2013年7月26日起至本判决确定付款之日止起按中国人民银行规定的同期贷款利率的四倍计算）；\n二、被告滨州圣丰工贸有限公司、滨州天一混凝土有限公司、惠民县美圣达新型建材有限公司、季玉波、孙荣、杜承文、李晓霞、贾兴国、林新强、赵延星对上述款项承担连带清偿责任\n案件受理费17 589元，财产保全费5 000元，由原告滨州信和担保有限公司负担5 050元。由被告山东天合牧业有限公司、滨州圣丰工贸有限公司、滨州天一混凝土有限公司、惠民县美圣达新型建材有限公司、季玉波、孙荣、杜承文、李晓霞、贾兴国、林新强、赵延星负担17 539元，","performance":"部分未履行","performedPart":"154361元","unperformPart":"1037234元","disruptTypeName":"其他有履行能力而拒不履行生效法律文书确定义务","publishDate":"2015年08月20日"}
import json
import MyJsonDecoder
import string

def json2Str(jsonStr):
    content = json.loads(
                         '''
                         {"id":1818535,
"iname":"孙荣",
"caseCode":"(2014)滨法执一字第01070号",
"age":35,
"sexy":"女",
"cardNum":"3723211980****0025",
"courtName":"滨城区人民法院",
"areaName":"山东",
"partyTypeName":"580",
"gistId":"(2013)滨商初字第513号",
"regDate":"2014年11月17日",
"gistUnit":"山东省滨州市滨城区人民法院",
"duty":"一、被告山东天合牧业有限公司于本判决生效后十日内支付原告滨州信和担保有限公司垫付款1 133 031.89元，利息41 025.08元，共计1174 056.97元及利息（利息时间从2013年7月26日起至本判决确定付款之日止起按中国人民银行规定的同期贷款利率的四倍计算）；\n二、被告滨州圣丰工贸有限公司、滨州天一混凝土有限公司、惠民县美圣达新型建材有限公司、季玉波、孙荣、杜承文、李晓霞、贾兴国、林新强、赵延星对上述款项承担连带清偿责任\n案件受理费17589元，财产保全费5000元，由原告滨州信和担保有限公司负担5050元。由被告山东天合牧业有限公司、滨州圣丰工贸有限公司、滨州天一混凝土有限公司、惠民县美圣达新型建材有限公司、季玉波、孙荣、杜承文、李晓霞、贾兴国、林新强、赵延星负担17 539元，",
"performance":"部分未履行",
"performedPart":"154361元",
"unperformPart":"1037234元",
"disruptTypeName":"其他有履行能力而拒不履行生效法律文书确定义务",
"publishDate":"2015年08月20日"}
                         '''
                         ,encoding='utf-8')
    print content, content.iname

if __name__ == '__main__':
    #json2Str('')
    
    s=u'''
                         {
"duty":"一、被告山东天合牧业有限公司于本判决生效后十日内支付原告滨州信和担保有限公司垫付款1 133 031.89元，利息41 025.08元，共计1174 056.97元及利息（利息时间从2013年7月26日起至本判决确定付款之日止起按中国人民银行规定的同期贷款利率的四倍计算）；\n"
    }
    '''
    
    #d = '{"name":"李丰","sex":"male","age":35}'
    
    print type(s)
    
    #mpa = string.maketrans(u'\n\r\t',u'   ')
    #print mpa,type(mpa)
    
    s=s.encode('utf8')
    
    s = s.translate(string.maketrans('\n\r\t','   '))
    
    print s,type(s)
   
    content = json.loads(s, encoding='utf8')
    print content,type(content)
    print content.get('duty')
    
    #print data["name"],data["sex"],data["age"],data.get("unknown")
