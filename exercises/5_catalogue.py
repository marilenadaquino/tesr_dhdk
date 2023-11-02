import lxml.etree as ET

# Read the content of a XML file
dom = ET.parse('5_catalogue.xml')

# Read the XSL file
xslt = ET.parse('5_catalogue.xsl')

# Build a XSL transformer
# create an instance of the class XSLT
transform = ET.XSLT(xslt)

# Perform the transformation
# the result is an instance of the class ElementTree
newdom = transform(dom)

# transform the ElementTree instance in a string and print it 
print(ET.tostring(newdom, pretty_print=True))

# write the string in a html document
with open("5_catalogue_py.html", "wb") as f:
 f.write(ET.tostring(newdom, pretty_print=True))
