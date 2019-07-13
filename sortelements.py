def sort_data(filename):
    '''sorts each line in file alphabetically and returns a set containing each
    molecule'''
    file = open(filename)
    lines = file.readlines()
    file.close()
    line_list = []
    for line in lines:
        line = line.rstrip().split()
        line.sort()
        sort_line = ''
        for element in line:
            sort_line += element
        line_list.append(sort_line)
        line_set = set(line_list)
    return line_set

def write_new_file(molecule_set):
    '''orders each molecule and writes them into a new file'''
    file = open('database.txt', 'w')
    element_list = sorted(list(molecule_set))
    for element in element_list:
        element += '\n'
        file.write(element)
    file.close()
    print('done')

molecules = sort_data('elements/all.txt')
write_new_file(molecules)