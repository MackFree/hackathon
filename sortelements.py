def sort_data(filename):
    '''sorts each line in file alphabetically'''
    file = open(filename)
    lines = file.readlines()
    file.close()
    line_list = []
    for line in lines:
        line = line.rstrip()
        line.sort()
        line_list.append(line)
    line_set = set(line_list)
    print(line_set)
    
sort_data('all.txt')
        