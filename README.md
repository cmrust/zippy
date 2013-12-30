zippy
=====

python unzipping utility 
------------------------

- Unzip PK-ZIP format files, including Zip64
- Unzip password protected zip files
- Works from Unix/Linux command line
- Works with Python v2.3 or greater

I recently found myself needing to unzip a Zip64 file on an older UNIX platform. The system didn't have access to v6.0 or greater of the UnZip CLI tool, where 64 bit support was added. So, I started digging around. It seems Python has been supporting the file format for a while now, and so I whipped up this script to do some unzipping!

This code should be compatible on any Linux system running Python v2.3 or greater.

    $ ./zippy
    zippy: Extracts Zip & Zip64 files
    Usage: zippy [options]
    
    Options:
      -h, --help      show this help message and exit
      -f ZIP_FILE     specify zip file
      -e EXPORT_PATH  specify an export path (optional)
      -p PASSWORD     specify a password (optional)

Note: The Python v2.3 dependency comes from the optparse lib. I would switch to argparse, since optparse is now deprecated, but I'm trying to keep support out-of-the-box for older systems.
