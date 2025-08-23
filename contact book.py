import os

# Node class for linked list
class ContactNode:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None


class ContactBook:
    def __init__(self):
        self.head = None
        self.filename = "contacts.txt"
        self.load_from_file()

    # Insert contact alphabetically
    def add_contact(self, name, phone, email):
        new_node = ContactNode(name, phone, email)

        # If list is empty or new contact should be first
        if self.head is None or name.lower() < self.head.name.lower():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_node.next = current.next
            current.next = new_node

        print(f"✅ Contact '{name}' added successfully.")
        self.save_to_file()

    # Search contact
    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print(f"🔍 Found: {current.name}, {current.phone}, {current.email}")
                return current
            current = current.next
        print("⚠️ Contact not found.")
        return None

    # Update contact
    def update_contact(self, name, new_phone=None, new_email=None):
        contact = self.search_contact(name)
        if contact:
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            print(f"✏️ Contact '{name}' updated successfully.")
            self.save_to_file()

    # Delete contact
    def delete_contact(self, name):
        if self.head is None:
            print("⚠️ Contact list is empty.")
            return

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            print(f"🗑️ Contact '{name}' deleted.")
            self.save_to_file()
            return

        current = self.head
        while current.next and current.next.name.lower() != name.lower():
            current = current.next

        if current.next:
            current.next = current.next.next
            print(f"🗑️ Contact '{name}' deleted.")
            self.save_to_file()
        else:
            print("⚠️ Contact not found.")

    # Show all contacts
    def show_contacts(self):
        if self.head is None:
            print("📭 No contacts available.")
            return
        print("\n📖 Contact List:")
        current = self.head
        while current:
            print(f"- {current.name} | {current.phone} | {current.email}")
            current = current.next

    # Save to file
    def save_to_file(self):
        with open(self.filename, "w") as f:
            current = self.head
            while current:
                f.write(f"{current.name},{current.phone},{current.email}\n")
                current = current.next

    # Load from file
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                self.add_contact(name, phone, email)


# -------------------- Console Menu --------------------
def main():
    book = ContactBook()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1) Add Contact")
        print("2) Search Contact")
        print("3) Update Contact")
        print("4) Delete Contact")
        print("5) Show All Contacts")
        print("0) Exit")

        choice = input("Choose option: ").strip()

        if choice == "0":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        elif choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            book.add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter name to search: ").strip()
            book.search_contact(name)
        elif choice == "3":
            name = input("Enter name to update: ").strip()
            new_phone = input("Enter new phone (or leave blank): ").strip()
            new_email = input("Enter new email (or leave blank): ").strip()
            book.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            book.delete_contact(name)
        elif choice == "5":
            book.show_contacts()
        else:
            print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    main()
