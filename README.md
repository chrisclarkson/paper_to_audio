# paper_to_audio

In the past I have found it useful, when reading important papers from my field, to turn the text into speech 
so that I can listen while reading. This enhances my concentration while going through the paper-content.

Here I have created a preliminary set of scripts that scrape the text content of online papers, 
removes the references and turns it into speech.

The script name specifies the journal from which it can accept content.

The actual conversion to audio is done with a python package called `pyttsx3`- unfortunately 
this package does not convert its output directly to an mp3 file and instead the audio just plays imediately (see below- `--play` option).

If you require for the content to be stored in an mp3 file, I suggest that you forego the `--play` option 
and use the software that's available on your computer to convert the output text file to an 
mp3 file. Suggestions for resources for converting text to mp3 are [here](https://alternativeto.net/software/text-to-mp3-converter/).
Personally, when doing this on my mac, I highlight the text of interest and `right click > services > add to itunes as a spoken track`.


# prerequisite python packages
```
pip install requests

pip install bs4 #previously called BeautifulSoup (if you use an old version, just edit to--> import BeautifulSoup) 

pip install pyttsx3
```

# installation and use:

```

git clone https://github.com/chrisclarkson/paper_to_audio/

cd paper_to_audio/

python scrape_cell.py --play --index_url 'https://www.cell.com/developmental-cell/fulltext/S1534-5807(18)30919-5'
```
Hence you must specify the link to the paper of interest after `index_url`

Further controls:

```
for further instructions:

python scrape_cell.py -h

usage: scrape_cell.py [-h] [--index_url INDEX_URL] [--play]
                      [--output_file OUTPUT_FILE] [--speech_rate SPEECH_RATE]
                      [--voice VOICE]

optional arguments:

  -h, --help            show this help message and exit
  
  --index_url INDEX_URL e.g. https://www.cell.com/cell-
                        metabolism/fulltext/S1550-4131(18)30735-6
                        
  --play                specifies for the audio to be played immediately-
                        default is to not play
                        
  --output_file OUTPUT_FILE if not specified- will default to title of the paper
  
  --speech_rate SPEECH_RATE default is 220 wpm
  
  --voice VOICE         Choose any from: Alex alice alva amelie anna carmit
                        damayanti daniel diego ellen fiona Fred ioana joana
                        jorge juan kanya karen kyoko laura lekha luca luciana
                        maged mariska mei-jia melina milena moira.premium
                        monica nora paulina samantha sara satu sin-ji tessa
                        thomas ting-ting veena Victoria xander yelda yuna yuri
                        zosia zuzana
  ```
                        
