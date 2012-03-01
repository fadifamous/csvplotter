import matplotlib
matplotlib.use('Agg')


from time import sleep
import os , sys
import subprocess
import numpy as np
#imports for 3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def draw3d(xvalarray , yvalarray , zvalarray , len):
    fig = plt.figure()
    xd = fig.add_subplot(111, projection='3d')
    i=0
    xd.scatter(xvalarray,yvalarray,zvalarray)
    plt.show()

def save3d(xvalarray , yvalarray , zvalarray , len,name):
    fig = plt.figure()
    xd = fig.add_subplot(111, projection='3d')
    i=0
    xd.scatter(xvalarray,yvalarray,zvalarray)
    plt.savefig(name)
#append image +name

def wrongusage():
    print ""
    sys.exit(-1)


# start main function
def main():   #to use command line stuff, use argv
    #pathname="/afs/ictp.it/home/f/fbataha/project"
    #args = sys.argv[1:]
    #if len(args) != 1:
    #    wrongusage()
    #pathname = args[1]

    pathname = "/home/ffk/project/"#data/"
    #pathname/home/ffk/project/fdata/sim2k0.5MS_constrho_beta0.1
    directory = os.path.join(pathname)
    files = os.listdir(pathname)
    mydict = {}
    k=0
    for file in files :
        #print file
        if file.endswith(".csv") :
            f=open(file, 'r')
            numlines=len(f.read().split('\n'))
            #print numlines
            mydata = np.zeros((numlines,3))
            f.close()
            f=open(file, 'r')
            i=0
            for line in f.readlines():
                if (i!=0):
                    #print line    
                    entries = line.split(',')
                    mydata[i] = entries[:3]
                    #print mydata[i]
                i+=1
                mydict[file] = mydata
                xval = mydata[:,0]
                yval = mydata[:,1]
                zval = mydata[:,2]
            #print xval    
            #print mydict
            k+=1
            y=str(k)
            save3d(xval,yval,zval,numlines,y)    
            f.close()


command = ('mencoder',
           'mf://*.png',
           '-mf',
           'type=png:w=800:h=600:fps=5',
           '-ovc',
           'lavc',
           '-lavcopts',
           'vcodec=mpeg4',
           '-oac',
           'copy',
           '-o',
           'output.avi')

print "\n\nabout to execute:\n%s\n\n" % ' '.join(command)
subprocess.check_call(command)

print "\n\n The movie was written to 'output.avi'"

print "\n\n You may want to delete *.png now.\n\n"




            #sleep(3)
#/home/ffk/project/data/esfera_2000.csv            

main()



#/home/ffk/project/output.avi     
      


