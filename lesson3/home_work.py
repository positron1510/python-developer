text = open('text.txt', mode='r', encoding='utf-8').read()


"""
1) методами строк очистить текст от знаков препинания;
"""

import re

text = re.sub(r"[^\w\s\-]+", '', text)
text = re.sub(r"[\s]{2,}", ' ', text)
text = re.sub(r"[\r\n]+", ' ', text)

print('Текст без знаков препинания:')
print(text)

"""
2) сформировать list со словами (split);
5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
"""

text_list = text.split()
text_list = list(map(lambda x: x.lower(), text_list))

import pymorphy2

morph = pymorphy2.MorphAnalyzer()
text_list = list(map(lambda w: morph.parse(w)[0].normal_form, text_list))

print()
print('Список лемматизированых слов:')
print(text_list)

"""
3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
"""

unique_words = set(text_list)
text_dict = {}
for word in unique_words:
    text_dict[word] = text_list.count(word)

print()
print('Словарь ключ - слово, значение - сколько раз встречается в списке:')
print(text_dict)

"""
4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
"""

dict_items = list(text_dict.items())
dict_items = list(map(lambda t: list(reversed(list(t))), dict_items))
dict_items.sort(reverse=True)

print()
print('5 наиболее часто встречающихся слов:')
for l in dict_items[:5]:
    print(l[1], ' - ', l[0])

print()
print('Уникальные слова:')
print(unique_words)
print('Количество уникальных слов: ', len(unique_words))
