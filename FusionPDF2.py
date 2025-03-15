import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

# Definimos la clase PDFMergerApp que manejará la lógica de la aplicación
class PDFMergerApp:
    def __init__(self, root):
        # Inicializamos la ventana principal y sus componentes
        self.root = root
        self.root.title("Fusionador de PDF")  # Título de la ventana
        self.pdf_files = []  # Lista para almacenar los archivos PDF seleccionados

        # Etiqueta para mostrar el texto "Archivos PDF seleccionados:"
        self.label = tk.Label(root, text="Archivos PDF seleccionados:")
        self.label.pack()

        # Lista para mostrar los archivos PDF seleccionados
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack()

        # Botón para agregar archivos PDF
        self.add_button = tk.Button(root, text="Agregar PDF", command=self.add_pdf)
        self.add_button.pack()

        # Botón para fusionar los archivos PDF seleccionados
        self.merge_button = tk.Button(root, text="Fusionar PDFs", command=self.merge_pdfs)
        self.merge_button.pack()

    def add_pdf(self):
        # Función para agregar archivos PDF a la lista
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])  # Abre el cuadro de diálogo para seleccionar archivos PDF
        if file_path:  # Si se selecciona un archivo
            self.pdf_files.append(file_path)  # Agrega el archivo a la lista de archivos PDF
            self.listbox.insert(tk.END, file_path)  # Muestra el archivo en la lista de la GUI

    def merge_pdfs(self):
        # Función para fusionar los archivos PDF seleccionados
        if self.pdf_files:  # Verifica que haya archivos en la lista
            merger = PdfMerger()  # Crea un objeto PdfMerger
            for pdf in self.pdf_files:  # Itera a través de la lista de archivos PDF
                merger.append(pdf)  # Añade cada archivo PDF al PdfMerger
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])  # Abre el cuadro de diálogo para guardar el archivo fusionado
            if output_path:  # Si se selecciona un archivo para guardar
                merger.write(output_path)  # Escribe el archivo PDF fusionado en la ruta seleccionada
                merger.close()  # Cierra el objeto PdfMerger
                self.pdf_files = []  # Reinicia la lista de archivos PDF
                self.listbox.delete(0, tk.END)  # Borra los elementos de la lista en la GUI
                messagebox.showinfo("Éxito", "Los archivos PDF se han fusionado correctamente.")  # Muestra un mensaje de éxito

# Punto de entrada principal inicio (de la aplicación)
if __name__ == "__main__":
    root = tk.Tk()  # Crea una instancia de la ventana principal de tkinter
    app = PDFMergerApp(root)  # Crea una instancia de la aplicación PDFMergerApp
    root.mainloop()  # Inicia el bucle principal de eventos de tkinter
