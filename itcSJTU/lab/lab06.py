# 1
def set_descending(a):
    '''
    删除列表中的重复数字，并且降序输出剩下的不重复数字
    '''
    a=list(set(a))
    a.sort()
    return a[::-1]
# print(set_descending([3,2,1,4,2,3,5]))

# 2
def capitalized_sentence(a):
    '''
    a is a string.
    '''
    return a.upper()
# print(capitalized_sentence('hello, world!'))

# 3
def merge(a,b):
    '''
    merge sorted 2 lists to be another one.
    '''
    a.extend(b)
    a.sort()
    return a
# print(merge([1,2,3],[-1,2,4]))

# 4
def count_even_odd(a):
    '''
    count the number of even and odd numbers from a series of numbers
    '''
    return len([i for i in a if i%2==0]),len([i for i in a if i%2!=0])
# print('even: {} odd: {}'.format(*count_even_odd([1,2,3,4,5,6,7,8,9])))

# 5
def is_valid(password):
    '''
    check if a password is valid or not.
    expecting password to a str,return True or False
    '''
    alphabet=[chr(i+ord('A')) for i in range(26)]
    ALPHABET=[chr(i+ord('a')) for i in range(26)]
    mix=['$','#','@']
    for i in range(len(password)):
        if password[i] in alphabet:
            break
    else:
        return False
    for i in range(len(password)):
        if password[i] in ALPHABET:
            break
    else:
        return False
    for i in range(len(password)):
        if password[i] in mix:
            break
    else:
        return False
    return True if 6<=len(password)<=16 else False
# print(is_valid("2Bjd3$dksjfdksd43a"))

# 6
def vowel_or_consonant(a):
    a=a.upper()
    vowels=['A','E','I','O','U']
    return 'vowels' if a in vowels else 'consonant'
# print(vowel_or_consonant('i'))

# 7
def month_day(month):
    month_day={'January':'31','Feburary':'28/29','March':'31','April':'30','May':'31','June':'30','July':'31','August':'31','September':'30','October':'31','November':'30','December':'31'}
    return month_day[month]
# print(month_day('November'))

# 8
def is_integer(a):
    if len(a)==1:
        return True if ord('0')<=ord(a)<=ord('9') else False
    elif a=='':
        return True
    else:
        return is_integer(a[0]) and is_integer(a[1:])
# print(is_integer('835d'))

# 9
def find_season(month, day):
    '''
    Determine the season based on the month and day.
    '''
    if (month == 12 and day >= 21) or (month in [1, 2]) or (month == 3 and day < 21):
        return "Winter"
    elif (month == 3 and day >= 21) or (month in [4, 5]) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (month in [7, 8]) or (month == 9 and day < 21):
        return "Summer"
    elif (month == 9 and day >= 21) or (month in [10, 11]) or (month == 12 and day < 21):
        return "Autumn"
# print(find_season(11, 12))

# 10
def zodiac(year):
    '''
    鼠牛虎兔龙蛇马羊猴鸡狗猪
    '''
    zodiac='猴鸡狗猪鼠牛虎兔龙蛇马羊'
    return zodiac[year%12]
# print(zodiac(2024))

#11
def next_day():
    '''
    get next day of a given date.
    '''
    year=int(input('Input a year: '))
    month=int(input('Inout a month[01-12]: '))
    day=int(input('Input a day[1-31]: '))
    month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if (year%4==0 and year%100!=0) or (year%400==0):
        month_days[2]+=1
    if day!=month_days[month]:
        day+=1
    else:
        day=1
        if month!=12:
            month=month+1
        else:
            month=1
            year+=1
    return 'The next date is: {}-{}-{}.'.format(year,month,day)
# print(next_day())
    
# 12
text='Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. \nNow we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. \nBut, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth. \nAbraham Lincoln\nNovember 19, 1863 '
# print(text)
def remove_item(item,text):
    while item in text:
        pop=text.index(item)
        text=text[:pop]+text[pop+len(item):] 
    return text
text=remove_item(' --',text)
text=remove_item('.',text)
text=remove_item(',',text)
text=text.lower()
word_num=text.count(' ')
letter_num=len(text)-word_num
print(text,word_num,letter_num)
