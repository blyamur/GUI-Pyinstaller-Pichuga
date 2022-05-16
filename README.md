## GUI for Pyinstaller based on Tkinker
#### Version 1.2 (current)

## Что это?
Максимально легкий способ использовать PyInstaller без использования командной строки.

![Light screenshot](https://github.com/blyamur/GUI-Pyinstaller-Pichuga/blob/main/app_screen.png)

Данный код основан на старой, но все еще актуальной реализации от [vsantiago113](https://github.com/vsantiago113/PyInstallerGUI), которая к сожалению, уже несколько лет как не обновляется. Используя специально сделанной для этого проекта темой оформления для ttk, основанной на темах от [rdbende](https://github.com/rdbende/Sun-Valley-ttk-theme) и теме 
[Spring-Noon](https://github.com/blyamur/Spring-Noon-ttk-theme), попробовал дать этой реализации второе дыхание. Главной задачей стояло создать удобный и простой инструмент, который позволит в пару кликов создавать приложения, используя возможности PyInstaller и обладая при этом, самым минимум необходимых навыков, используя инструмент который прост, понятен и выглядит узнаваемо и современно.


## Как начать использовать?
1. Скачайте архив с последней версией и распакуйте в любое удобное для вас место; 

2. Установите необходимые компоненты и зависимости если такая необходимость имеется;

3. Запустите ИМЯ_ФАЙЛА.py и выбрав в окне нужные вам опции, создайте свою программу.


#### Для работы вам понадобится только содержимое папки *Pichuga*

*  **Pichuga-GUI-Pyinstaller.py** - версия на русском языке

*  **Pichuga-GUI-Pyinstaller-en.py** - English version

*  **theme** Папка с темой оформления (стили, иконки и пр.)

*  **russian-spring.tcl** - Файл темы оформления

*  **icon.ico** - иконка скрипта

Папки **build**, **dist** и файл **.spec** создаются автоматически

После распаковки содержимого архива в лубую удобную вам папку, достаточно запустить файл *Pichuga-GUI-Pyinstaller.py*, затем в открывшемся окне установить необходимые вам опции и выбрать файл скрипта, который необходимо сделать исполняемым файлом, при необходимости можно задать имя и указать путь до иконки. Далее просто жмем на конку "Начать" и ждем окончания процесса, за ходом которого, можно наблюдать в окне консоли. Готовый результат будет располагаться в папке **dist**

## Без этого, данного проекта бы не было:

[Python script: PyInstallerGUI](https://github.com/vsantiago113/PyInstallerGUI) - [vsantiago113](https://github.com/vsantiago113/)

[Tkinker theme: Sun-Valley](https://github.com/rdbende/Sun-Valley-ttk-theme) - [rdbende](https://github.com/rdbende/)

[Tkinker theme: Spring-Noon](https://github.com/blyamur/Spring-Noon-ttk-theme) - [blyamur](https://github.com/blyamur/)

[Tkinker theme: Spring-Sunset](https://github.com/blyamur/Spring-Sunset-ttk-theme) - [blyamur](https://github.com/blyamur/)


