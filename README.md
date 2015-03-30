# photoac-dl
The photo urls collector for [photo AC](http://www.photo-ac.com/ "写真AC") written by Python.

# Requirements
* Beautiful Soup 4
* html5lib (optional: If it don't be installed, you must edit photoac-dl.py before using.)

# How to use
    pip install beautifulsoup4 html5lib
    
    python3.4 photoac-dl.py -h
    usage: photoac-dl.py [-h] keyword
    
    The photo urls collector for photo AC written by Python.
    
    positional arguments:
      keyword

    optional arguments:
      -h, --help  show this help message and exit
    
    python3.4 photoac-dl.py keyword > urls.txt
    
    # If you use command-line downloader such as wget, cookie must be set.
    # In my case, I download them using Chrono Download Manager on Google Chrome.
