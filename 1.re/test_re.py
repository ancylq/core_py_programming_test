# coding:utf-8
import re

# ----- 使用finditer()查找每一次出现的位置 -----
s = 'This and that'
print [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)] # [('This', 'that')]
print [g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)] # ['This', 'that']

# ----- sub() subn() -----
print re.sub('[ae]', 'x', 'abcdefg') # xbcdxfg
print re.subn('[ae]', 'x', 'abcdefg') # ('xbcdxfg', 2)
# 很疑惑下面两个，子组换位置就输出的非预计的
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\3/\1/\2', '2/20/2016') # 20/2/2016
print re.sub(r'(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{2}|\d{4})', '\g<year>-\g<month>-\g<day>', '2/20/2016')

inputStr = "hello 123 world 456";
def _add111(matched):
    intStr = matched.group("number"); #123
    intValue = int(intStr);
    addedValue = intValue + 111; #234
    addedValueStr = str(addedValue);
    return addedValueStr;
         
replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr);
print "replacedStr=",replacedStr; #hello 234 world 567

# ----- split() -----
data = ('Mountain Vies, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA')
for datnum in data:
    print re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datnum)
# 输出如下：
# ['Mountain Vies', 'CA 94040']
# ['Sunnyvale', 'CA']
# ['Los Altos', '94023']
# ['Cupertino 95014']
# ['Palo Alto CA']

# ----- 扩展符号 -----
print re.findall(r'(?i)yes', 'yes?Yes,YES')    # (?i) 不区分大小写,['yes', 'Yes', 'YES']
print re.findall(r'(?im)(^th[\w ]+)', '''
This line is the first,
another line,
that line, it's the best''')    # (?im) 不区分大小写并多行匹配，['This line is the first', 'that line']

