
#1
log = "January 12 10:00:04 fannyPC succesfull_process[12678]: Sucessful login"
index = log.index('[')
print(log[index+1:index+6]) #print: 1278
#2
log = "January 12 10:00:04 fannyPC succesfull_process[126789]: Sucessful login"
index = log.index('[')
print(log[index+1:index+6]) #print: 1278 (9 is missing)
#3
log = "January 12 10:00:04 [fannyPC] succesfull_process[126789]: Sucessful login"
index = log.index('[')
print(log[index+1:index+6]) #print: fanny
#4
import re
log = "January 12 10:00:04 fannyPC succesfull_process[126789]: Sucessful login"
pattern = r'\[(\d+)\]'
result = re.search(pattern, log)
print(result[1]) #print: 126789
#5
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'P.ng'
        print(re.search(pattern, line))
        #print:<re.Match object; span=(5, 9), match='Ping'>
        #print:<re.Match object; span=(3, 7), match='Pang'>
        #print:<re.Match object; span=(3, 7), match='Pong'>
        #print:<re.Match object; span=(4, 8), match='Pung'>

#6
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'^This P.ng'
        print(re.search(pattern, line))
        #print: <re.Match object; span=(0, 9), match='This Ping'>
        #print: None
        #print: None
        #print: None

#7
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'.ng$'
        print(re.search(pattern, line))
        #print: <re.Match object; span=(6, 9), match='ing'>
        #print: <re.Match object; span=(4, 7), match='ang'>
        #print: <re.Match object; span=(4, 7), match='ong'>
        #print: <re.Match object; span=(4, 7), match='ung'>
#8
print(re.search(r'p.ng', 'Ping', re.IGNORECASE)) #<re.Match object; span=(0, 4), match='Ping'>

#9
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'P[iaou]ng'
        print(re.search(pattern, line))
        #print: <re.Match object; span=(5, 9), match='Ping'>
        #print: <re.Match object; span=(3, 7), match='Pang'>
        #print: <re.Match object; span=(3, 7), match='Pong'>
        #print: <re.Match object; span=(4, 8), match='Pung'>

#10
print(re.search(r'[A-Z]stefanía', 'Estefanía')) #print: <re.Match object; span=(0, 9), match='Estefanía'>

#11
print(re.search(r'[^A-Za-z ]','Mi department number is 9')) #print:<re.Match object; span=(24, 25), match='9'>

#12
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'R.ng|Pin.'
        print(re.search(pattern, line))
        #print: <re.Match object; span=(5, 9), match='Ping'>
        #print: None
        #print: None
        #print: None

#13
print(re.findall(r'Ping|Pung','This sentence contains Ping, Pang, Pung')) #print: ['Ping', 'Pung']

#14
with open('P_ng.txt', 'r') as file:
    for line in file:
        pattern = r'P.*'
        print(re.search(pattern, line))
        #print:<re.Match object; span=(5, 9), match='Ping'>
        #print:<re.Match object; span=(3, 7), match='Pang'>
        #print:<re.Match object; span=(3, 8), match='Pong '>
        #print:<re.Match object; span=(4, 8), match='Pung'>

#15
print(re.findall(r'o+l+', 'Sing me the Holly Dolly Song')) #print: ['oll', 'oll']

#16
print(re.findall(r'H?olly|D?olly', 'Sing me the Holly Dolly olly Song')) #print: ['Holly', 'Dolly', 'olly']

#17
print(re.search(r'\.com', 'www.mypersonalweb.com')) #print: <re.Match object; span=(17, 21), match='.com'>

#18
print(re.search(r'\w*', 'Phone_889998564')) #print: <re.Match object; span=(0, 15), match='Phone_889998564'>

#19
print(re.search(r' \d*', 'Phone 889998564')) #print: <re.Match object; span=(5, 15), match=' 889998564'>

#20
print(re.search(r' \d{3}', 'My bank balance is: 9874463728 €')) #print: <re.Match object; span=(19, 23), match=' 987'>

#21
print(re.search(r'[A-Z]{3}-\[\d{4}]','The purchase ID is OTC-[8872]')) #print:<re.Match object; span=(19, 29), match='OTC-[8872]'>




