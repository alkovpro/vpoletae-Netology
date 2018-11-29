# without collections.Counter.most_common(10)
import xml.etree.ElementTree as ET

top_10 = []

tree = ET.parse('newsafr.xml', ET.XMLParser(encoding='utf-8'))

root = tree.getroot()
xml_descriptions = root.findall('channel/item/description')

for xml in xml_descriptions:
    over_6 = [i for i in xml.text.split(' ') if len(i) > 6]

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

