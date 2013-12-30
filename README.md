zippy - python unzipping utility 
--------------------------------

- Unzip PKZIP (WinZip) format files, including Zip64
- Unzip password protected zip files
- Compatible with Python v2.3 or greater
- Free to use under MIT License

I recently found myself trying and failing to unzip a Zip64 file on an old UNIX box. The system didn't have access to Unzip 6.0, where support for the format was added. But, it seems the Python library zipfile has supported the format for a while now. If you happen to find yourself in the same spot, here's a script.

    $ ./zip.py
    zippy: Extracts Zip & Zip64 files
    Usage: zip.py [options]
    
    Options:
      -h, --help      show this help message and exit
      -f ZIP_FILE     specify zip file
      -e EXPORT_PATH  specify an export path (optional)
      -p PASSWORD     specify a password (optional)

<sub><sup>Note: The Python v2.3 dependency comes from the optparse lib.</sup></sub>
