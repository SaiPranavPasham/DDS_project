from collections import deque
from datetime import datetime

# Message class
class Message:
    def __init__(self, msg_id, text):
        self.id = msg_id
        self.text = text
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"#{self.id} [{self.time}] {self.text}"


class ChatHistory:
    def __init__(self):
        self.next_id = 1
        self.incoming = deque()
        self.sent = []
        self.received = []
        self.undo_stack = []
        self.redo_stack = []

    def send(self, text):
        msg = Message(self.next_id, text)
        self.next_id += 1
        self.sent.append(msg)
        self.undo_stack.append(msg)
        self.redo_stack.clear()
        print(f"Sent: {msg}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        msg = self.undo_stack.pop()
        self.sent.remove(msg)
        self.redo_stack.append(msg)
        print(f"Undo: Removed {msg}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        msg = self.redo_stack.pop()
        self.sent.append(msg)
        self.undo_stack.append(msg)
        print(f"Redo: Restored {msg}")

    def enqueue_incoming(self, text):
        msg = Message(self.next_id, text)
        self.next_id += 1
        self.incoming.append(msg)
        print(f"Incoming queued: {msg}")

    def process_incoming(self):
        if not self.incoming:
            print("No incoming messages.")
            return
        msg = self.incoming.popleft()
        self.received.append(msg)
        print(f"Received: {msg}")

    def show_sent(self):
        print("\n--- Sent Messages ---")
        if not self.sent:
            print("(none)")
        for m in self.sent:
            print(m)

    def show_received(self):
        print("\n--- Received Messages ---")
        if not self.received:
            print("(none)")
        for m in self.received:
            print(m)


# -------- Console-based interaction --------
def main():
    chat = ChatHistory()

    while True:
        print("\n=== Chat Message History Manager ===")
        print("1) Send message")
        print("2) Undo last send")
        print("3) Redo last send")
        print("4) Enqueue incoming message")
        print("5) Process next incoming")
        print("6) Show sent history")
        print("7) Show received history")
        print("0) Exit")

        choice = input("Select option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            text = input("Enter message to SEND: ")
            chat.send(text)
        elif choice == "2":
            chat.undo()
        elif choice == "3":
            chat.redo()
        elif choice == "4":
            text = input("Enter INCOMING message to enqueue: ")
            chat.enqueue_incoming(text)
        elif choice == "5":
            chat.process_incoming()
        elif choice == "6":
            chat.show_sent()
        elif choice == "7":
            chat.show_received()
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
