import os,subprocess,sys
import html

image_name_and_location = "photo1.png"
opening_boilerplate = '<html><head></head><body>'
image_tag = '<img src= "'
image_ending = ' ">'
end = "</body></html>"
if subprocess.call("./a.out") == 0:
    f = open("/Users/ariella/Desktop/MyProj/polar-anchorage-92883/public/t.html", "w")
    f.write(opening_boilerplate)
    f.write(image_tag)
    f.write(image_name_and_location)
    f.write(image_ending)
    f.write(end)
