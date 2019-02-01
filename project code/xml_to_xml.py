import xml.etree.ElementTree as ET
tree = ET.parse('newSprl2017_test_3.xml')
root = tree.getroot()
# print(root)
for scene in root.iter('SCENE'):
    doc_no = scene.find('DOCNO').text
    print(doc_no.text)
    break