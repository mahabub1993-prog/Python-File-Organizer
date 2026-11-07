
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

from core.organizer import (
    preview_files,
    organize_files,
    get_summary,
    export_report
)


APP_TITLE = "FileOrganizer - Professional Edition"


class FileOrganizerApp:

    def __init__(self, root):

        self.root = root

        self.root.title(APP_TITLE)
        self.root.geometry("1050x650")
        self.root.minsize(800, 500)

        self.selected_folder = None
        self.current_results = []

        self.create_widgets()

    # =====================================
    # 1. CREATE GUI
    # =====================================

    def create_widgets(self):

        main = ttk.Frame(self.root, padding=15)
        main.pack(fill="both", expand=True)

        # Application title

        ttk.Label(
            main,
            text="FileOrganizer",
            font=("Segoe UI", 22, "bold")
        ).pack(anchor="w")

        ttk.Label(
            main,
            text="Smart Python File Organization Automation"
        ).pack(anchor="w", pady=(2, 15))

        # Folder selection

        folder_frame = ttk.LabelFrame(
            main,
            text="Select Folder",
            padding=10
        )

        folder_frame.pack(fill="x", pady=(0, 12))

        self.folder_var = tk.StringVar(
            value="No folder selected"
        )

        ttk.Entry(
            folder_frame,
            textvariable=self.folder_var,
            state="readonly"
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        ttk.Button(
            folder_frame,
            text="Browse Folder",
            command=self.browse_folder
        ).pack(side="right")

        # Summary dashboard

        summary_frame = ttk.LabelFrame(
            main,
            text="Organization Summary",
            padding=10
        )

        summary_frame.pack(fill="x", pady=(0, 12))

        self.summary_var = tk.StringVar(
            value="Total: 0 | Moved: 0 | Already Organized: 0 | Errors: 0"
        )

        ttk.Label(
            summary_frame,
            textvariable=self.summary_var,
            font=("Segoe UI", 10, "bold")
        ).pack(anchor="w")

        # File details table

        table_frame = ttk.LabelFrame(
            main,
            text="File Details",
            padding=8
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "filename",
            "category",
            "source",
            "destination",
            "status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading("filename", text="File Name")
        self.tree.heading("category", text="Category")
        self.tree.heading("source", text="Source")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("status", text="Status")

        self.tree.column("filename", width=160)
        self.tree.column("category", width=120)
        self.tree.column("source", width=210)
        self.tree.column("destination", width=210)
        self.tree.column("status", width=140)

        # Vertical scrollbar

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Action buttons

        button_frame = ttk.Frame(main)

        button_frame.pack(
            fill="x",
            pady=(12, 5)
        )

        ttk.Button(
            button_frame,
            text="Preview Files",
            command=self.preview_files
        ).pack(side="left")

        ttk.Button(
            button_frame,
            text="Organize Files",
            command=self.organize_files
        ).pack(side="left", padx=8)

        ttk.Button(
            button_frame,
            text="Export CSV",
            command=self.export_csv
        ).pack(side="left")

        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_preview
        ).pack(side="left", padx=8)

        ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.destroy
        ).pack(side="right")

        # Status bar

        self.status_var = tk.StringVar(
            value="Ready. Select a folder to begin."
        )

        ttk.Label(
            main,
            textvariable=self.status_var
        ).pack(anchor="w", pady=(8, 0))

    # =====================================
    # 2. BROWSE FOLDER
    # =====================================

    def browse_folder(self):

        folder = filedialog.askdirectory(
            title="Choose a folder to organize"
        )

        if folder:

            self.selected_folder = Path(folder)

            self.folder_var.set(str(self.selected_folder))

            self.clear_preview()

            self.status_var.set(
                "Folder selected. Click Preview Files."
            )

    # =====================================
    # 3. CLEAR TABLE
    # =====================================

    def clear_preview(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        self.current_results = []

        self.update_summary([])

        self.status_var.set("Preview cleared.")

    # =====================================
    # 4. DISPLAY RESULTS
    # =====================================

    def display_results(self, results):

        self.clear_table_only()

        for item in results:

            self.tree.insert(
                "",
                "end",
                values=(
                    item.get("filename", ""),
                    item.get("category", ""),
                    item.get("source", ""),
                    item.get("destination", ""),
                    item.get("status", "")
                )
            )

        self.current_results = results

        self.update_summary(results)

    def clear_table_only(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

    # =====================================
    # 5. UPDATE SUMMARY
    # =====================================

    def update_summary(self, results):

        summary = get_summary(results)

        self.summary_var.set(
            f"Total: {summary['total_files']}  |  "
            f"Moved: {summary['moved_files']}  |  "
            f"Preview: {summary['preview_files']}  |  "
            f"Already Organized: {summary['already_organized']}  |  "
            f"Errors: {summary['errors']}"
        )

    # =====================================
    # 6. PREVIEW FILES
    # =====================================

    def preview_files(self):

        if not self.selected_folder:

            messagebox.showwarning(
                APP_TITLE,
                "Please select a folder first."
            )

            return

        try:

            results = preview_files(
                str(self.selected_folder)
            )

            self.display_results(results)

            if not results:

                self.status_var.set("No files found.")

                messagebox.showinfo(
                    APP_TITLE,
                    "No files found in the selected folder."
                )

                return

            self.status_var.set(
                f"Preview completed: {len(results)} file(s). "
                "No files have been moved."
            )

        except Exception as error:

            messagebox.showerror(
                "Preview Error",
                str(error)
            )

    # =====================================
    # 7. ORGANIZE FILES
    # =====================================

    def organize_files(self):

        if not self.selected_folder:

            messagebox.showwarning(
                APP_TITLE,
                "Please select a folder first."
            )

            return

        try:

            preview_results = preview_files(
                str(self.selected_folder)
            )

            if not preview_results:

                messagebox.showinfo(
                    APP_TITLE,
                    "No files found."
                )

                return

            movable_files = sum(
                1 for item in preview_results
                if item["status"] == "Preview"
            )

            if movable_files == 0:

                self.display_results(preview_results)

                messagebox.showinfo(
                    APP_TITLE,
                    "All files are already organized."
                )

                return

            answer = messagebox.askyesno(
                "Confirm Organization",

                f"{movable_files} file(s) will be moved.\n\n"

                f"Selected folder:\n"
                f"{self.selected_folder}\n\n"

                "Please make sure you selected the correct folder "
                "and have a backup.\n\n"

                "Continue?"
            )

            if not answer:

                self.status_var.set(
                    "Organization cancelled."
                )

                return

            results = organize_files(
                str(self.selected_folder)
            )

            self.display_results(results)

            summary = get_summary(results)

            message = (
                f"Organization completed!\n\n"
                f"Total files: {summary['total_files']}\n"
                f"Moved: {summary['moved_files']}\n"
                f"Already organized: {summary['already_organized']}\n"
                f"Errors: {summary['errors']}"
            )

            if summary["errors"] > 0:

                messagebox.showwarning(
                    "Completed with Errors",
                    message
                )

            else:

                messagebox.showinfo(
                    "Success",
                    message
                )

            self.status_var.set(
                "Organization completed successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Organization Error",
                str(error)
            )

    # =====================================
    # 8. EXPORT CSV REPORT
    # =====================================

    def export_csv(self):

        if not self.current_results:

            messagebox.showwarning(
                APP_TITLE,
                "Please preview or organize files first."
            )

            return

        report_path = filedialog.asksaveasfilename(

            title="Save Organization Report",

            defaultextension=".csv",

            initialfile="File_Organizer_Report.csv",

            filetypes=[
                ("CSV Files", "*.csv"),
                ("All Files", "*.*")
            ]
        )

        if not report_path:

            return

        try:

            saved_file = export_report(
                self.current_results,
                report_path
            )

            messagebox.showinfo(
                "Report Exported",
                f"CSV report saved successfully!\n\n{saved_file}"
            )

            self.status_var.set(
                "CSV report exported successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Export Error",
                str(error)
            )


# =========================================
# 9. APPLICATION ENTRY POINT
# =========================================

def main():

    root = tk.Tk()

    app = FileOrganizerApp(root)

    root.mainloop()


if __name__ == "__main__":

    main()
