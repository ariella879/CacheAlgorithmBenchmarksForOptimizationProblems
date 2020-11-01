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
  shutil.copy("/Users/ariella/Desktop/polar-anchorage-92883/public/photo1.png", results_path)
  image_path = os.path.join(results_path, 'photo1.png')
  complete_name = os.path.join(results_path, 't.html')
  f = open(complete_name, "w")
  f.write('<html><head></head><body><img src= "')
  f.write(image_path)
  f.write('"></body></html>')
  f.close()
  print(results_path)
else:
  fp = open('execution_trace.log', 'w')
  fp.write('problem_chooser ran with error')
  fp.close()
  print('An error occurred')

