colors = ['red ', 'green ', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()