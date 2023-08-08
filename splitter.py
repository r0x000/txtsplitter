def txt_splitter(file_name, chunk_size):
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        lines = text.strip().split('\n')
        
        for i in range(0, len(lines), chunk_size):
            chunk = lines[i:i + chunk_size]
            new_file_name = f"{file_name}_chunk_{i // chunk_size}.txt"
            
            with open(new_file_name, 'w') as new_file:
                new_file.write('\n'.join(chunk))
            
            print(f"{new_file_name} created.")
        
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

file_name = 'filtered'  # Enter the name of the file you want to split here
chunk_size = 20  # Specify how many lines each chunk will have

txt_splitter(file_name, chunk_size)
