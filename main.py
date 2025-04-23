import tkinter as tk
from tkinter import messagebox, ttk

def calculate_metrics():
    try:
        lambda_val = float(entry_lambda.get())
        mu_val = float(entry_mu.get())
        
        if lambda_val <= 0 or mu_val <= 0:
            messagebox.showerror("Ошибка", "Значения должны быть больше 0")
            return
        
        rho = lambda_val / mu_val
        p_refuse = rho / (1 + rho)
        q = 1 - p_refuse
        a = lambda_val * q
        
        result_label.config(
            text=f"P(отказ): {p_refuse:.4f} 🚫\nQ: {q:.4f} 📈\nA: {a:.4f} пок./час 📊"
        )
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

root = tk.Tk()
root.title("СМО: Магазин продуктов")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#F0FFF0")

main_frame = tk.Frame(root, bg="#F0FFF0", padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

title_label = tk.Label(
    main_frame,
    text="🛒 Магазин продуктов: Анализ СМО",
    font=("DejaVu Sans", 14, "bold"),
    bg="#F0FFF0",
    fg="#355E3B"
)
title_label.pack(pady=(0, 15))

input_frame = tk.Frame(main_frame, bg="#F0FFF0")
input_frame.pack(anchor="w")

tk.Label(input_frame, text="λ (пок./час):", font=("DejaVu Sans", 11), bg="#F0FFF0", fg="#355E3B").pack(anchor="w", pady=5)
entry_lambda = ttk.Entry(input_frame, width=15, font=("DejaVu Sans", 11))
entry_lambda.pack(pady=5)

tk.Label(input_frame, text="μ (пок./час):", font=("DejaVu Sans", 11), bg="#F0FFF0", fg="#355E3B").pack(anchor="w", pady=5)
entry_mu = ttk.Entry(input_frame, width=15, font=("DejaVu Sans", 11))
entry_mu.pack(pady=5)

button_frame = tk.Frame(main_frame, bg="#F0FFF0")
button_frame.pack(fill="x")

style = ttk.Style()
style.configure("Custom.TButton", font=("DejaVu Sans", 11), background="#98FB98", foreground="#355E3B")
calculate_button = ttk.Button(
    button_frame,
    text="Рассчитать",
    command=calculate_metrics,
    style="Custom.TButton"
)
calculate_button.pack(anchor="e", pady=15)

result_frame = tk.Frame(main_frame, bg="#E0FFE0", relief="solid", bd=1)
result_frame.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(result_frame, height=150, bg="#E0FFE0", highlightthickness=0)
scrollbar = tk.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#E0FFE0")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

result_label = tk.Label(
    scrollable_frame,
    text="",
    font=("DejaVu Sans", 11),
    bg="#E0FFE0",
    fg="#355E3B",
    justify="left",
    wraplength=280
)
result_label.pack(pady=10, padx=10)

style.configure("Custom.TEntry", padding=5)

root.mainloop()