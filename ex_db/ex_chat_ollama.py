from tkinter import *
from tkinter import scrolledtext
def send_message(event=None):
    message = entry.get()
    if message:
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"\nYou:{message}\n")
        chat_window.config(state=DISABLED)
        entry.delete(0, END)
        chat_window.yview(END)  # 자동 스크롤
        # ollama 에게 요청
        res_stream = ollama.chat(model=model_nm, messages=messages)
        # 응답 내용을 출력

app = Tk()
app.title("Chat UI")
app.geometry("400x500")
# 채팅 창
chat_window = scrolledtext.ScrolledText(app, wrap=WORD, state=DISABLED, height=20, width=50)
chat_window.pack(pady=10, padx=10, expand=True, fill=BOTH)

# 입력프레임
input_frame = Frame(app)
input_frame.pack(pady=10, padx=10, fill=X)
# input
entry = Entry(input_frame)
entry.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
# btn
btn = Button(input_frame, text="Send", command=send_message)
btn.pack(side=RIGHT, padx=5, pady=5)
app.mainloop()

result = tk.Label(app, text=f"{ai_all_response}")
result.pack(pady=10)

res_stream = ollama.chat(model=model_nm, messages=message, stream=True)
ai_all_response = ""
for part in res_stream:
    text = part["message"]["content"]
    print(text, end="", flush=True)
    ai_all_response += text
print()
message.append({"role": "assistant", "content": ai_all_response})  # 컨텍스트 저장

