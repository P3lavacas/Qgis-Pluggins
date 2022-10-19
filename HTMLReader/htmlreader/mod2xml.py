import xml.etree.ElementTree as obj

file = '/home/kenriquez/Documentos/Pruebas/HTMLReader/'+ \
    'htmlreader/HTMLReader_dialog_base.ui'

def updateXml(filename):
    """Esta funcion debe de cambiar el string del XML"""
    tree = obj.ElementTree(file=filename)
    root = tree.getroot()

    wid = root.find("./widget/layout/item/widget/property/url/string")
    wid.text = "www.google.com"

    tree = obj.ElementTree(root)

    with open(filename, "wb") as fileupdate:
        tree.write(fileupdate)

updateXml(file)
