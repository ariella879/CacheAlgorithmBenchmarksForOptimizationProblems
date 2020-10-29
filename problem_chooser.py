import os,subprocess,sys
import html
import time
import shutil

name_of_dir = time.strftime("%Y__%m__%d__%H__%M__%S")
directory = name_of_dir
parent_dir = "/Users/ariella/Desktop/untouched/polar-anchorage-92883/"
path = os.path.join(parent_dir, directory)

def make_dir():
    os.mkdir(path)
    shutil.copy("/Users/ariella/Desktop/polar-anchorage-92883/public/photo1.png", path)
    return path


def generate_results(results_location, ):
    opening_boilerplate = '<html><head></head><body>'
    image_tag = '<img src= "'
    image_ending = ' ">'
    end = "</body></html>"
    name_of_file = "t"
    complete_name = os.path.join(results_location, name_of_file+".html")
    image_path = os.path.join(results_location, "photo1.png")

    if subprocess.call("./a.out") == 0:
        f = open(complete_name, "w")
        f.write(opening_boilerplate)
        f.write(image_tag)
        f.write(image_path)
        f.write(image_ending)
        f.write(end)

results_location = make_dir()
generate_results(results_location)
#print(results_location)
print(name_of_dir)
