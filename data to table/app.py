table = []
skipLine = True

with open("./dataset.txt", "r") as file:
    
    lines = file.readlines() 
    
    for line in lines:
        
        if "00Z" in line:
            splitText = line.split("00Z")
            date = splitText[1][1:].replace(" ","-")

        if line.startswith("-"):
            skipLine = False
    
        elif line.startswith("Station"):
            skipLine = True
        
        if skipLine == False:

            data = line.strip()
            if data.startswith("hPa"):
                continue
            elif data.startswith("PRES"):
                continue
            # elif line.startswith("-"):
            #     continue

            fileName = f"./{date}.txt"

            table.append(data)

            string = "\n".join(table)
            split_string = string.split("-----")

            for str in split_string:
                print(str)
'''

            with open(fileName, 'w') as output_file:
                for line in string:
                    output_file.write(line)
#'''