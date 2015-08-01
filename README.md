# photoac-dl

The photo urls collector for [photo AC](http://www.photo-ac.com/ "写真AC") written in Python.

写真素材を提供する写真ACから特定のキーワードの写真のダウンロードURLを収集するスクリプトです．  

# Requirements

* Beautiful Soup 4
* lxml or html5lib (optional)

# How to use

```bash
pip install beautifulsoup4 lxml

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
```