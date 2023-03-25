import re
def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))
en = {1:'AEIOULNSTR', 2:'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10:'QZ'}
ru = {1:'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЕЮ', 10:'ФЩЪ'}
text=input().upper()   
if isCyrillic(text):
    print(sum([k for i in text for k,v in ru.items() if i in v]))
else:
    print(sum([k for i in text for k,v in en.items() if i in v]))
