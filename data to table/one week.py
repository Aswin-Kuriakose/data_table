data_file_path = './dataset.txt'
output_folder_path = './'

with open(data_file_path, 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    print(lines)
# '''
    # Find all occurrences of '43371'
    indices = []
    for i, line in enumerate(lines):
        if 'Thiruvananthapuram' in line:
            indices.append(i)
            if "00Z" in line:
                    split_text = line.split("00Z")
                    date = split_text[1][1:].replace(" ","-")

            print(date)
    if len(indices) > 0:
        for idx in indices:
            # Find the line containing 'Station' after 4 lines of '43371'
            station_index = None
            for i in range(idx + 5, len(lines)):
                if 'Station' in lines[i]:
                    station_index = i
                    break

            if station_index is not None:
                # Create the output file path
                
                    output_file_path = output_folder_path + f"{date}.txt"

                    with open(output_file_path, 'w') as output_file:
                        # Write the data from idx+5 to station_index (excluding both lines)
                        for line in lines[idx + 5:station_index]:
                            output_file.write(line)

    #             print(f"The data after 4 lines of 'Thiruvananthapuram' has been written to {output_file_path}")
    #         else:
    #             print("'Station' not found after 4 lines of 'Thiruvananthapuram'")
    # else:
    #     print("'Thiruvananthapuram' not found in the data file")
# '''