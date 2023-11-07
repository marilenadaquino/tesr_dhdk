import xml.etree.ElementTree as ET

def xml_to_txt(input_xml_file, output_txt_file):
    try:
        tree = ET.parse(input_xml_file)
        root = tree.getroot()

        with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            for element in root.iter():
                if element.text:
                    txt_file.write(element.text.strip() + ' ')
    
    except ET.ParseError:
        print("Error: Invalid XML file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

# example of usage
input_xml_file = 'some.xml'
output_txt_file = 'some.txt'
xml_to_txt(input_xml_file, output_txt_file)
