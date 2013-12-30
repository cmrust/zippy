zippy - python unzipping utility 
--------------------------------

- Unzip PKZIP (WinZip) format files, including Zip64
- Unzip password protected zip files
- Compatible with Python v2.3 or greater
- Tested in Unix/Linux Bash shells (should technically work on Macs)

I recently found myself failing to extract a Zip64 file on an old UNIX box.
The system didn't have access to Unzip 6.0, where support for the format was added.
But, it seems Python's zipfile library has supported 64 bit zips for a while now.
And so, this script was born: 

    $ ./zip.py
    zippy: Extracts Zip & Zip64 files
    Usage: zip.py [options]
    
    Options:
      -h, --help      show this help message and exit
      -f ZIP_FILE     specify zip file
      -e EXPORT_PATH  specify an export path (optional)
      -p PASSWORD     specify a password (optional)

<sub><sup>Note: The Python v2.3 dependency comes from the optparse lib.
Note 2: Use freely under the MIT License.
