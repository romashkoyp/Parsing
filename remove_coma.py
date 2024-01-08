# Open the file for reading and writing
with open(r'C:\Users\romas\Documents\Code\Parsing\Sources\suomen-sanomalehtikielen-taajuussanasto-B9996.txt', 'r') as file:
    lines = file.readlines()

# Modify the content to remove the first comma
modified_lines = [line.lstrip(',') for line in lines]

# Open the file again for writing and overwrite it with the modified content
with open(r'C:\Users\romas\Documents\Code\Parsing\Sources\suomen-sanomalehtikielen-taajuussanasto-B9996-2.txt', 'w') as file:
    file.writelines(modified_lines)
