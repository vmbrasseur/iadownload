# iadownload

## NAME

`iaupload` - Download files from [Internet Archive](http://archive.org).

## SYNOPSIS

```
usage: iadownload.py [-h] [--collection COLLECTION_ID] [--item ITEM_ID]
                     --outdir OUTDIR [--verbose]

Download files from an Internet Archive collection.

optional arguments:
  -h, --help            show this help message and exit
  --collection COLLECTION_ID
                        Internet Archive collection identifier
  --item ITEM_ID        Internet Archive item identifier
  --outdir OUTDIR       Directory where the files will be saved
  --verbose             Have verbose output

```

## DESCRIPTION

 `iadownload` is a Python script I wrote to download files from all of the
items contained in a single collection at [Internet
Archive](https://archive.org).

The script can also download files from a single item.

The script creates a collection directory in the location you specify. Within that directory it will create a subdirectory for each item in the collection. These subdirectories will contain the files for their respective items.

### LIMITATIONS!

Because this script was written so I could download hundreds of books from a single collection, it currently will **only** download text-formatted files from the items. The specific formats which it will download:

* Comic Book RAR
* EPUB
* Animated GIF
* Text PDF
* Image Container PDF

In the future the script will allow for specification of the desired formats at the command line (or perhaps via a YAML config file).

As well, the script currently has no accommodations for downloading files from protected collections (access limited to certain Internet Archive patron accounts, therefore downloads require authorization). The script only downloads files from public collections. But as there are almost no protected collections on IA, this probably isn't a feature that I'll be adding any time soon.

## PREREQUISITES

### Internet Archive Python Library

This script uses the [internetarchive Python Library](https://github.com/jjjake/ia-wrapper).

To install (assumes global install):

```
sudo pip install "internetarchive[speedups]"
```

This will install not only the library but also some optional dependencies which will allow the downloads to happen more quickly.

### Cython

The Internet Archive Python Library uses [Cython](http://cython.org/) to perform concurrent downloads.

To install (assumes global install):

```
sudo pip install cython git+git://github.com/surfly/gevent.git@1.0rc2#egg=gevent
```

## OPTIONS

### --collection

Defines the
[identifier](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#identifier)
of the Internet Archive
[collection](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#collection)
from which you'd like to download files.

If this option is specified, the script will download files from every
[item](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#item)
in the collection. The files for each item will be placed in a subdirectory
named using the
[identifier](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#identifier)
of the item.

This option may not be used in conjunction with the `--item` option.

Either this option or `--item` is required for the script to function.

### --item

Defines the
[identifier](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#identifier)
of the Internet Archive
[item](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#item)
from which you'd like to download files.

If this option is specified, the script will download files for the
[item](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#item)
in the collection. The files for the item will be placed in a subdirectory named
using the
[identifier](https://github.com/vmbrasseur/IAS3API/blob/master/appendices/terminology.md#identifier)
of the item.

This option may not be used in conjunction with the `--collection` option.

Either this option or `--collection` is required for the script to function.

### --outdir

Defines the directory to which you'd like the items to be downloaded. You must have write access to this directory.

This option is required.

### --verbose

If defined, this option will enable output to STDOUT to allow you to track the progress of the downloads.

This option is optional. If it is not defined, the script will be entirely silent unless it exits due to error.

## EXAMPLE

```
./iadownload.py --collection=sfperlmongers --outdir=~/Desktop/iadownloads --verbose
```

## AUTHOR

This script is written and maintained by [VM Brasseur](http://vmbrasseur.com).

## KNOWN BUGS

All known bugs and enhancement requests are tracked in the [issues](https://github.com/vmbrasseur/iaupload/issues) on this repo.

## REPORTING BUGS OR ENHANCEMENTS

If you use this script and would like to report bugs or suggest enhancements, please use the [issues](https://github.com/vmbrasseur/iaupload/issues) on this repo.

## CONTRIBUTING

If you'd like to contribute to this project (docs, code, tests, etc.), please send a pull request.

## COPYRIGHT AND LICENSE

All work on this project is copyright the authors of said work.

The source code for this project is licensed under the Apache License v2.0.

All documentation, web, or other content are licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

Please see the `LICENSE` file for copies of these licenses.

## SEE ALSO

* [ia-wrapper](https://github.com/jjjake/ia-wrapper)
* [IAS3API Documentation](https://github.com/vmbrasseur/IAS3API)
* [iaupload](https://github.com/vmbrasseur/iaupload)
