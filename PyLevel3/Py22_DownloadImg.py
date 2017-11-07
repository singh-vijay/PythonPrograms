import random
import urllib.request

def downloadWebImg(animal,url):
    name = random.randrange(1, 100)
    fullName = animal + str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

downloadWebImg("Tiger","https://cdn.pixabay.com/photo/2017/10/27/20/25/leopard-2895448_960_720.jpg")
downloadWebImg("Bird","https://cdn.pixabay.com/photo/2017/03/13/10/31/greylag-goose-2139296_960_720.jpg")
