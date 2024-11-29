def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Please enter the filename to read: ")

        # Attempt to open the file for reading
        with open(filename, 'r') as file:
            # Read the content from the file
            content = file.read()

        # Modify the content (Example: Convert to uppercase)
        modified_content = content.upper()

        # Ask for the output filename to save the modified content
        output_filename = input("Enter the filename to save the modified content: ")

        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"The modified content has been written to {output_filename}")

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        # Handle the case where the file cannot be opened (permission issues)
        print(f"Error: You do not have permission to read or write to '{filename}'.")
    except Exception as e:
        # Catch any other exceptions and print the error message
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
