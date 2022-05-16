import os
from os import path
import tkinter as tk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import requests

#FromRussiaWithLove | Mons (https://blog.mons.ws) | ver. 1.2 | "non-commercial use only, for personal use

class App(ttk.Frame):
	def __init__(self, parent):
		ttk.Frame.__init__(self)
		for index in [0, 1, 2]:
			self.columnconfigure(index=index, weight=1)
			self.rowconfigure(index=index, weight=1)
		self.setup_widgets()




	def setup_widgets(self):
		self.var_name = tk.BooleanVar()
		self.var_onedir = tk.BooleanVar()
		currentVersion = '1.2'

        
#1 title box
		self.aa_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.aa_frame.grid(row=0, column=0, padx=(10, 10), pady=0, columnspan=10 , sticky="n")
		
		self.label = ttk.Label(
			self.aa_frame,
			text="GUI for PyInstaller",
			justify="center",
			font=("-size", 15, "-weight", "bold"),
		)
		self.label.grid(row=0, column=0,padx=0, pady=(20, 0), columnspan=10)
#2 Option box
		self.ab_frame = ttk.LabelFrame(self, text="Options", padding=(10, 10))
		self.ab_frame.grid(
			row=0, column=0, padx=(20, 20), pady=(45, 20), sticky="ns"
		)
#Options -window -consone-nonconsole
		self.option_menu_list = [' --console', ' --windowed', ' --noconsole']
		self.var_4 = StringVar(value=self.option_menu_list[0])
		self.combobox_opt = ttk.Combobox(self.ab_frame,  state="readonly", textvariable=self.var_4, values=self.option_menu_list)
		#self.combobox_opt.current(0)
		self.combobox_opt.grid(row=1, column=0, padx=5, pady=10, columnspan=2)
		
		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('console'))
		self.button.grid(row=1, column=2, padx=5, pady=10, sticky="w")
#set name - checkbox ()
		self.var_name = tk.StringVar()
		self.var_name.set('')
		self.check_1 = ttk.Checkbutton(
			self.ab_frame, text="--name", variable=self.var_name, onvalue=' --name', offvalue='', command=lambda: build_command('')
		)
		self.check_1.grid(row=1, column=3, padx=(50, 5), pady=10, sticky="w")

		self.entry_nm = ttk.Entry(self.ab_frame)
		self.entry_nm.grid(row=1, column=4, padx=5, ipady=2, pady=(10, 10), sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('name'))
		self.button.grid(row=1, column=5, padx=5, pady=10, sticky="w")

#set onefile - checkbox ()
		self.var_onefile = tk.StringVar()
		self.var_onefile.set(' ')
		self.check_2 = ttk.Checkbutton(
			self.ab_frame, text="--onefile", variable=self.var_onefile, onvalue=' --onefile', offvalue='', command=lambda: build_command('')
		)
		self.check_2.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('onefile'))
		self.button.grid(row=3, column=2, padx=5, pady=10, sticky="w")

#set onedir - checkbox ()
		self.var_onedir = tk.StringVar()
		self.var_onedir.set('')
		self.check_3 = ttk.Checkbutton(
			self.ab_frame, text="--onedir", variable=self.var_onedir, onvalue=' --onedir', offvalue='', command=lambda: build_command('')
		)
		self.check_3.grid(row=3, column=4, padx=5, pady=10, sticky="ne")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('onedir'))
		self.button.grid(row=3, column=5, padx=5, pady=10, sticky="nsew")
#set noupx - checkbox ()
		self.var_noupx = tk.StringVar()
		self.var_noupx.set(' --noupx')
		self.check_npx = ttk.Checkbutton(
			self.ab_frame, text="--noupx", variable=self.var_noupx, onvalue=' --noupx', offvalue='', command=lambda: build_command('')
		)
		self.check_npx.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('noupx'))
		self.button.grid(row=4, column=2, padx=5, pady=10, sticky="w")
#set clean - checkbox ()
		self.var_clean = tk.StringVar()
		self.var_clean.set(' --clean')
		self.check_5 = ttk.Checkbutton(
			self.ab_frame, text="--clean  ", variable=self.var_clean, onvalue=' --clean', offvalue='', command=lambda: build_command('')
		)
		self.check_5.grid(row=4, column=4, padx=5, pady=10, sticky="ne")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('clean'))
		self.button.grid(row=4, column=5, padx=5, pady=10, sticky="nsew")
#select Script
		self.label = ttk.Label(
			self.ab_frame,
			text="Script *.py",
			justify="center",
			font=("-size", 10, "-weight", "normal"),
		)
		self.label.grid(row=5, column=0, padx=5, pady=10, columnspan=1, sticky="w")

		self.accentbutton = ttk.Button(
			self.ab_frame, text="Select", style="Accent.TButton", command=lambda: get_directory_string('script')
		)
		self.accentbutton.grid(row=5, column=1, padx=5, pady=10, sticky="w")

		self.entry_sc = ttk.Entry(self.ab_frame)
		self.entry_sc.grid(row=5, column=2, columnspan=7, ipadx=83, ipady=2, padx=(8, 5), pady=(10, 10), sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('script'))
		self.button.grid(row=5, column=5, padx=5, pady=10, sticky="nsew")
#select icon
		self.var_icon = tk.StringVar()
		self.var_icon.set('')
		self.check_6 = ttk.Checkbutton(
			self.ab_frame, text="--icon", variable=self.var_icon, onvalue=' --icon', offvalue='', command=lambda: build_command('')
			)
		self.check_6.grid(row=6, column=0, padx=5, pady=10, sticky="w")

		self.accentbutton = ttk.Button(
			self.ab_frame, text="Select", style="Accent.TButton", command=lambda: get_directory_string('icon')
		)
		self.accentbutton.grid(row=6, column=1, padx=5, pady=10, sticky="w")

		self.entry_ic = ttk.Entry(self.ab_frame)
		self.entry_ic.grid(row=6, column=2, columnspan=7, ipadx=83, ipady=2, padx=(8, 5), pady=(10, 10), sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('icon'))
		self.button.grid(row=6, column=5, padx=5, pady=10, sticky="nsew")
#select version
		self.var_version = tk.StringVar()
		self.var_version.set('')
		self.check_7 = ttk.Checkbutton(
			self.ab_frame, text="--version", variable=self.var_version, onvalue=' --version', offvalue='', command=lambda: build_command('')
			)
		self.check_7.grid(row=7, column=0, padx=5, pady=10, sticky="w")

		self.accentbutton = ttk.Button(
			self.ab_frame, text="Select", style="Accent.TButton", command=lambda: get_directory_string('version')
		)
		self.accentbutton.grid(row=7, column=1, padx=5, pady=10, sticky="w")

		self.entry_vr = ttk.Entry(self.ab_frame)
		self.entry_vr.grid(row=7, column=2, columnspan=7, ipadx=83, ipady=2, padx=(8, 5), pady=(10, 10), sticky="w")

		self.button = ttk.Button(self.ab_frame, text="?",command=lambda:show_info('version'))
		self.button.grid(row=7, column=5, padx=5, pady=10, sticky="nsew")


#3 Command line box
		self.ab_frame = ttk.LabelFrame(self, text="Command", padding=(20, 10))
		self.ab_frame.grid(
			row=1, column=0, padx=(5, 5), sticky="n"
		)
		self.entry_bl = ttk.Entry(self.ab_frame)
		self.entry_bl.insert(0, "pyinstaller --clean  --console --noupx")
		self.entry_bl.grid(row=0, column=0, ipadx=190, ipady=3, padx=(3, 3), pady=(10, 20))
#4 Build buttons
		self.bb_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.bb_frame.grid(row=2, column=0, padx=(10, 10), pady=0, columnspan=10 , sticky="n")

		self.accentbutton = ttk.Button(
			self.bb_frame, text="Build", style="Accent.TButton",command=lambda:run_build()
		)
		self.accentbutton.grid(row=0, column=0, columnspan=2, ipady=5, ipadx=29, padx=5, pady=10, sticky="nsew")

		self.button = ttk.Button(self.bb_frame, text="Cancel",command=lambda:quit())
		self.button.grid(row=0, column=2, padx=10, pady=15, ipadx=12, sticky="nsew")

#5 Copy docs check vers buttons
		self.copy_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
		self.copy_frame.grid(row=8, column=0, padx=(10, 10), pady=0, columnspan=10 , sticky="n")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="PyInstaller Manual", style="Url.TButton",command=openweb
		)
		self.UrlButton.grid(row=1, column=0, padx=20, pady=0, columnspan=2, sticky="n")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="Vers.: " +currentVersion+" ", style="Url.TButton",command=checkUpdate
		) 
		self.UrlButton.grid(row=1, column=4, padx=20, pady=0, columnspan=2, sticky="w")
		self.UrlButton = ttk.Button(
			self.copy_frame, text="Donate", style="Url.TButton",command=donate
		)
		self.UrlButton.grid(row=1, column=7, padx=20, pady=0, columnspan=2, sticky="w")




		def get_directory_string(string):
			if string == 'script':
				filename = filedialog.askopenfilename(filetypes=[('Python Script', '*.py | *.pyw')])
				self.entry_sc.delete(0, tk.END)
				if filename == '':
					pass
				else:
					self.entry_sc.insert(tk.END, str(filename))
			elif string == 'version':
				filename = filedialog.askopenfilename(filetypes=[('Version File', '*.txt')])
				self.entry_fv.delete(0, tk.END)
				if filename == '':
					pass
				else:
					self.entry_fv.insert(tk.END, str(filename))
			elif string == 'icon':
				filename = filedialog.askopenfilename(filetypes=[('Icon', '*.ico')])
				self.entry_ic.delete(0, tk.END)
				if filename == '':
					pass
				else:
					self.entry_ic.insert(tk.END, str(filename))
			build_command('')


		def build_command(*args):
			string = 'pyinstaller '+ self.var_4.get()+self.var_noupx.get()+self.var_clean.get()+self.var_onefile.get()+self.var_onedir.get() 
			if self.var_name.get() == '' or self.entry_nm.get().strip() == '':
				pass
			else:
				string += self.var_name.get()+' "'+self.entry_nm.get()+'"'
			if self.entry_sc.get().strip() == '':
				pass
			else:
				string += ' "'+self.entry_sc.get()+'"'
			if self.var_icon.get() == '' or self.entry_ic.get().strip() == '':
				pass
			else:
				string += self.var_icon.get()+' "'+self.entry_ic.get()+'"'

			if self.var_version.get() == '' or self.entry_vr.get().strip() == '':
				pass
			else:
				string += self.var_version.get()+' "'+self.entry_vr.get()+'"'
                
			self.entry_bl.delete(0, tk.END)
			self.entry_bl.insert(tk.END, string)
#Combobox
		self.combobox_opt.bind("<<ComboboxSelected>>", build_command)
        
		def run_build():
			if self.entry_sc.get().strip() == '':
				pass
			else:
				os.system(str(self.entry_bl.get().strip()))
				self.var_4.set(' --console')
				self.var_name.set('')
				self.entry_nm.delete(0, tk.END)
				self.var_onefile.set('')
				self.var_noupx.set(' --noupx')
				self.var_version.set('')
				self.entry_vr.delete(0, tk.END)
				self.entry_sc.delete(0, tk.END)
				self.var_icon.set('')
				self.entry_ic.delete(0, tk.END)
				build_command('')



def quit():
	global root
	root.quit()

def show_info(string):
	if string == 'onefile':
		messagebox.showinfo('Info', 'Create a one-file bundled executable.')
	elif string == 'name':
		messagebox.showinfo('Info', 'Optional name to assign to the project (from which the spec file name is '
									'generated). If omitted, the basename of the (first) script is used.')
	elif string == 'console':
		messagebox.showinfo('Info', 'Use a console subsystem executable (default) or use a windowed subsystem '
									'executable, which on Windows does not open the console when the program '
									'is launched')
	elif string == 'onedir':
		messagebox.showinfo('Info', 'Create a one-folder bundle containing an executable (default)')
	elif string == 'noupx':
		messagebox.showinfo('Info', 'Do not use UPX even if available (works differently between Windows and '
									'*nix)')
	elif string == 'version':
		messagebox.showinfo('Info', 'Add a version resource from FILE to the exe')
	elif string == 'icon':
		messagebox.showinfo('Info', 'If FILE is an .ico file, add the icon to the final executable.')
	elif string == 'clean':
		messagebox.showinfo('Info', 'Clean PyInstaller cache and remove temporary files before building.')
	elif string == 'script':
		messagebox.showinfo('Info', 'Path to the script in *.py | *.pyw format.')





def openweb():
	webbrowser.open_new_tab('https://pyinstaller.org/en/stable/')
def donate():
	webbrowser.open_new_tab('https://ko-fi.com/monseg')
def checkUpdate(method='Button'):
	try:
		# check for the latest version in the README file 
		github_page = requests.get('https://raw.githubusercontent.com/blyamur/GUI-Pyinstaller-Pichuga/main/README.md')
		github_page_html = str(github_page.content).split()
		
		for i in range(0,9):
			try:
				index = github_page_html.index(('1.' + str(i)))
				version = github_page_html[index]
			except ValueError:
				pass
			# display a popup if an update is found
		if float(version) > float(currentVersion):
			updateApp(version)
		else:
			if method == 'Button':
				messagebox.showinfo(title='Updates not found', message=f'Updates not found.\nCurrent version: {version}')
	# do not check for updates in offline mode
	except requests.exceptions.ConnectionError:
		if method == 'Button':
			messagebox.showwarning(title='No network access', message='No network access.\nCheck your internet connection.')
		elif method == 'Button':
			pass

def updateApp(version):
	update = messagebox.askyesno(title='Update found', message=f'A new version {version} is available. Update?')
	if update:
		webbrowser.open_new_tab('https://github.com/blyamur/GUI-Pyinstaller-Pichuga/')
        
if __name__ == "__main__":
	root = tk.Tk()
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2 
	h = h//2 
	w = w - 200
	h = h - 200
	currentVersion = '1.2'
	root.geometry('620x670+{}+{}'.format(w, h)) #window dimensions
	root.resizable(False, False)
	root.title("GUI for PyInstaller") #application window title
	root.iconbitmap('icon.ico') #application window icon
	root.tk.call("source", "russian-spring.tcl") #setting the theme
	root.tk.call("set_theme", "light") #theme style
	app = App(root)
	app.pack(fill="both", expand=True)
	root.update()
	root.mainloop()
