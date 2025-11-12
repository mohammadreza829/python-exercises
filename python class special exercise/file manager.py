# import os
# import shutil
# import tkinter as tk
# from tkinter import filedialog, messagebox

# # Mapping of file types to extensions
# FILE_TYPES = {
#     "Documents": {
#         "Word": ['.docx', '.doc'],
#         "Excel": ['.xlsx', '.xls'],
#         "Text": ['.txt'],
#         "PDF": ['.pdf'],
#         "Presentation": ['.pptx', '.ppt']
#     },
#     "Archives": {
#         "Zip": ['.zip'],
#         "RAR": ['.rar'],
#         "7z": ['.7z']
#     },
#     "Images": {
#         "JPEG": ['.jpg', '.jpeg'],
#         "PNG": ['.png'],
#         "GIF": ['.gif'],
#         "Bitmap": ['.bmp']
#     },
#     "Scripts": {
#         "Python": ['.py'],
#         "JavaScript": ['.js'],
#         "HTML": ['.html'],
#         "CSS": ['.css']
#     },
#     "Audio": {
#         "MP3": ['.mp3'],
#         "WAV": ['.wav'],
#         "AAC": ['.aac']
#     },
#     "Videos": {
#         "MP4": ['.mp4'],
#         "AVI": ['.avi'],
#         "MKV": ['.mkv'],
#         "MOV": ['.mov']
#     },
#     "Others": {}
# }

# class FileCategorizer:
#     def __init__(self, directory):
#         self.directory = directory

#     def categorize(self):
#         if not os.path.isdir(self.directory):
#             raise ValueError("Invalid directory path.")
#         files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]
#         for file in files:
#             ext = os.path.splitext(file)[1].lower()
#             placed = False
#             for category, subtypes in FILE_TYPES.items():
#                 for subfolder, extensions in subtypes.items():
#                     if ext in extensions:
#                         self._move_file(file, category, subfolder)
#                         placed = True
#                         break
#                 if placed:
#                     break
#             if not placed:
#                 self._move_file(file, "Others")

#     def _move_file(self, filename, category, subfolder=""):
#         base_folder = os.path.join(self.directory, category)
#         if subfolder:
#             target_folder = os.path.join(base_folder, subfolder)
#         else:
#             target_folder = base_folder
#         os.makedirs(target_folder, exist_ok=True)
#         src = os.path.join(self.directory, filename)
#         dst = os.path.join(target_folder, filename)
#         shutil.move(src, dst)

# class FileOrganizerGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("File Organizer")
#         self.root.geometry("400x200")
#         self.path = tk.StringVar()

#         tk.Label(root, text="Select Folder to Organize").pack(pady=10)
#         tk.Entry(root, textvariable=self.path, width=40).pack(pady=5)
#         tk.Button(root, text="Browse", command=self.browse_folder).pack()
#         tk.Button(root, text="Organize", command=self.organize_files).pack(pady=20)

#     def browse_folder(self):
#         folder_selected = filedialog.askdirectory()
#         if folder_selected:
#             self.path.set(folder_selected)

#     def organize_files(self):
#         try:
#             categorizer = FileCategorizer(self.path.get())
#             categorizer.categorize()
#             messagebox.showinfo("Success", "Files have been organized!")
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

# def main():
#     root = tk.Tk()
#     app = FileOrganizerGUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

# print(dir(tuple))




