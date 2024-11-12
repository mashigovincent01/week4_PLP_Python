def read_and_write_file():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read from: ")

    try:
        # Attempt to open the specified file for reading
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, converting it to uppercase)
        modified_content = content.upper()

        # Specify a new filename to write the modified content
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written to.")

# Run the function
read_and_write_file()
