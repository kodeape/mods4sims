# mods4sims

mods4sims is a Python tool that tries to remove some of the hassle tied to updating your Sims 4 mods. After initial setup, you only need to provide download links for the mods. The tool will download the mods for you, unzip them and put them into your Mods folder. The tool can also auto-backup your mods, saves, tray etc. prior to the installation.

## Getting started

This section will guide you in the first-time setup and the usage of the tool.

### Install Python

The first thing you need to do is install Python if you don't have it yet. Python is a high-level programming language that's very popular for small applications and casual projects such as this.

You can download the newest Python version from the [official download site](https://www.python.org/downloads/). Run the executable when it has finished downloading, and follow the steps in the wizard to install Python on your computer. Going with the default choices is fine.

### Install dependencies

Dependencies are secondary software that a program depends on in order to function correctly, for example Python packages. So far, mods4sims only has one dependency aside from Python itself - the `requests` package for Python. To install `requests`, you need to open your terminal of choice. If you're new, just use Windows PowerShell on Windows or Terminal on MacOS.

We'll use pip (package installer for Python) to install `requests` with the following command in the terminal:

```ps
$ pip3 install requests
```

If the `pip3` command wasn't recognized, try the following:

```ps
$ python3 -m pip install requests
```

**Note:** the Python keyword (`python3` in the command above) can differ between terminals. In PowerShell and Git Bash, the keyword is `py`. If neither `py` nor `python3` works, google your issue.

### Download mods4sims

Time to actually download the tool! On the main GitHub page for mods4sims, click the green "Code" button. In the dropdown menu, click "Download ZIP". The `mods4sims-master.zip` should now start downloading on your computer. When it has finished downloading, unpack the zip wherever you want the tool to be. It doesn't matter where you put it in terms of functionality.

Just cloning the Git repository is also completely fine if you're already familiar with Git.

### Configure the tool

The configuration of the tool is in the `config.json` file. Out-of-box, it's filled out with an example configuration - you need to edit it for the tool to work for you.

Here's a table of all the fields in the configuration and what they do:

| Field         | Description          |
| ------------- | -------------------- |
| `simsdir`     | The full path to you Sims game directory, the one with the mod folder, save folder and all other game files. The mods will be installed in `simsdir`/Mods. |
| `backup`      | Object containing info on auto-backup. |
| `backup` -> `dir` | The full path to the directory in which you wish to store backup files for your game. |
| `backup` -> `folders` | A list of folders from the Sims game directory that the tool should back up (create a copy of) in the backup directory. |
| `backup` -> `enabled` | This should be `true` to enable auto-backup, and `false` to disable it. |
| `modlist`     | List where each item contains info on a mod. |
| `modlist` item -> `name` | The name of the mod. This will become the folder name for the mod files. |
| `modlist` item -> `url` | The download link for the mod. Right-click the download button you would use to download the mod and click copy link to get the download link. **Note:** the tool can only handle zipped mods - it does not support single-file `.package` mods yet! |
| `modlist` item -> `enabled` | Should be `true` if you want the tool to install the mod, and `false` if you would like to ignore it. |

Open `config.json` in your preferred text editor (for example Notepad on Windows) and edit the configuration as needed according to the table above.

### Use the tool

Using the tool is fairly simple. First, you need to get the full path to the `m4s.py` file. Then, open your terminal again, like you did when you installed dependencies, and enter the following command:

```ps
$ python3 path/to/m4s.py
```

where `python3` again should be the Python keyword for your terminal (`py` in PowerShell), and "path/to/m4s.py" should be replaced by the full path to `m4s.py`.

If you enabled backup in the configuration, you should start seeing info about which folders are being backed up. This can take some time, depending on how many files the tool has to back up. After backup (or immediately if you disabled backup), you should start seeing info about the enabled mods from your `modlist` being downloaded and unzipped.

**Note:** When trying the tool for the first time, I recommend using an empty test directory as your `simsdir` to check that everything gets installed as expected. Disable backups when doing this, as the tool won't find any of the folders you want to back up in this empty test directory.
