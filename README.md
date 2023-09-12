# image-name-cleanup
Sequentially rename and move images from a source to a destination.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)
* [Configuration](#configuration)

#### <a name="prerequisites"></a>Prerequisites
* A complete install of `Python 3.x`.
* Under `Downloads`, the folders containing the images you want to cleanup.

**Example**:
```
C:\Users\nso89\Downloads\Captain Kirk\89abe98de6071178edb1b28901a8f459.webp
C:\Users\nso89\Downloads\Captain Kirk\James_Kirk,_2371.webp
```

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract `image-name-cleanup-main.zip`.

**Example**:
```batch
C:\Users\nso89\image-cleanup-main
```

#### <a name="running-the-script"></a>Running the Script

1. Open `cmd.exe` and change the directory to the `image-name-cleanup-main` folder.

**Example**:
```batch
C:\Users\nso89>cd image-name-cleanup-main
```
2. Start the `main.py` script.

**Example**:
```batch
C:\Users\nso89\image-cleanup-main>python main.py
```

4. It renames and moves the images from the `source` to the `destination` folder.

**Example**:
```batch
Source: C:\Users\nso89\Downloads\Captain Kirk Destination: C:\Users\nso89\Pictures\Captain Kirk
89abe98de6071178edb1b28901a8f459.webp -> 1.webp
James_Kirk,_2371.webp -> 2.webp
Remove: C:\Users\nso89\Downloads\Captain Kirk
```

If you already have a `source` and `destination` folder with the same name, the count continues from the number of files in the `destination` folder.

5. When completed, if the `source` folder is empty, it's removed.

#### <a name="configuration"></a>Configuration

If you need to change the `source` or `destination` folder:

1. Open the `main.py` script in any text editor.
2. Locate the `SOURCE_PARENT` or `DESTINATION_PARENT` variable.

**Example**:
```python
SOURCE_PARENT = Path.home().joinpath("Downloads")
DESTINATION_PARENT = Path.home().joinpath("Pictures")
```
3. When you finish changing the variables, save and close the editor.
