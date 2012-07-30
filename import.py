from xml.dom import minidom

#file = open('assets.xml', 'r')

filex = minidom.parse('assets.xml')

assets = filex.getElementsByTagName('asset')

a1 = assets[0].attributes
values = a1.values()
name = a1["name"]
image = a1["image"]
arr1 = [name.value, image.value]
print arr1
