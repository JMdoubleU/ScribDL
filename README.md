## Purpose
This script bypasses [scribd.com](https://www.scribd.com/)'s paywall, allowing you to download anything listed as a document (has a URL like `https://www.scribd.com/doc/<number>/<title>`) and convert it to a PDF. I created this script because I don't believe education should be kept behind a paywall.

### Dependencies
* [ImageMagick](http://www.imagemagick.org/) - used to compile page images to a PDF
* [selenium](https://pypi.python.org/pypi/selenium) - needed because most of scribd's page content is generated with javascript

### Usage
To run the script, use:
`python scribdl.py <number> <path>` where `<number>` is the number in the document URL (`https://www.scribd.com/doc/<number>/<title>`) and `<path>` is the path to a directory where you want everything saved.

Images of each page of the document will be saved in order under `<path>/<title>/images/`. A PDF created by compiling all those images will be saved as `<path>/<title>_<number>/<title>.pdf`
