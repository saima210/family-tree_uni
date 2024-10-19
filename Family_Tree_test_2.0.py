def main():
    # Ensure the main family tree file exists
    initialize_family_list()

    option_path = input("Please enter 'yes' to create a family: ")

    if option_path.lower() == "yes":
        family_name = input("Please enter your family name: ")
        
        # Add the new family name to the main family tree file
        add_family_name(family_name)

        while True:
            person_name = input("Please enter a name to add to the family (or type 'exit' to see family block): ")
            if person_name.lower() == 'exit':
                break
            person_birth_date = input("Please enter the person's birth date as {dd/mm/yyyy}: ")
            Family_Tree_write(family_name, person_birth_date, person_name)

        print_family_tree(family_name)  

def Family_Tree_write(family_name, person_birth_date, person_name=None):
    file_name = f"{family_name}_family_doc.txt"
    
    with open(file_name, "a") as f:
        if person_name:
            f.write(f"{person_name}, {person_birth_date}\n")
        else:
            f.write(f"{family_name}, {person_birth_date}\n")

def print_family_tree(family_name):
    file_name = f"{family_name}_family_doc.txt"
    
    try:
        with open(file_name, "r") as f:
            contents = f.read()
            print(f"\nContents of {file_name}:")
            print(contents)
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

def initialize_family_list():
    # Create main_family_tree.txt if it doesn't exist
    try:
        with open("main_family_tree.txt", "x") as f:
            pass  # Just create the file
    except FileExistsError:
        pass  # File already exists

def add_family_name(family_name):
    with open("main_family_tree.txt", "a") as f:
        f.write(f"{family_name}\n")

def show_existing_families():
    try:
        with open("main_family_tree.txt", "r") as f:
            print("\nExisting families:")
            print(f.read())
    except FileNotFoundError:
        print("No family names exist yet.")

if __name__ == "__main__":
    show_existing_families()  # Show existing families before starting
    main()
