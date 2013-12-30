zippy - python unzipping utility 
--------------------------------

- Unzip PKZIP (WinZip) format files, including Zip64
- Unzip password protected zip files
- Compatible with Python v2.3 or greater

I recently found myself trying and failing to unzip a Zip64 file on an older UNIX system. The box didn't have access to Unzip 6.0, where support for the format was added. But, it seems Python's zipfile library has been supporting the format for a while now and so here's a script if you find yourself in the same spot.

    $ ./zip.py
    zippy: Extracts Zip & Zip64 files
    Usage: zip.py [options]
    
    Options:
      -h, --help      show this help message and exit
      -f ZIP_FILE     specify zip file
      -e EXPORT_PATH  specify an export path (optional)
      -p PASSWORD     specify a password (optional)

<sub><sup>Note: The Python v2.3 dependency comes from the optparse lib.</sup></sub>
