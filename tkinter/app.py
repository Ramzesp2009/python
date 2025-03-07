from tkinter import *
from tkinter import ttk
import psutil as pt
from datetime import date
import time, sys
from ctypes import windll
from string import ascii_uppercase as au



class CPU_Bar:
    def __init__(self):
        self.num_of_physical_cores = pt.cpu_count(logical=False)
        self.num_of_logical_cores = pt.cpu_count()


    def cpu_percents(self):
        return pt.cpu_percent(percpu=True)


    def get_ram_usage(self):
        return pt.virtual_memory()


class Disks:
    def __init__(self):
        self.drives = self.get_local_drives()
        self.deal_with_disks()


    def get_local_drives(self):
        drives = []
        b = windll.kernel32.GetLogicalDrives()
        for i in au:
            if b & 1:
                drives.append(i)
            b >>= 1
        return drives


    def deal_with_disks(self):
        availabli_drivers = []
        for i in self.drives:
            try:
                s = pt.disk_usage(f"{i}:\\")
                availabli_drivers.append(i)
            except PermissionError:
                pass
        self.drives = availabli_drivers



class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self["bg"] = "#000000"
        self.title("CPU, Disk, RAM Usage Monitor Bar")
        self.resizable(False, False)
        self.overrideredirect(False)
        self.attributes("-topmost", True)
        self.exit_but_text = "Exit"
        self.date_time_fr_text = "Date & Time"
        self.qf_frame_text = "Quick Functions"
        self.language_lab_text = "Language"
        self.time_format_lab_text = "Time Format"
        self.modes_lab_text = "Mode"
        self.list_modes = ["Light", "Dark"]
        self.cpu_frame_text = "CPU CORES' USAGES"
        self.disk_frame_text = "DISKS' USAGE"
        self.disk_name_title_text = "Disk Name"
        self.total_disk_title_text = "Total, GB"
        self.percent_disk_title_text = "Percent"
        self.used_disk_title_text = "Used, GB"
        self.free_disk_title_text = "Free, GB"
        self.time_format = 1
        self.cpu = CPU_Bar()
        self.disks = Disks()
        self.mode = 1
        self.lang = 0
        self.launch()

    def launch(self):
        self.loading()
        self.update()
        time.sleep(1.3)
        self.clear_win()
        self.update()
        time.sleep(1.3)
        self.set_ui()
        self.update()

    def loading(self):
        self.exit_but = Button(self, text=self.exit_but_text,
                               font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#ff0000",
                               command=self.app_exit)
        self.exit_but.pack(fill=X)
        self.date_time_fr = LabelFrame(self, text=self.date_time_fr_text,
                                       font=("SF Pro Display", "18"),
                                       foreground="#6a6a6a", background="#000000")
        self.date_time_fr.pack(fill=X)
        self.date_lab = Label(self.date_time_fr, text="88-08-8888",
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="12")
        self.date_lab.pack(side=LEFT)
        self.time_lab = Label(self.date_time_fr, text="88:88:88",
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="10")
        self.time_lab.pack(side=LEFT)
        self.am_pm = Frame(self.date_time_fr, background="#000000")
        self.am_pm.pack(side=LEFT)

        self.am, self.pm = Label(self.am_pm, text="AM", font=("SF Pro Display", "14"),
                                 foreground="#ff0000", background="#000000",
                                 width="3"), \
                            Label(self.am_pm, text="PM", font=("SF Pro Display", "14"),
                            foreground="#ff0000", background="#000000", width="3")

        self.am.pack(side=TOP); self.pm.pack(side=BOTTOM)

        self.qf_frame = LabelFrame(self, text=self.qf_frame_text,
                                   font=("SF Pro Display", "18"),
                                   foreground="#6a6a6a", background="#000000"
                                   )
        self.qf_frame.pack(fill=X)

        self.func1 = Frame(self.qf_frame, background="#000000")
        self.func1.pack(side=TOP, fill=X, expand=True)
        self.language_lab = Label(self.func1, text=self.language_lab_text,
                                  font=("SF Pro Display", "24"),
                                  foreground="#6a6a6a", background="#000000",
                                  justify=LEFT, anchor=W)
        self.language_lab.pack(side=LEFT)

        self.languages_win = ttk.Combobox(self.func1, values=["English", "Deutsch",
                                                              "Українська"],
                                          state="disabled", font=("SF Pro Display", "24"),
                                          width="10")
        self.languages_win.current(2)
        self.languages_win.pack(side=RIGHT)

        self.func2 = Frame(self.qf_frame, background="#000000")
        self.func2.pack(side=TOP, fill=X, expand=True)

        self.time_format_lab = Label(self.func2, text=self.time_format_lab_text,
                                  font=("SF Pro Display", "24"),
                                  foreground="#6a6a6a", background="#000000",
                                  justify=LEFT, anchor=W)
        self.time_format_lab.pack(side=LEFT)

        self.time_formats = ttk.Combobox(self.func2, values=["12-hour", "24-hour"],
                                         state="disabled", font=("SF Pro Display", "24"),
                                         width="7")
        self.time_formats.current(1)
        self.time_formats.pack(side=RIGHT)

        self.func3 = Frame(self.qf_frame, background="#000000")
        self.func3.pack(side=TOP, fill=X, expand=True)

        self.modes_lab = Label(self.func3, text=self.modes_lab_text,
                               state="disabled", font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#000000",
                               justify=LEFT, anchor=W, width="6")
        self.modes_lab.pack(side=LEFT)

        self.modes = ttk.Combobox(self.func3, values=self.list_modes,
                                         state="readonly", font=("SF Pro Display", "24"),
                                         width="12")
        self.modes.current(1)
        self.modes.pack(side=RIGHT)

        self.cpu_frame = LabelFrame(self, text=self.cpu_frame_text,
                                    font=("SF Pro Display", "18"),
                                    foreground="#6a6a6a", background="#000000")
        self.cpu_frame.pack(fill=BOTH)

        self.list_frames = [Frame(self.cpu_frame, background="#000000")
                            for i in range(self.cpu.num_of_physical_cores)]

        self.list_num_cores = [Label(self.list_frames[i], text=i + 1,
                                     font=["Digital-7 Mono", "36"],
                                     foreground="#ff0000", background="#000000",
                                     justify=LEFT, anchor=CENTER)
                               for i in range(self.cpu.num_of_physical_cores)]
        self.list_percent_cores = [Label(self.list_frames[i], text='188.88%',
                                         font=["Digital-7 Mono", "36"],
                                         foreground="#ff0000", background="#000000",
                                         justify=RIGHT, anchor=E, width="8")
                                   for i in range(self.cpu.num_of_physical_cores)]
        for i in self.list_frames:
            i.pack(side=TOP, fill=X, expand=True)

        for i in self.list_num_cores:
            i.pack(side=LEFT)

        for i in self.list_percent_cores:
            i.pack(side=RIGHT)

        self.disk_frame = LabelFrame(self, text=self.disk_frame_text,
                                     font=["SF Pro Display", "18"],
                                     foreground="#6a6a6a", background="#000000")
        self.disk_frame.pack(fill=BOTH)

        self.subs = Frame(self.disk_frame, background="#000000")
        self.subs.pack(side=TOP, fill=X, expand=True)

        self.disk_name_title = Label(self.subs, text=self.disk_name_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.disk_name_title.pack(side=LEFT)

        self.total_disk_title = Label(self.subs, text=self.total_disk_title_text,
                                      font=["SF Pro Display", "22"],
                                      foreground="#ff0000", background="#000000",
                                      width="12")
        self.total_disk_title.pack(side=LEFT)

        self.percent_disk_title = Label(self.subs, text=self.percent_disk_title_text,
                                        font=["SF Pro Display", "22"],
                                        foreground="#ff0000", background="#000000",
                                        width="12")
        self.percent_disk_title.pack(side=LEFT)

        self.used_disk_title = Label(self.subs, text=self.used_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.used_disk_title.pack(side=LEFT)

        self.free_disk_title = Label(self.subs, text=self.free_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.free_disk_title.pack(side=LEFT)

        self.total_disks = Label()

    def set_ui(self):
        self.exit_but = Button(self, text=self.exit_but_text,
                               font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#ff0000",
                               command=self.app_exit, activeforeground="#ffffff",
                               activebackground="#ff0000")
        self.exit_but.pack(fill=X)

        self.date_time_fr = LabelFrame(self, text=self.date_time_fr_text,
                                       font=("SF Pro Display", "18"),
                                       foreground="#6a6a6a", background="#000000")
        self.date_time_fr.pack(fill=X)

        current_date = str(date.today())
        current_date = "-".join(reversed(current_date.split('-')))

        current_time = time.strftime("%H:%M:%S")

        self.date_lab = Label(self.date_time_fr, text=current_date,
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="12")
        self.date_lab.pack(side=LEFT)

        self.time_lab = Label(self.date_time_fr, text=current_time,
                              font=("Digital-7 Mono", "36"),
                              foreground="#ff0000", background="#000000",
                              width="10")
        self.time_lab.pack(side=LEFT)

        self.am_pm = Frame(self.date_time_fr, background="#000000")
        self.am_pm.pack(side=LEFT)

        self.am, self.pm = Label(self.am_pm, text="AM", font=("SF Pro Display", "14"),
                                 foreground="#ff0000", background="#000000",
                                 width="3"), \
            Label(self.am_pm, text="PM", font=("SF Pro Display", "14"),
                  foreground="#ff0000", background="#000000", width="3")

        self.am.pack(side=TOP)
        self.pm.pack(side=BOTTOM)

        self.qf_frame = LabelFrame(self, text=self.qf_frame_text,
                                   font=("SF Pro Display", "18"),
                                   foreground="#6a6a6a", background="#000000"
                                   )
        self.qf_frame.pack(fill=X)

        self.func1 = Frame(self.qf_frame, background="#000000")
        self.func1.pack(side=TOP, fill=X, expand=True)
        self.language_lab = Label(self.func1, text=self.language_lab_text,
                                  font=("SF Pro Display", "24"),
                                  foreground="#ffffff", background="#000000",
                                  justify=LEFT, anchor=W)
        self.language_lab.pack(side=LEFT)

        self.languages_win = ttk.Combobox(self.func1, values=["English", "Deutsch",
                                                              "Українська"],
                                          state="readonly", font=("SF Pro Display", "24"),
                                          width="10")
        self.languages_win.current(2)
        self.languages_win.pack(side=RIGHT)

        self.languages_win.bind("<<ComboboxSelected>>", self.change_language)

        self.func2 = Frame(self.qf_frame, background="#000000")
        self.func2.pack(side=TOP, fill=X, expand=True)

        self.time_format_lab = Label(self.func2, text=self.time_format_lab_text,
                                     font=("SF Pro Display", "24"),
                                     foreground="#ffffff", background="#000000",
                                     justify=LEFT, anchor=W)
        self.time_format_lab.pack(side=LEFT)

        self.time_formats = ttk.Combobox(self.func2, values=["12-hour", "24-hour"],
                                         state="readonly", font=("SF Pro Display", "24"),
                                         width="7")
        self.time_formats.current(1)
        self.time_formats.pack(side=RIGHT)
        self.time_formats.bind("<<ComboboxSelected>>", self.change_format)

        self.func3 = Frame(self.qf_frame, background="#000000")
        self.func3.pack(side=TOP, fill=X, expand=True)

        self.modes_lab = Label(self.func3, text=self.modes_lab_text,
                               font=("SF Pro Display", "24"),
                               foreground="#ffffff", background="#000000",
                               justify=LEFT, anchor=W, width="6")
        self.modes_lab.pack(side=LEFT)

        self.modes = ttk.Combobox(self.func3, values=self.list_modes,
                                  state="readonly", font=("SF Pro Display", "24"),
                                  width="12")
        self.modes.current(1)
        self.modes.pack(side=RIGHT)

        self.cpu_bar()
        self.disk_bar()
        self.configure_date_and_time()


    def cpu_bar(self):
        self.cpu_frame = LabelFrame(self, text=self.cpu_frame_text,
                                    font=("SF Pro Display", "18"),
                                    foreground="#6a6a6a", background="#000000")
        self.cpu_frame.pack(fill=BOTH)

        self.list_frames = [Frame(self.cpu_frame, background="#000000")
                            for i in range(self.cpu.num_of_physical_cores)]

        self.list_num_cores = [Label(self.list_frames[i], text=i + 1,
                                     font=["Digital-7 Mono", "36"],
                                     foreground="#ff0000", background="#000000",
                                     justify=LEFT, anchor=CENTER)
                               for i in range(self.cpu.num_of_physical_cores)]
        self.list_percent_cores = [Label(self.list_frames[i], text='188.88%',
                                     font=["Digital-7 Mono", "36"],
                                     foreground="#ff0000", background="#000000",
                                     justify=RIGHT, anchor=E, width="8")
                               for i in range(self.cpu.num_of_physical_cores)]
        for i in self.list_frames:
            i.pack(side=TOP, fill=X, expand=True)

        for i in self.list_num_cores:
            i.pack(side=LEFT)

        for i in self.list_percent_cores:
            i.pack(side=RIGHT)

        self.configure_cpu_bar()


    def disk_bar(self):
        self.disk_frame = LabelFrame(self, text=self.disk_frame_text,
                                     font=["SF Pro Display", "18"],
                                     foreground="#6a6a6a", background="#000000")
        self.disk_frame.pack(fill=BOTH)

        self.subs = Frame(self.disk_frame, background="#000000")
        self.subs.pack(side=TOP, fill=X, expand=True)
        self.disk_name_title = Label(self.subs, text=self.disk_name_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.disk_name_title.pack(side=LEFT)

        self.total_disk_title = Label(self.subs, text=self.total_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.total_disk_title.pack(side=LEFT)

        self.percent_disk_title = Label(self.subs, text=self.percent_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.percent_disk_title.pack(side=LEFT)

        self.used_disk_title = Label(self.subs, text=self.used_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.used_disk_title.pack(side=LEFT)

        self.free_disk_title = Label(self.subs, text=self.free_disk_title_text,
                                     font=["SF Pro Display", "22"],
                                     foreground="#ff0000", background="#000000",
                                     width="12")
        self.free_disk_title.pack(side=LEFT)

        self.total_disks = Label()


    def change_format(self, event):
        self.time_format = self.time_formats.current()
        self.time_formats.current(self.time_format)

    def configure_date_and_time(self):
        current_date = str(date.today())
        current_date = "-".join(reversed(current_date.split('-')))
        time_: str = time.strftime("%H:%M:%S").split(":")
        buf = time_.copy()
        if self.time_formats.current() == 0:
            time_[0] = f"{int(time_[0]) % 12:02d}" if time_[0] != "12" else "12"
            self.time_lab["text"] = ":".join(time_)
            if int(buf[0]) in range(0, 12):
                self.am["foreground"] = "#ff0000"
                self.pm["foreground"] = "#000000"
            else:
                self.am["foreground"] = "#000000"
                self.pm["foreground"] = "#ff0000"
        else:
            self.time_lab["text"] = ":".join(time_)
            self.am["foreground"] = "#000000"
            self.pm["foreground"] = "#000000"

        self.after(1000, self.configure_date_and_time)


    def configure_cpu_bar(self):
        percent = self.cpu.cpu_percents()
        for i in range(len(self.list_percent_cores)):
            self.list_percent_cores[i]["text"]  = f"{percent[i]:.2f}%".zfill(7)
        self.after(750, self.configure_cpu_bar)


    def change_language(self, event):
        language = self.languages_win.current()
        self.lang = language
        self.languages_win.current(language)
        if self.languages_win.current() == 0:   # English
            self.exit_but_text = "Exit"
            self.date_time_fr_text = "Date & Time"
            self.qf_frame_text = "Quick Functions"
            self.language_lab_text = "Language"
            self.time_format_lab_text = "Time Format"
            self.modes_lab_text = "Mode"
            self.list_modes = ["Light", "Dark"]
            self.cpu_frame_text = "CPU CORES' USAGES"
            self.disk_frame_text = "DISKS' USAGE"
            self.disk_name_title_text = "Disk Name"
            self.total_disk_title_text = "Total, GB"
            self.percent_disk_title_text = "Percent"
            self.used_disk_title_text = "Used, GB"
            self.free_disk_title_text = "Free, GB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab["text"] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.modes.current(self.mode)
            self.update()
        elif self.languages_win.current() == 1:   # Deutsch
            self.exit_but_text = "Ausgang"
            self.date_time_fr_text = "Zeitformat"
            self.qf_frame_text = "Schnell Funktionen"
            self.language_lab_text = "Sprache"
            self.time_format_lab_text = "Zeit Format"
            self.modes_lab_text = "Mode"
            self.list_modes = ["Hell", "Dunkel"]
            self.cpu_frame_text = "Verwendung CPU"
            self.disk_frame_text = "DISKS' Verwendung"
            self.disk_name_title_text = "Disk Name"
            self.total_disk_title_text = "Total, GB"
            self.percent_disk_title_text = "Percent"
            self.used_disk_title_text = "Verwendung, GB"
            self.free_disk_title_text = "Frei, GB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab["text"] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.modes.current(self.mode)
            self.update()
        elif self.languages_win.current() == 2:   # Українська
            self.exit_but_text = "Вихід"
            self.date_time_fr_text = "Дата і Час"
            self.qf_frame_text = "Швидкі функції"
            self.language_lab_text = "Мови"
            self.time_format_lab_text = "Формат часу"
            self.modes_lab_text = "Режим"
            self.list_modes = ["Світлий", "Темний"]
            self.cpu_frame_text = "Використання ЦПУ"
            self.disk_frame_text = "Використання дисків"
            self.disk_name_title_text = "Назва диску"
            self.total_disk_title_text = "Всього, GB"
            self.percent_disk_title_text = "Процент"
            self.used_disk_title_text = "Використано, GB"
            self.free_disk_title_text = "Вільно, GB"
            self.exit_but["text"] = self.exit_but_text
            self.date_time_fr["text"] = self.date_time_fr_text
            self.qf_frame["text"] = self.qf_frame_text
            self.language_lab["text"] = self.language_lab_text
            self.time_format_lab["text"] = self.time_format_lab_text
            self.modes_lab["text"] = self.modes_lab_text
            self.modes["values"] = self.list_modes
            self.cpu_frame["text"] = self.cpu_frame_text
            self.disk_frame["text"] = self.disk_frame_text
            self.disk_name_title["text"] = self.disk_name_title_text
            self.total_disk_title["text"] = self.total_disk_title_text
            self.percent_disk_title["text"] = self.percent_disk_title_text
            self.used_disk_title["text"] = self.used_disk_title_text
            self.free_disk_title["text"] = self.free_disk_title_text
            self.modes.current(self.mode)
            self.update()


    def clear_win(self):
        for i in self.winfo_children():
            i.destroy()

    def app_exit(self):
        self.destroy()
        sys.exit()


root = Application()
root.mainloop()