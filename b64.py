import os
import sys
import base64
import filecmp


INPUT_FILE = sys.argv[1]

# check if param is file 
def enc_file(input_file):
    if os.path.isfile(input_file):
        with open(input_file, 'rb') as f:
            file_encoded = base64.b64encode(f.read())
            return file_encoded


file_encoded = enc_file(INPUT_FILE)
file_decoded = base64.b64decode(file_encoded)

if file_encoded == base64.b64encode(file_decoded):
    print('######################\nOk proceed! You can copy\n###########################\n')
    print(file_encoded)
else:
    print('Test failed!')
