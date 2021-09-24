FROM ubuntu:20.04

#Configuramos nuestro espacio de trabajo y seteamos la zona y la hrs
WORKDIR /tmp
ENV TZ=America/Santiago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#Actualizamos los paquetes e instalamos los escenciales para ubuntu
RUN apt -yqq update
RUN apt install -yqq build-essential 
RUN apt install -yqq libapr1-dev libaprutil1-dev libpcre3-dev
RUN apt-get install ca-certificates -y \
    && apt clean


#Instalamos los paquete necesarios para la instalacion del servidor y el servidor 
RUN apt install -yqq nodejs npm git
RUN git clone git://github.com/mafintosh/multicast-dns.git
WORKDIR /tmp/multicast-dns
RUN npm install 

#Ejecutamos las consultas por dominio multicasT cuando se corra el contenedor.
CMD node cli.js seba.local &&\
node cli.js felipe.local && sleep 1s &&\
node cli.js marcos.local && sleep 1s &&\
node cli.js example1.local && sleep 1s &&\
node cli.js example2.local && sleep 1s &&\
node cli.js example3.local && sleep 1s &&\
node cli.js example4.local && sleep 1s &&\
node cli.js example5.local && sleep 1s &&\
node cli.js example6.local && sleep 1s &&\
node cli.js example7.local

#docker build -t cliente .
#docker run --name cli --net=internet -it cliente


