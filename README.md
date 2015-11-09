# phy-suite
instrucciones y archivos adaptados para el funcionamiento de la suite phy de cortexlab

si una linea empieza con '$' significa que debe ejecutarse en una terminal todo lo que le sigue al simbolo
si una linea empieza con '#' significa que debe ejecutarse en una terminal todo lo que le sigue al simbolo, asegurandose de tener permisos de administrador
donde diga USUARIO se debe reemplazar con el usuario de la computadora de trabajo

descargar la ultima version de miniconda3 de http://conda.pydata.org/miniconda.html
o a partir del siguiente script (si la pc es de 64 bits)

$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

para asegurarse que el sistema es de 64 bits, ejecutar
$ uname -a

si la salida dice x64 es de 64 bits, sino no, y en ese caso hay que descargar la versión de 32 bits.

$ bash Miniconda3-latest-Linux-x86_64.sh
Este comando debe ejecutarse desde la misma ubicación donde se encuentra el archivo descagado.

Durante la instalacion, primero presionar ENTER para continuar. 
Se muestra la licencia, apretar SPACE para ir al final y luego escribir en la terminal 'yes' para aceptar la licencia.

Al final de la instalacion va a preguntar si desea agregar estos datos al .bashrc

Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/USUSARIO/.bashrc ? [yes|no]

si se elige si, el sistema por default utilizara python instalando en ~/miniconda3
si se elige no, para utilizar conda hay que ejecutar
  export PATH=/home/USUARIO/miniconda3/bin:$PATH

sugiero poner 'no'

una vez instalado miniconda, seguimos los pasos indicados por la documentacion de phy, que son:

si el sistema se encuentra destras de un proxy

crear el archivo /home/USUARIO/.condarc con el siguiente contenido
proxy_servers:
    http: http://proxy.uba.ar:8080
    https: https://proxy.uba.ar:8080

cambiando por la direccion de proxy que corresponda

y luego generar la variable de entorno (si no esta generada por sistema)

$ export http_proxy=http://proxy.uba.ar:8080
$ export https_proxy=http://proxy.uba.ar:8080

luego de configurar el proxy, la instalacion continua normalmente

$ export PATH=/home/USUARIO/miniconda3/bin:$PATH
$ conda install conda python=3.4 pip numpy matplotlib scipy h5py pyqt ipython-notebook requests six --yes
$ conda install -c https://conda.binstar.org/kwikteam klustakwik2 --yes
$ pip install vispy
$ pip install phy
$ exit

$ phy -v

# Ejecución

luego para ejecutar phy, si no se modifico la variable PATH, cada vez que se abre una terminal nueva
se debe ejecutar

  export PATH=/home/USUARIO/miniconda3/bin:$PATH

para verificar que esta bien definida la variable de entorno PATH se puede probar

$ which phy

que deveria devolver

/home/USUARIO/miniconda3/bin/phy

agregar los archivos .prb en 

/home/USUARIO/miniconda3/lib/python3.4/site-packages/phy/electrode/probes
