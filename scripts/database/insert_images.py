# Python script to generate a SQL script to batch insert images into the database
#
# SQL STATEMENT: INSERT INTO tbl_image_data(image_id, language_name, task_type_id, image_filepath)
#                VALUES ('006', 'Korean', '1', 'data/korean/1/006.png')

import os

filename = 'batch_image_insert.sql'
image_directory = 'C:\Users\Administrator\Documents\MCS_Data\Folder125.1-Korean(Seoul)'

for file in os.listdir(image_directory):
    print file

# with open(filename, 'w') as f:
#     for file in os.listdir("/mydir"):
#     if file.endswith(".txt"):
#         print(file)
#
#     for column in range(41):
#         f.write("class Form_Task_Foci_001_0" + str(column) + "(ModelForm):")
#         f.write("""
#     class Meta:
#         model =  Task_Foci_001
#         fields = ('cell_a""" + str(column) + """', 'cell_b""" + str(column) + """', 'cell_c""" + str(column) + """', 'cell_d""" + str(column) + """', 'cell_e""" + str(column) + """',
#                   'cell_f""" + str(column) + """', 'cell_g""" + str(column) + """', 'cell_h""" + str(column) + """', 'cell_i""" + str(column) + """', 'cell_j""" + str(column) + """',)\n""")
#         f.write("    column = " + str(column) + "\n")
#         for row in rows:
#             f.write("    cell_" + str(row) + str(column) + " = forms.CharField(widget=forms.TextInput(), label = \"" + str(row).upper() + "\", required=False)\n")
#         f.write("\n")
