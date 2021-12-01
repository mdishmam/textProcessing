import random

#prefix array
pref_arr1 = ['Best', 'Top Best']
pref_arr2 = ['Top', 'Buying guide for']
pref_arr3 = ['Deals for', 'Buying guide for', 'Best deals for']
pref_arr4 = ['Best', 'Top Best', 'Buying', 'guide for']

#suffix array
suf_arr1 = ['Based on user rating', 'Based on customer ratings', 'Based on Scores in [2021]', 'To buy online', 'for you', 'with exaprt recommendation', 'with rpoducts list', 'available on market', 'with scores']
suf_arr2 = ['Reviews in [2021]', 'Based on user rating', 'Based on customer ratings', 'Based on scores', 'In [2021]', '- To Buy Online', 'Reviews For you', 'With expert recommendation', 'Reviews With products list', '- available on market', 'Reviews With scores']
suf_arr3 = ['Reviews in [2021]', 'Based on user rating', 'Based on customer ratings', 'Based on scores In [2021]', '- To Buy Online', 'Reviews For you', 'With expert recommendation', 'Reviews With products list', '- available on market', 'Reviews With scores']
suf_arr4 = ['Reviews in [2021]', 'Based on user rating', 'Based on customer ratings', 'Based on scores In [2021]', '- To Buy Online', 'Reviews For you', 'With expert recommendation', 'Reviews With products list', '- available on market', 'Reviews With scores']

def titleProcessing(title):
    # both best and review or reviews
    if (title.split()[-1].lower() == 'reviews' or title.split()[-1].lower() == 'review') and title.split()[0].lower() == 'best':
        title = title[len('best '):]
        prefIndex = random.randrange(0,len(pref_arr1))
        suffIndex = random.randrange(0,len(suf_arr1))
        editedTitle = f'{pref_arr1[prefIndex]} {title} {suf_arr1[suffIndex]}'
        return editedTitle.title()

    #logic 1
    elif title.split()[-1].lower() == 'reviews' or title.split()[-1].lower() == 'review':
        prefIndex = random.randrange(0,len(pref_arr1))
        suffIndex = random.randrange(0,len(suf_arr1))
        editedTitle = f'{pref_arr1[prefIndex]} {title} {suf_arr1[suffIndex]}'
        return editedTitle.title()

    #logic 2
    elif title.split()[0].lower() == 'best':
        prefIndex = random.randrange(0,len(pref_arr2))
        suffIndex = random.randrange(0,len(suf_arr2))
        editedTitle = f'{pref_arr2[prefIndex]} {title} {suf_arr2[suffIndex]}'
        return editedTitle.title()

    #logic 3
    elif 'cheap' in title.lower():
        prefIndex = random.randrange(0,len(pref_arr3))
        suffIndex = random.randrange(0,len(suf_arr3))
        editedTitle = f'{pref_arr3[prefIndex]} {title} {suf_arr3[suffIndex]}'
        return editedTitle.title()

    #logic 4
    else:
        prefIndex = random.randrange(0, len(pref_arr4))
        suffIndex = random.randrange(0, len(suf_arr4))
        editedTitle = f'{pref_arr4[prefIndex]} {title} {suf_arr4[suffIndex]}'
        return editedTitle.title()

def textEditing(text):
    pass

if __name__ == '__main__':
    testTitle = 'best laptop for students'
    output = titleProcessing(testTitle)
    print(output)