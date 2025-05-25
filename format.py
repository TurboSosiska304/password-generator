import json
from tkinter import filedialog, messagebox

def export_passwords(passwords, format_):
    filetypes = {
        "txt": ("Text files", "*.txt"),
        "md": ("Markdown files", "*.md"),
        "json": ("JSON files", "*.json"),
        "html": ("HTML files", "*.html")
    }

    default_ext = f".{format_}"
    file_path = filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=[filetypes[format_]],
        title="Сохранить файл как..."
    )

    if not file_path:
        return  # пользователь отменил выбор

    try:
        if format_ == "txt":
            with open(file_path, "w", encoding="utf-8") as f:
                for i, pwd in enumerate(passwords, start=1):
                    f.write(f"{i}. {pwd}\n")

        elif format_ == "md":
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("# Exported Passwords\n\n")
                for i, pwd in enumerate(passwords, start=1):
                    f.write(f"- **{i}.** `{pwd}`\n")

        elif format_ == "json":
            data = {str(i): pwd for i, pwd in enumerate(passwords, start=1)}
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        elif format_ == "html":
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("<!DOCTYPE html>\n<html><head><meta charset='utf-8'><title>Passwords</title></head><body>\n")
                f.write("<h1>Exported Passwords</h1><ul>\n")
                for i, pwd in enumerate(passwords, start=1):
                    f.write(f"<li><strong>{i}.</strong> <code>{pwd}</code></li>\n")
                f.write("</ul></body></html>")

        messagebox.showinfo("Успех", f"Пароли экспортированы в файл:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка экспорта: {str(e)}")
