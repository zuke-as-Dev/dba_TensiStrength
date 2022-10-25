from dataclasses import dataclass
import nltk
from sentistrength import PySentiStr
nltk.download('wordnet')
nltk.download('omw-1.4')
from sentistrength import PySentiStr
from nltk.corpus import wordnet


senti = PySentiStr()
senti.setSentiStrengthPath('E:\college data\Final Year Project\Code\Final code\TensiStrength\TensiStrengthMain.jar')
senti.setSentiStrengthLanguageFolderPath('E:\college data\Final Year Project\Code\Final code\TensiStrength\TensiStrength_Data')

def download_nltk_dependencies_if_needed():
    try:
        nltk.word_tokenize('foobar')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.pos_tag(nltk.word_tokenize('foobar'))
    except LookupError:
        nltk.download('averaged_perceptron_tagger')

def get_some_word_synonyms(word):
    word = word.lower()
    synonyms = []
    synsets = wordnet.synsets(word)
    if (len(synsets) == 0):
        return []
    synset = synsets[0]
    lemma_names = synset.lemma_names()
    for lemma_name in lemma_names:
        lemma_name = lemma_name.lower().replace('_', ' ')
        if (lemma_name != word and lemma_name not in synonyms):
            synonyms.append(lemma_name)
    return synonyms

def get_all_word_synonyms(word):
    word = word.lower()
    synonyms = []
    synsets = wordnet.synsets(word)
    if (len(synsets) == 0):
        return []
    for synset in synsets:
        lemma_names = synset.lemma_names()
        for lemma_name in lemma_names:
            lemma_name = lemma_name.lower().replace('_', ' ')
            if (lemma_name != word and lemma_name not in synonyms):
                synonyms.append(lemma_name)
    return synonyms

def sort(txt):
        DeleteWords = ["for", "and", "nor", "but", "or", "yet", "so","a","an","the","The","A","i","me","he","she","it","they","am","were","was"]
        st = txt
        x=st.split()
        f_list = []
        for i in x:
            if i not in f_list:
                f_list.append(i)
        NewList = [word for word in f_list if word not in DeleteWords]
        # s=('\n'.join(dict.fromkeys(NewList)))
        return NewList


def rating(s_txt:list):    
    new_word =[]
    for i in s_txt:
        new_word.append(i)
    # c = len(new_word)
    # loader = ProgressLoader(total=c, character='+', colour='yellow')
    output =[]
    count = 0
    for word in new_word:
        # words = words.strip()
        results = senti.getSentiment(word, score='dual')
        # results.append(senti.getSentiment(word, score='dual'))
        output.append( word +" "+ str(results))
        count+=1
        # loader.progress(count)
        # for word in new_word:
        #     for result in results:
        #         output.append( word +" "+ str(result))
    return output

def neutral(r_txt):
    f_read= r_txt
    c = len(f_read)
    n_txt = []
    count=0
    for x in f_read:
        x=x.strip()
        count+=1
        a=x.index('(')
        b=x.index(')')
        if x[a+1:b] == "1, -1":
            n_txt.append(x)
    return n_txt

def data_creator(n_txt: list):
    words=[]
    words_list=n_txt
    for word in words_list:
        word=str(word.replace("[(1, -1)]",""))
        word=str(word.replace("'",''))
        word=str(word.replace("[",''))
        word=str(word.replace("]",''))
        words.append(word.lstrip().rstrip())
    download_nltk_dependencies_if_needed()
    cont = 0
    final_str=""
    for word in words:
        count=0
        cont += 1
        synonyms = get_all_word_synonyms(word)
        string1= str(word)
        result=[(1, -1)]
        for synonym in synonyms:
            synonym = synonym.strip()
            result1=senti.getSentiment(synonym, score='dual')
            count+=1
            if count == 3:
                break
            string1=string1+" "+str(result1)
        final_str=final_str+string1+'\n'
    final_str=final_str.replace('-1','')
    final_str=final_str.replace('1','')
    final_str=final_str.replace('[','')
    final_str=final_str.replace(']','')
    final_str=final_str.replace('(','')
    final_str=final_str.replace(')','')
    final_str=final_str.replace(',','')
    final_list=final_str.split('\n')
    return final_list

def data_base(f_list: list):
    final_list = f_list
    temp = []
    data_base= []
    all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for word in final_list:
        f_str=''
        word=word.rstrip()
        total_digits=0
        for s in word:
            if s in all_digits and word[0:1] not in all_digits:
                total_digits += 1
        if total_digits==2:
            f_str = f_str + str(word)+'\n'  
        elif total_digits==1:
            f_str = f_str + str(word) + ' ' + word[-2:]+'\n' 
        elif total_digits==0:
            pass
        if f_str not in temp:
            temp.append(f_str)
    for i in temp:
        if i not in data_base:
            data_base.append(i)
    return data_base

def new_word(data:list):
    final_list=data
    words=[]
    f_str=''
    all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_digits_neg = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0', '-1',   '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']
    for word in final_list:
        word=word.rstrip()
        total_digits=0
        for s in word:
            if s in all_digits and word[0:1] not in all_digits:
                total_digits += 1
        if total_digits==2:
            f_str = f_str + str(word)+'\n'
        elif total_digits==1:
            f_str = f_str + str(word) + ' ' + word[-2:]+'\n' 
        elif total_digits==0:
            pass
    dataword = f_str.split('\n')
    data_word = ''
    for word in dataword:
        word_list = word.split(' ')
        sub = str(word_list[0])
        data_word = data_word + sub +'\n'
    words=(data_word.split())
    return words

def psy_word(data:list):
    final_list= data
    psy= []
    psy_study=''
    all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_digits_neg = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0', '-1',   '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9']
    for word in final_list:
        word=word.rstrip()
        total_digits=0
        for s in word:
            if s in all_digits and word[0:1] not in all_digits:
                total_digits += 1
        if total_digits==0:
            psy_study=psy_study+str(word)+'\n'
    psy=(psy_study.split())
    return psy

def data_cleaner(data_list: list):
    rm_data = ['','\n']
    NewList = [word for word in data_list if word not in rm_data]
    return NewList

def super_function(txt):
    neutral_data = neutral(rating(sort(txt)))
    clean_data =data_cleaner(data_creator(neutral_data))
    final_data = data_cleaner(data_base(clean_data))
    return (final_data)

def word(txt):
    neutral_data = neutral(rating(sort(txt)))
    words = new_word(data_cleaner(data_creator(neutral_data)))
    return words

def psy_f(txt):
    neutral_data = neutral(rating(sort(txt)))
    psy_data = psy_word(data_cleaner(data_creator(neutral_data)))
    return psy_data