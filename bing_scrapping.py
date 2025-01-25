import os
import tkinter as tk
from tkinter import ttk, messagebox
from bing_image_downloader import downloader

def download_images(query, limit=300):
    downloader.download(
        query, 
        limit=limit, 
        output_dir='Downloads', 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60
    )

def handle_download():
    query = query_entry.get()
    limit = int(limit_entry.get())
    if query and limit:
        try:
            download_images(query, limit)
            messagebox.showinfo("Éxito", f"Se han descargado {limit} imágenes de '{query}' en la carpeta 'Descargas'")
        except Exception as e:
            messagebox.showerror("Error", f"Error al descargar imágenes: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")

root = tk.Tk()
root.title("BING SCRAPPER")
root.geometry("500x300")
root.configure(bg="#2e2e2e")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#4a4a4a", foreground="#ffffff")
style.configure("TLabel", font=("Helvetica", 12), background="#2e2e2e", foreground="#ffffff")
style.configure("TEntry", font=("Helvetica", 12), fieldbackground="#4a4a4a", foreground="#ffffff")

query_label = ttk.Label(root, text="Ingrese el término de búsqueda:")
query_label.pack(pady=5)
query_entry = ttk.Entry(root, width=60)
query_entry.pack(pady=10)
query_entry.insert(0, "")

limit_label = ttk.Label(root, text="Cuantas imagenes deseas descargar?")
limit_label.pack(pady=5)
limit_entry = ttk.Entry(root, width=60)
limit_entry.pack(pady=20)
limit_entry.insert(0, "")

style.configure("TEntry", padding=10, relief="flat", borderwidth=2, bordercolor="#4a4a4a")
style.map("TEntry", fieldbackground=[("active", "#4a4a4a"), ("!active", "#4a4a4a")])

download_button = ttk.Button(root, text="Descargar Imágenes", command=handle_download)
download_button.pack(pady=20)

root.mainloop()
