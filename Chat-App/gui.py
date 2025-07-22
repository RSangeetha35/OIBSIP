
import tkinter as tk

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")
        self.root.configure(bg='#1e1e1e')

        self.chat_area = tk.Text(root, state='disabled', width=60, height=20,
                                 bg='#2d2d2d', fg='#d4d4d4', font=('Consolas', 11), insertbackground='white')
        self.chat_area.pack(padx=10, pady=10)

        self.msg_entry = tk.Entry(root, width=50, font=('Consolas', 11),
                                  bg='#3c3c3c', fg='#ffffff', insertbackground='white')
        self.msg_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", font=('Segoe UI', 10, 'bold'),
                                     bg='#0e639c', fg='white', activebackground='#1177bb',
                                     command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

        self.send_message = None  

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        if self.send_message:
            self.send_message(event)