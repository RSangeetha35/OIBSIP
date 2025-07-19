import socket
import threading
import tkinter as tk
from gui import ChatGUI

HOST = '127.0.0.1'
PORT = 12350  

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.gui = None

    def start_gui(self):
        root = tk.Tk()
        self.gui = ChatGUI(root)
        self.gui.send_message = self.send_message
        self.connect_to_server()
        root.mainloop()

    def connect_to_server(self):
        try:
            self.client.connect((HOST, PORT))
            msg = self.client.recv(1024).decode()
            if msg == "USERNAME":
                username = self.ask_username()
                self.client.send(username.encode())

            threading.Thread(target=self.receive_messages, daemon=True).start()
            self.gui.display_message("✅ Connected to the chat server!")
        except Exception as e:
            print("❌ Connection failed:", e)

    def ask_username(self):
        popup = tk.Toplevel()
        popup.title("Enter Username")
        popup.geometry("300x100")

        label = tk.Label(popup, text="Enter your username:")
        label.pack(pady=5)

        entry = tk.Entry(popup)
        entry.pack(pady=5)

        username = tk.StringVar()

        def submit():
            username.set(entry.get())
            popup.destroy()

        btn = tk.Button(popup, text="Submit", command=submit)
        btn.pack(pady=5)

        popup.grab_set()
        popup.wait_window()
        return username.get()

    def send_message(self, event=None):
        message = self.gui.msg_entry.get()
        if message:
            try:
                self.client.send(message.encode())
                self.gui.display_message(f"You: {message}")
                self.gui.msg_entry.delete(0, tk.END)
            except:
                self.gui.display_message("❌ Failed to send message.")

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                self.gui.display_message(message)
            except Exception as e:
                print("🔌 Disconnected from server:", e)
                self.client.close()
                break

if __name__ == "__main__":
    app = ChatClient()
    app.start_gui()