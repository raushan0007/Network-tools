import subprocess
import tkinter as tk
import datetime

class PingApplication:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Network Ping Application")
        self.create_gui()
        self.root.mainloop()

    def create_gui(self):
        # create input field and buttons
        ip_label = tk.Label(self.root, text="Enter IP address:")
        ip_label.pack()

        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.pack()

        self.start_button = tk.Button(self.root, text="Start", command=self.start_ping)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", state=tk.DISABLED, command=self.stop_ping)
        self.stop_button.pack()

        # create output text area
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

        self.output_text.tag_config("green", foreground="green")
        self.output_text.tag_config("red", foreground="red")

    def start_ping(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.ping()

    def stop_ping(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.root.after_cancel(self.after_id)

    def ping(self):
        ip = self.ip_entry.get()

        response = subprocess.Popen(["ping", "-n", "1", ip], stdout=subprocess.PIPE).stdout.read().decode('utf-8')

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "TTL=" in response:
            self.output_text.insert(tk.END, f"{current_time} - {ip} is up\n", "green")
        else:
            self.output_text.insert(tk.END, f"{current_time} - {ip} is down\n", "red")

        self.after_id = self.root.after(1000, self.ping)

if __name__ == "__main__":
    PingApplication()
