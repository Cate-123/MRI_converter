import os
import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid
from datetime import datetime
from tkinter import Tk, Label, Button, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD

# ========================
# Function to convert enhanced multiframe DICOM to single-frame with proper metadata
# ========================
def convert_enhanced_to_single_frame_fixed(input_paths, output_root):
    for file_path in input_paths:
        try:
            ds = pydicom.dcmread(file_path)

            if not hasattr(ds, 'NumberOfFrames') or ds.NumberOfFrames <= 1:
                continue

            patient_name = getattr(ds.PatientName, 'family_name', 'UnknownPatient')
            series_desc = getattr(ds, 'SeriesDescription', 'UnknownSeries')[:30].replace(' ', '_')
            series_uid = getattr(ds, 'SeriesInstanceUID', generate_uid())

            folder_name = f"{patient_name}_{series_desc}_{series_uid}"
            series_output_path = os.path.join(output_root, folder_name)
            os.makedirs(series_output_path, exist_ok=True)

            num_frames = ds.NumberOfFrames
            rows = ds.Rows
            cols = ds.Columns
            spp = ds.SamplesPerPixel
            bpp = ds.BitsAllocated // 8
            frame_size = rows * cols * spp * bpp

            for i in range(num_frames):
                new_ds = FileDataset(None, {}, file_meta=ds.file_meta, preamble=b"\0" * 128)
                for elem in ds:
                    if elem.tag.group == 0x7FE0:
                        continue
                    if elem.tag not in new_ds:
                        new_ds.add(elem)

                new_ds.SOPInstanceUID = generate_uid()
                new_ds.file_meta.MediaStorageSOPInstanceUID = new_ds.SOPInstanceUID
                new_ds.SeriesInstanceUID = series_uid
                new_ds.InstanceNumber = i + 1
                new_ds.NumberOfFrames = 1

                start = i * frame_size
                end = (i + 1) * frame_size
                new_ds.PixelData = ds.PixelData[start:end]

                filename = os.path.join(series_output_path, f"IMG_{i+1:04d}.dcm")
                new_ds.save_as(filename)

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# ========================
# GUI to handle drag-and-drop and run conversion
# ========================
def launch_gui():
    root = TkinterDnD.Tk()
    root.title("Nexstim MRI Converter")
    root.geometry("500x300")

    Label(root, text="Drag and drop enhanced MRI DICOM files here:", pady=20).pack()

    dropped_files = []

    def drop(event):
        dropped = root.tk.splitlist(event.data)
        dropped_files.clear()
        dropped_files.extend(dropped)
        messagebox.showinfo("Files Received", f"Received {len(dropped_files)} file(s).")

    drop_area = Label(root, text="Drop files here", relief="ridge", height=5)
    drop_area.pack(pady=10, padx=20, fill="x")
    drop_area.drop_target_register(DND_FILES)
    drop_area.dnd_bind('<<Drop>>', drop)

    def start_conversion():
        if not dropped_files:
            messagebox.showerror("No Files", "Please drop some files first.")
            return

        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        output_root = os.path.join(desktop, "Standard MRIs")
        os.makedirs(output_root, exist_ok=True)

        convert_enhanced_to_single_frame_fixed(dropped_files, output_root)
        messagebox.showinfo("Done", f"Conversion complete. Files saved to: {output_root}")

    Button(root, text="Convert to Standard MRIs", command=start_conversion).pack(pady=30)

    root.mainloop()

# ========================
# Run the GUI if script is executed directly
# ========================
if __name__ == "__main__":
    launch_gui()
