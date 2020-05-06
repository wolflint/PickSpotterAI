import csv

# append id and file name to csv to speed up manual data labelling
with open('pick_locations.csv', "a", newline='') as location_file:
    fieldnames = ['id', 'img_name', 'pick_x', 'pick_y']
    filewriter = csv.DictWriter(location_file, fieldnames)
    next_index = int(input('Next index: '))
    file_prefix = input('Filename prefix character: ')
    file_suffix = '.jpg'
    num_of_new_images = int(input('How many new images? '))

    current_index = next_index
    while current_index <= (current_index + num_of_new_images):
        file_index_string = '{:0>4}'.format(current_index)
        current_row = {
        'id': str(current_index),
        'img_name': file_prefix + file_index_string + file_suffix,
        'pick_x': '0',
        'pick_y': '0',
        }
        filewriter.writerow(current_row)
        print('Appended: {}'.format(current_row))
        current_index += 1
