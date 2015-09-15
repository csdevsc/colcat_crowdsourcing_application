with open('output.txt', 'w') as f:
    f.write("[")
    for x in range(41):
        f.write("Form_Task_Foci_001_0" + str(x) + ", ")
    f.write("]")
