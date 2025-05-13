def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found.")
    except IOError:
        print("❌ Error: File can't be read or written.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Run the function
read_and_modify_file()
