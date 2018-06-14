from imutils import paths
import argparse
import requests
import cv2
import os

"""

SCRIPT FOR GETTING IMAGE URLS FROM GOOGLE
EXECUTE IT IN THE JS CONSOLE IN CHROME, SAFARI OR FIREFOX (who needs Internet Explorer?) 

------- I ------- 
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);

------- II -------

var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });

------- III -------

var textToSave = urls.toArray().join('\n');
var hiddenElement = document.createElement('a');
hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
hiddenElement.target = '_blank';
hiddenElement.download = 'urls.txt';
hiddenElement.click();
"""

"""
python download_images.py --urls urls.txt --output images/{name_of_class_folder}
"""

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
                help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
                help="path to output directory of images")
args = vars(ap.parse_args())

rows = open(args["urls"]).read().strip().split("\n")
total = 0
p = None

# this iterates and try to download the images from google
for url in rows:
    print(url)
    try:
        r = requests.get(url, timeout=60)

        p = os.path.sep.join([args["output"], "{}.jpg".format(str(total).zfill(8))])
        f = open(p, "wb")
        f.write(r.content)
        f.close()

        print("[INFO] downloaded: {}".format(p))
        total += 1

    except:
        print("[INFO] error downloading {}...skipping".format(p))

# if something went wrong, we delete the wrong downloaded images
for imagePath in paths.list_images(args["output"]):
    delete = False

    try:
        image = cv2.imread(imagePath)

        if image is None:
            delete = True

    except:
        print("Except")
        delete = True

    if delete:
        print("[INFO] deleting {}".format(imagePath))
        os.remove(imagePath)
