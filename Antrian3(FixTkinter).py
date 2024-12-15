import tkinter as tk
from tkinter import messagebox

class AntrianApotek:
    def __init__(self):
        self.antrian = []

    def tambah_antrian(self, nama):
        """Menambahkan nama pasien ke dalam antrian."""
        self.antrian.append(nama)

    def panggil_antrian(self):
        """Memanggil pasien pertama dalam antrian."""
        if self.antrian:
            return self.antrian.pop(0)
        else:
            return None

    def tampilkan_antrian(self):
        """Mengembalikan daftar pasien yang sedang menunggu."""
        return self.antrian

    def jumlah_antrian(self):
        """Mengembalikan jumlah pasien dalam antrian."""
        return len(self.antrian)

class ApotekApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Antrian Apotek")

        self.apotek = AntrianApotek()

        # Label Judul
        self.label_judul = tk.Label(root, text="Sistem Antrian Apotek", font=("Arial", 16))
        self.label_judul.pack(pady=10)

        # Frame untuk menambahkan antrian
        self.frame_tambah = tk.Frame(root)
        self.frame_tambah.pack(pady=5)

        self.label_nama = tk.Label(self.frame_tambah, text="Nama Pasien: ")
        self.label_nama.pack(side=tk.LEFT, padx=5)

        self.entry_nama = tk.Entry(self.frame_tambah, width=30)
        self.entry_nama.pack(side=tk.LEFT, padx=5)

        self.button_tambah = tk.Button(self.frame_tambah, text="Tambah Antrian", command=self.tambah_antrian)
        self.button_tambah.pack(side=tk.LEFT, padx=5)

        # Frame untuk memanggil antrian
        self.frame_panggil = tk.Frame(root)
        self.frame_panggil.pack(pady=5)

        self.button_panggil = tk.Button(self.frame_panggil, text="Panggil Antrian", command=self.panggil_antrian)
        self.button_panggil.pack(side=tk.LEFT, padx=5)

        # Daftar antrian
        self.label_antrian = tk.Label(root, text="Daftar Antrian:", font=("Arial", 14))
        self.label_antrian.pack(pady=10)

        self.listbox_antrian = tk.Listbox(root, width=50, height=10)
        self.listbox_antrian.pack(pady=5)

        # Button Keluar
        self.button_keluar = tk.Button(root, text="Keluar", command=root.quit, bg="red", fg="white")
        self.button_keluar.pack(pady=10)

    def tambah_antrian(self):
        nama = self.entry_nama.get()
        if nama:
            self.apotek.tambah_antrian(nama)
            self.entry_nama.delete(0, tk.END)
            self.update_listbox()
            messagebox.showinfo("Informasi", f"{nama} telah ditambahkan ke dalam antrian.")
        else:
            messagebox.showwarning("Peringatan", "Nama pasien tidak boleh kosong!")

    def panggil_antrian(self):
        nama = self.apotek.panggil_antrian()
        if nama:
            self.update_listbox()
            messagebox.showinfo("Informasi", f"Memanggil pasien: {nama}")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada pasien dalam antrian.")

    def update_listbox(self):
        self.listbox_antrian.delete(0, tk.END)
        for i, nama in enumerate(self.apotek.tampilkan_antrian(), start=1):
            self.listbox_antrian.insert(tk.END, f"{i}. {nama}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApotekApp(root)
    root.mainloop()
