#!/usr/bin/python

import sys,getopt
import time
import glob
import numpy as np
import time

input_file_patt = 'prueba'
output_file = 'output.dat'

def convert(input_file_patt, output_file,tetrode,filesN=None,appendStrobe=False,channels=[],offset=0,totCh=25):

  if channels == []:
    for i in tetrode:
      for n in range((i-1)*4,i*4):
        channels.append(n+offset)

    if appendStrobe == True:
      channels.append(totCh-1)

  files=glob.glob(input_file_patt+'*')
  n = len(files)
  if n==0:
    assert 'Ruta inexistente'
  if filesN is None:
    fstart = 0
    fend = n-2
  else:
    fstart = filesN[0]
    fend = filesN[1]


  fout = open(output_file,'wb')
  data = None
  for i in range(fstart,fend+1):
    fin = input_file_patt+str(i)
    print ('File:', i-fstart+1,'/', fend-fstart+1, '->', fin)
    newdata=np.fromfile(fin,dtype='int16',count=-1)
    newdata.reshape(-1,totCh)[:,channels].tofile(fout)

  fout.close()

def show_help():
    print ('  python bin2dat.py -i <inputpattern> -o <outputfile> [-F X,Z][-T 1,...,M] [-S True|False] [-C 0,...,N-1] -h')
    print ('   -i    Patron de archivos de entrada  (nombre de archivo incluyendo el "_" o "-" final antes del ultimo numero)')
    print ('   -o    Nombre de archivo de salida')
    print ('   -F    opcional, debe indicarse el numero inicial (X) y final (Z) de archivos a procesar (incluye a Z).')
    print ('         Si no se indica se utilizan todos los archivos que tengan el mismo patron')
    print ('   -T    opcional, debe indicarse una cadena de numeros de 1 a 6 separado de comas, que indica')
    print ('         los tetrodos ')
    print ('   -S    opcional, indica si se agrega el canal 25')
    print ('   -C    opcional, debe indicarse una cadea de numeros de 0 a 23 (o 24, donde 24 es strobe) que indica los canales')
    print ('         que se van a utilizar. Al usar esta opcion se ignora la opcion -T y -S')
    print ('   -Q    opcional, indica si hay que sumar un offset a cada canal (default 0)')
    print ('   -N    opcional, total de canales (default 25) que tiene el registro independiente de cuantos se utilicen (sirve')
    print ('         para identificar cada los registros correspondientes a cada instante de tiempo')
    print ('   -h    muestra esta ayuda')
    print (' ')
    print ('  ejemplos:')
    print ('    python bin2dat.py -i ../../registro/030315/prueba12LC_ -o salida.dat')
    print ('    python bin2dat.py -i prueba12LC_ -o salida.dat -F 0,49 -T 1,2,3')
    print ('    python bin2dat.py -i prueba12LC_ -o salida.dat -F 15,23 -T 1,2,3 -S ')
    print ('    python bin2dat.py -i prueba12LC_ -o salida.dat -F 0,49 -C 0,2,5,18')
    print ('    python bin2dat.py -i 20160101-1- -o salida.dat -F 1,5 -C 2,4,5,18 -Q 3 -N 40')
    print (' ')
    print ('  orden de electrodos I1: 1 2 11 16 10 6 14 15 9 4 7 13 3 5 8 12 17 18 25 20 28 32 23 24 29 26 30 31 19 21 22 27')

def main(argv):
  inputpatt = ''
  outputfile = ''
  tetrode = range(1,7) # si no se define se usan todos los tetrodos
  strobe = False      # si no se especifica, no se agrega
  filesN = None
  channels = []
  totalChannels = 25
  offset = 0
  try:
    opts, args = getopt.getopt(argv,"hi:o:F:T:S:C:Q:N:",["ifile=","ofile=","filesN=","tetrode=","strobe","channels=","offset=","totalChannels="])
  except getopt.GetoptError:
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))
    print ('ARGV      :', sys.argv[1:])
    show_help()
    sys.exit(2)
  for opt, arg in opts:
    #print opt
    #print arg
    if opt == '-h':
      show_help()
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputpatt = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
    elif opt in ("-F", "--filesN"):
      filesN = [int(i) for i in arg.split(',')]
    elif opt in ("-T", "--tetrode"):
      tetrode = [int(i) for i in arg.split(',')]
    elif opt in ("-S", "--strobe"):
      strobe = True
    elif opt in ("-C", "--channels"):
      channels = [int(i) for i in arg.split(',')]
    elif opt in ("-Q", "--offset"):
      offset = arg
    elif opt in ("-N", "--totalChannels"):
      totalChannels = int(arg)
  print ('Input pattern is :', inputpatt+'*')
  print ('File num filter  :', filesN)
  print ('Output file is   :', outputfile)
  print ('Tetrodes         :', tetrode)
  print ('Channels         :', channels)
  print ('TotalChannels    :', totalChannels)
  print ('Add Strobe       :', strobe)
  print ('Offset           :', offset)
  convert(inputpatt,outputfile,tetrode,filesN,strobe,channels,offset,totalChannels)

if __name__ == "__main__":
   main(sys.argv[1:])

