import tkinter as tk
from tkinter import messagebox, ttk

from src.generator import generate_password, generate_password_from_master
from format import export_passwords

languages = {
    "Русский": {
        "title": "Генератор паролей",
        "count": "Сколько паролей",
        "length": "Длина пароля",
        "uppercase": "Заглавные буквы",
        "digits": "Цифры",
        "specials": "Спецсимволы",
        "master": "Мастер-пароль (опционально)",
        "format": "Формат экспорта",
        "generate": "Сгенерировать",
        "done": "Пароли сгенерированы и сохранены в файл.",
        "error": "Количество и длина должны быть числами."
    },
    "English": {
        "title": "Password Generator",
        "count": "Number of passwords",
        "length": "Password length",
        "uppercase": "Uppercase letters",
        "digits": "Digits",
        "specials": "Special characters",
        "master": "Master password (optional)",
        "format": "Export format",
        "generate": "Generate",
        "done": "Passwords generated and saved to file.",
        "error": "Count and length must be numbers."
    }
}

current_lang = "Русский"

def get_text(key):
    return languages[current_lang][key]

def switch_language(event=None):
    global current_lang
    current_lang = language_var.get()
    update_ui_text()

def update_ui_text():
    root.title(get_text("title"))
    label_count.config(text=get_text("count"))
    label_length.config(text=get_text("length"))
    check_upper.config(text=get_text("uppercase"))
    check_digits.config(text=get_text("digits"))
    check_special.config(text=get_text("specials"))
    label_master.config(text=get_text("master"))
    label_format.config(text=get_text("format"))
    button_generate.config(text=get_text("generate"))

def generate():
    try:
        count = int(entry_count.get())
        length = int(entry_length.get())
        use_upper = var_upper.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        master_pwd = entry_master.get().strip()

        passwords = []
        for i in range(count):
            if master_pwd:
                pwd = generate_password_from_master(master_pwd, i, length, use_upper, use_digits, use_special)
            else:
                pwd = generate_password(length, use_upper, use_digits, use_special)
            passwords.append(pwd)

        text_output.delete(1.0, tk.END)
        for i, pwd in enumerate(passwords, start=1):
            text_output.insert(tk.END, f"{i}. {pwd}\n")

        export_format = export_format_var.get()
        export_passwords(passwords, export_format)

    except ValueError:
        messagebox.showerror("Ошибка", get_text("error"))

# --- GUI ---
root = tk.Tk()
root.geometry("450x550")
root.resizable(False, False)

# Язык
language_var = tk.StringVar(value=current_lang)
lang_menu = ttk.Combobox(root, textvariable=language_var, values=list(languages.keys()), state="readonly")
lang_menu.pack(pady=5)
lang_menu.bind("<<ComboboxSelected>>", switch_language)

label_count = tk.Label(root)
label_count.pack()
entry_count = tk.Entry(root)
entry_count.pack()
entry_count.insert(0, "5")

label_length = tk.Label(root)
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()
entry_length.insert(0, "16")

var_upper = tk.BooleanVar(value=True)
check_upper = tk.Checkbutton(root, variable=var_upper)
check_upper.pack()

var_digits = tk.BooleanVar(value=True)
check_digits = tk.Checkbutton(root, variable=var_digits)
check_digits.pack()

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(root, variable=var_special)
check_special.pack()

label_master = tk.Label(root)
label_master.pack()
entry_master = tk.Entry(root)
entry_master.pack()

label_format = tk.Label(root)
label_format.pack()
export_format_var = tk.StringVar(value="txt")
export_options = ["txt", "md", "json", "html"]
export_menu = ttk.Combobox(root, textvariable=export_format_var, values=export_options, state="readonly")
export_menu.pack()

button_generate = tk.Button(root, command=generate)
button_generate.pack(pady=10)

text_output = tk.Text(root, height=12, width=50)
text_output.pack()

update_ui_text()
root.mainloop()
