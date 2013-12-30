#!/usr/bin/python
# Chris Rust - 20131229
# zippy: CLI unzipping tool, based on python's zipfile lib
import zipfile
import optparse
import os

def unzip(filename,path=None,password=None):
    try:
        print "[+] Unzipping file: " + filename
        zippy = zipfile.ZipFile(filename)
        zippy.extractall(path=path,pwd=password)
        print "[+] Unzip complete"
    except Exception, e:
        print "[-] ERROR: " + str(e)

def main():
    # Option parser for CLI args
    parser = optparse.OptionParser()
    parser.add_option('-f', dest='zip_file', type='string',\
            help='specify zip file')
    parser.add_option('-e', dest='export_path', type='string',\
            help='specify an export path (optional)')
    parser.add_option('-p', dest='password', type='string',\
            help='specify a password (optional)')
    (options, args) = parser.parse_args()

    # Set zip_file or print usage
    if options.zip_file is None:
        print "zippy: Extracts Zip & Zip64 files"
        parser.print_help()
        exit(0)
    else:
        zip_file = options.zip_file

    # Check that zip_file is accessible
    if not os.path.isfile(zip_file):
        print "[-] ERROR: " + zip_file + " file does not exist"
        exit(1)
    if not os.access(zip_file, os.R_OK):
        print "[-] ERROR: " + zip_file + " access denied (file not readable)"
        exit(1)

    # Check that export_path (optional) is executable
    if options.export_path is not None:
        export_path = options.export_path
        if not os.path.isdir(export_path):
            print "[-] ERROR: " + export_path + " dir does not exist"
            exit(1)
        if not os.access(export_path, os.X_OK):
            print "[-] ERROR: " + export_path + " access denied (dir not executable)"
            exit(1)

    # Unzip zip_file
    unzip(zip_file, options.export_path, options.password)

if __name__ == '__main__':
    main()
