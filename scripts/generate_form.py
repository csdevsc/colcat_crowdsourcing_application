# generate_form.py
#
# Generates forms for various task models.

"""
class Form_Task_Foci_001_01(ModelForm):
    class Meta:
        model =  Task_Foci_001
        fields = ('cell_a0', 'cell_b0', 'cell_c0', 'cell_d0', 'cell_e0',
                  'cell_f0', 'cell_g0', 'cell_h0', 'cell_i0', 'cell_j0',)
    cell_a0 = forms.CharField(widget=forms.TextInput(), label="A", required=False)
    cell_b0 = forms.CharField(widget=forms.TextInput(), label="B", required=False)
    cell_c0 = forms.CharField(widget=forms.TextInput(), label="C", required=False)
    cell_d0 = forms.CharField(widget=forms.TextInput(), label="D", required=False)
    cell_e0 = forms.CharField(widget=forms.TextInput(), label="E", required=False)
    cell_f0 = forms.CharField(widget=forms.TextInput(), label="F", required=False)
    cell_g0 = forms.CharField(widget=forms.TextInput(), label="G", required=False)
    cell_h0 = forms.CharField(widget=forms.TextInput(), label="H", required=False)
    cell_i0 = forms.CharField(widget=forms.TextInput(), label="I", required=False)
    cell_j0 = forms.CharField(widget=forms.TextInput(), label="J", required=False)
"""

rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

with open('output.txt', 'w') as f:
    for column in range(41):
        f.write("class Form_Task_Foci_001_0" + str(column) + "(ModelForm):")
        f.write("""
    class Meta:
        model =  Task_Foci_001
        fields = ('cell_a""" + str(column) + """', 'cell_b""" + str(column) + """', 'cell_c""" + str(column) + """', 'cell_d""" + str(column) + """', 'cell_e""" + str(column) + """',
                  'cell_f""" + str(column) + """', 'cell_g""" + str(column) + """', 'cell_h""" + str(column) + """', 'cell_i""" + str(column) + """', 'cell_j""" + str(column) + """',)\n""")
        f.write("    column = " + str(column) + "\n")
        for row in rows:
            f.write("    cell_" + str(row) + str(column) + " = forms.CharField(widget=forms.TextInput(), label = \"" + str(row).upper() + "\", required=False)\n")
        f.write("\n")
