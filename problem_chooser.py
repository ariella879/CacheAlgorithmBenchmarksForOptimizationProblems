import os, subprocess, sys
import html
import time
import shutil


parent_dir = "/Users/ariella/Desktop/polar-anchorage-92883/"
datestr = time.strftime("%Y__%m__%d__%H__%M__%S")
results_path = os.path.join(parent_dir, datestr)
os.mkdir(results_path)
if subprocess.call("./a.out") == 0:
  fp = open('execution_trace.log', 'w')
  fp.write('problem_chooser ran successfully')
  fp.close()
  shutil.copy("/Users/ariella/Desktop/polar-anchorage-92883/static_location/photo1.png", results_path)
  static_location = '/images/photo1.png'
  image_path = static_location
  complete_name = os.path.join(results_path, 't.html')
  image_path_to= os.path.join(results_path, 'photo1.png')
  f = open(complete_name, "w")
  f.write('<html><head></head><body><img src= "')
  f.write(image_path)
  f.write('"></body></html>')
  f.close()
  shutil.copy(image_path_to, '/Users/ariella/Desktop/polar-anchorage-92883/public' )
  shutil.copy(complete_name, '/Users/ariella/Desktop/polar-anchorage-92883/public')
else:
  fp = open('execution_trace.log', 'w')
  fp.write('problem_chooser ran with error')
  fp.close()
  print('An error occurred')
