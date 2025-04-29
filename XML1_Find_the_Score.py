import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    retur= len(node.attrib)
    for child in node:
        retur +=get_attr_number(child)
    return retur
    # your code goes here


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
