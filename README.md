### GUI for Pyinstaller based on Tkinker
#### Version 1.2 (current)

### Что это? | What is it?
Максимально легкий способ использовать PyInstaller с минимальным использованием командной строки. Простой инструмент, при помощи которого можно сделать ваш скрипт в формате .py в исполняемый файл .exe

> The easy way to use PyInstaller with minimal command line usage.. A simple tool to turn your .py script into an .exe executable

![Light screenshot](https://github.com/blyamur/GUI-Pyinstaller-Pichuga/blob/main/app_screen.png)

Данный код основан на старой, но все еще актуальной реализации от [vsantiago113](https://github.com/vsantiago113/PyInstallerGUI), которая к сожалению, уже несколько лет как не обновляется. Однако, скрипт по прежнему работает и полезен. Используя специально сделанной для этого проекта темой оформления для ttk, основанной на темах от [rdbende](https://github.com/rdbende/Sun-Valley-ttk-theme) и теме 
[Spring-Noon](https://github.com/blyamur/Spring-Noon-ttk-theme), попробовал дать этой реализации второе дыхание. Главной задачей стояло создать удобный и простой инструмент, который позволит в пару кликов создавать приложения, используя возможности PyInstaller и обладая при этом, самым минимум необходимых навыков, используя инструмент который прост, понятен и выглядит узнаваемо и современно.

>  This code is based on an old but still current implementation from [vsantiago113](https://github.com/vsantiago113/PyInstallerGUI), which unfortunately has not been updated for several years. However, the script still works and is useful. Using a custom ttk theme for this project based on the themes from [rdbende](https://github.com/rdbende/Sun-Valley-ttk-theme) and the theme
[Spring-Noon](https://github.com/blyamur/Spring-Noon-ttk-theme), tried to give this implementation a second wind. The main task was to create a convenient and simple tool that will allow you to create applications in a couple of clicks using the capabilities of PyInstaller and at the same time having the bare minimum of necessary skills, using a tool that is simple, understandable and looks recognizable and modern.


### Как начать использовать? | How to start using?
1. Скачайте архив с последней версией и распакуйте в любое удобное для вас место; 

2. Установите необходимые компоненты и зависимости если такая необходимость имеется;

3. Запустите *Pichuga-GUI-Pyinstaller.py* и указав нужные вам опции, создайте свою программу.

---
> 1. Download the archive with the latest version and extract it to any place convenient for you;
> 
> 2. Install the necessary components and dependencies if necessary;
> 
> 3. Run Pichuga-GUI-Pyinstaller.py and select the options you need in the window, create your program.


#### Для работы вам понадобится только содержимое папки *GUI-Pyinstaller-Pichuga*

*  **Pichuga-GUI-Pyinstaller.py** - версия на русском языке

*  **Pichuga-GUI-Pyinstaller-en.py** - версия на английском языке

*  **theme** - Папка с темой оформления (стили, иконки и пр.)

*  **russian-spring.tcl** - Файл темы оформления

*  **icon.ico** - иконка скрипта

*  **requirements_windows.txt** - Зависимости

* Папки **build**, **dist** и файл **.spec** создаются автоматически

---

> #### To work, you only need the contents of the *GUI-Pyinstaller-Pichuga* folder
> 
> *  **Pichuga-GUI-Pyinstaller.py** - Russian version
> 
> *  **Pichuga-GUI-Pyinstaller-en.py** - English version 
> 
> *  **theme** - folder with the theme (styles, icons, etc.)
> 
> *  **russian-spring.tcl** - Theme File
> 
> *  **icon.ico** - script icon
> 
> *  **requirements_windows.txt** - requirements
> 
> * The *build*, *dist* folders and *.spec* file are automatically created


После распаковки содержимого архива в любую удобную вам папку, для начала достаточно запустить файл *Pichuga-GUI-Pyinstaller.py*, затем в открывшемся окне установить необходимые вам опции и выбрать файл скрипта, который необходимо сделать исполняемым файлом, при необходимости можно задать имя и указать путь до иконки. Далее просто жмем на конку "Начать" и ждем окончания процесса, за ходом которого, можно наблюдать в окне консоли. Готовый результат будет располагаться в папке **dist**

****Внимание: Все сторонние изображения, стили, иконки и прочие дополнительные компоненты вашего приложения, после создания файла в формате .exe, обязательно необходимо скопировать из оригинальной директории, в ту директорию где у вас расположен новый файл .exe****

> After unpacking the contents of the archive into any folder convenient for you, first you just need to run the Pichuga-GUI-Pyinstaller.py file, then in the window that opens, set the options you need and select the script file that you want to make an executable file, if necessary, you can specify a name and specify the path to the icon. Next, just click on the "Build" button and wait for the end of the process, the progress of which can be observed in the console window. The finished result will be located in the **dist** folder
> 
> ****Attention: All third-party images, styles, icons and other additional components of your application, after creating a file in the .exe format, must be copied from the original directory to the directory where you have the new .exe file****

### Page in English [translate.google.com](https://github-com.translate.goog/blyamur/GUI-Pyinstaller-Pichuga?_x_tr_sl=ru&_x_tr_tl=en&_x_tr_hl=ru&_x_tr_pto=wapp)

Команда для установка необходимых компонентов

    pip install -r requirements.txt

или

    pip install pyinstaller 

Команда на сборку exe файла без использования GUI: 

    pyinstaller yourscript.py --noconsole --onefile --icon=icon.ico


---
***Графический интерфейс PyInstaller был протестирован только в Windows с использованием версии Python 3.10.2***

***Возможны перебои, баги и прочие вещи. По возможности это все исправляется. Но в целом работает...***

> ***The PyInstaller GUI has only been tested on Windows using Python version 3.10.2***
> 
> ***Interruptions, bugs and other things are possible. If possible, this will be corrected. But in general it works...***



![Light](https://github.com/blyamur/GUI-Pyinstaller-Pichuga/blob/main/action_pichuga.gif)

### Ссылки: | Links:

[PyInstaller Manual](https://pyinstaller.org/en/stable/)

[PyInstaller on GitHub](https://github.com/pyinstaller/pyinstaller) (latest version)

[Python script: PyInstallerGUI](https://github.com/vsantiago113/PyInstallerGUI) - [vsantiago113](https://github.com/vsantiago113/)

[Tkinker theme: Sun-Valley](https://github.com/rdbende/Sun-Valley-ttk-theme) - [rdbende](https://github.com/rdbende/)

[Tkinker theme: Spring-Noon](https://github.com/blyamur/Spring-Noon-ttk-theme) - [blyamur](https://github.com/blyamur/)

[Tkinker theme: Spring-Sunset](https://github.com/blyamur/Spring-Sunset-ttk-theme) - [blyamur](https://github.com/blyamur/)



### Copyrights and Licenses
Not for commercial use.


*Thanks for reading :heart_eyes_cat:*
> Спасибо за чтение!


### Did you find this useful?! | Вы нашли это  полезным ?!

Happy to hear that :) *If You want to help me, you can buy me a cup of cup of coffee :coffee: ( [yoomoney](https://yoomoney.ru/to/41001158104834) or [PayPal](https://paypal.me/enkonu) or [ko-fi](https://ko-fi.com/W7W460SQ3) )*

> Рад это слышать :) Если вы хотите мне помочь, вы можете угостить меня чашечкой кофе 
  
© 2022 From Russia with ❤ 


<img src="https://raw.githubusercontent.com/blyamur/GUI-Pyinstaller-Pichuga/main/shields/python-3.svg" width="100"> <img src="https://raw.githubusercontent.com/blyamur/GUI-Pyinstaller-Pichuga/main/shields/release-date.svg" width="170">
