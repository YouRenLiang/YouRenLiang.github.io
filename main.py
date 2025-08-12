import tkinter as tk
from encode import encode
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("BaseN Encoder")

    tk.Label(root, text="Enter string:").grid(row=0, column=0, padx=10, pady=10)
    entry = tk.Entry(root, width=50)
    entry.grid(row=0, column=1, padx=10, pady=10)

    result_var = tk.StringVar()
    tk.Label(root, text="Encoded output:").grid(row=2, column=0, padx=10, pady=10)
    result_entry = tk.Entry(root, textvariable=result_var, width=50, state='readonly')
    result_entry.grid(row=2, column=1, padx=10, pady=10)

    def on_encode():
        try:
            encoded = encode(entry.get())
            result_var.set(encoded)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            result_var.set("")

    btn = tk.Button(root, text="Encode", command=on_encode)
    btn.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()