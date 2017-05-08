import urllib.request
import zipfile
import os

doc_zip = 'movies.zip'

print("Bajando archivo")
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
urllib.request.urlretrieve(url, doc_zip)

print("Extrayendo archivo")
zip_ref = zipfile.ZipFile(doc_zip, 'r')
zip_ref.extractall()
zip_ref.close()
