import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import openai

app_size_x = 500
app_size_y = 500

def create_chat_string(msg_history):
    display_str = ""
    for ii in range(len(msg_history)-2, len(msg_history)):
        display_str += msg_history[ii]["role"] + " : " + msg_history[ii]["content"] + "\n"
    return display_str

def gpt_response(client, msg_history):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msg_history)
    return completion.choices[0].message.content

class App():
    def __init__(self, gpt_key):
        self.chat_history = []
        self.client = openai.OpenAI(api_key=gpt_key)
        self.app_window = tk.Tk()
        self.app_window.title("ChatGpt")
        self.app_window.geometry(str(app_size_x) + 'x' + str(app_size_y))
        self.main_frame = tk.Frame(self.app_window)
        self.main_frame.pack()
        self.chat_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD,
                                              width=60, height=20,
                                              font=("Times New Roman", 12))
        self.chat_area.configure(state="disabled")
        self.chat_area.pack()
        self.chat_input = tk.Text(self.main_frame, height=5, width=60)
        self.chat_input.bind("<Return>", lambda x:self.send_message())
        self.chat_input.pack()
        self.chat_input.focus_set()
        # self.show_script = tk.Button(self.app_window, text='Refresh', width=10, height=2, bg='lightblue', command=lambda:self.send_message())
        # self.show_script.pack()
        self.chat_input.insert(tk.END, "Czesc Czacie")
        self.app_window.mainloop()

    def send_message(self):
        cur_msg = self.chat_input.get(1.0, "end-1c")
        self.chat_input.delete(1.0, "end-1c")
        if cur_msg != '':
            self.chat_history.append({"role": "user", "content": cur_msg})
            bot_res=gpt_response(self.client, self.chat_history)
            self.chat_history.append({"role": "assistant", "content": bot_res})
            conv_str = create_chat_string(self.chat_history)
            self.chat_area.configure(state="normal")
            self.chat_area.insert("end", conv_str)
            self.chat_area.configure(state="disabled")
        return "break"

def main():
    load_dotenv()
    gpt_env_key = os.getenv("GPT_KEY")
    tk_app = App(gpt_key)

if __name__ == "__main__":
    main()

