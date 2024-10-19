def main():
    option_path = input("Please enter 'yes' to create a family: ")

    if option_path.lower() == "yes":
        family_name = input("Please enter your family name: ")

        while True:
            person_name = input("Please enter a name to add to the family (or type 'exit' to quit): ")
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

if __name__ == "__main__":
    main()
