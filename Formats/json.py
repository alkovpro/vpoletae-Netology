# without collections.Counter.most_common(10)
import json
#from pprint import pprint

top_10 = []
with open('newsafr.json', 'r', encoding = 'UTF8') as newsafr:
    news_afr = json.load(newsafr)
    
    for description in news_afr['rss']['channel']['items']:
        over_6 = [i for i in description['description'].split(' ') if len(i) > 6]

    same_root = set([i[:6] for i in over_6])
    
    frequency_set = set()
    for root in same_root:
        frequency_set.add(([i[:6] for i in over_6].count(root), root.lower()))
    top_10 = sorted(frequency_set, reverse = True)

    for count, root in top_10[:11]:
        for i in over_6:
            if root in i:
                print('{0} - {1} times'.format(f"{root}-({i[6:]})", count))
                break
