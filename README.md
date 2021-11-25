# Proyecto final
El propósito de este desarrollo es poner a prueba los conocimientos adquiridos en la asignatura de sistemas embebidos, aplicándolos a una solución de ingeniería haciendo uso de sistemas embebidos de alto nivel y sensores. Los temas empleados para el desarrollo son: 

- Uso de comandos en bash
- Instalación y configuración de librerías y puertos 
- Otorgar permisos
- Lectura de sensores
- Protocolo de comunicación MQTT para envío y recepción de datos 
- Uso de systemd

## Envío a plataforma IoT y medición de variables ambientales (humedad, temperatura y luz), para aplicaciones hidropónicas utilizando un sistema embebido de alto nivel (Raspberry Pi).

La ejecución de los scripts y el uso de los archivos de configuración de este repositorio le permitirán adquirir información de dos sensores desde que la maquina es encendida, guardar los datos en un archivo cada 5 segundos para luego ser enviados a una plataforma de IoT cada minuto utilizando una tarea programada y leer los datos enviados desde la plataforma cada 30 segundos para realizar acciones en el sistema embebido (encender y apagar un LED).

## Pre-requisitos 📋

- **Hardware**
  - Raspberry Pi 1 o superior con su respectivo adaptador de corriente
  - Sensor BME280 (Temperatura, humedad y presión)
  - Sensor BH1750 (Luz)
  - Resistencia 270 Ohms
  - Jumpers
  - LED
  - Memoria SD 16 Gb (sugerida) o superior

- **Software**
  - Raspberry Pi OS (Debian)
  - Registro en la plataforma Adafruit IO 

## Instalación 🔧

Antes de empezar, necesita tener formateada la memoria SD y el sistema operativo instalado la Raspberry Pi. Para esto puede dirigirse a la página oficial de [Raspberry Pi](https://www.raspberrypi.com/software/) y seguir los pasos indicados.

Una vez tenga instalado el OS y su Raspberry funcionando deberá instalar algunas librerías para la correcta ejecución de los scripts contenidos en este repositorio. Para esto puede utilizar [SSH](https://www.ionos.es/digitalguide/servidores/configuracion/activar-ssh-en-raspberry-pi/) o la interfaz gráfica utilizando la consola.

**Ejecute los siguientes comandos en su consola:**

  - $ sudo pip3 install RPi.bme280
  - $ sudo pip3 install adafruit-io
  - $ sudo apt-get install wiringpi
  - $ sudo apt-get install i2c-tools
 
  Para copiar los scripts en la Raspberry Pi, debe crear primero la carpeta "ProyectoFinal" en la ruta pi/Documents/ y copiar allí los archivos .py que se encuentran en la carpeta "Códigos" de este repositorio, de tal modo que la ruta donde estarían los archivos quedaría de la siguiente forma: pi/Documents/ProyectoFinal/.
  Una vez copiado los archivos, necesitará otorgarle permisos de ejecución a los archivos main.py, read_file.py y read_switch.py. Esto lo puede hacer usando el siguiente comando:
  **$ chmod u=x {archivo.py}**
  
  Los archivos de configuración para ejecutar las tareas programadas se encuentran en la carpeta "systemd" de este repositorio y debe ubicarlos en la ruta /etc/systemd/system/ de la raspberry. Para esto necesita permisos de super usuario.
  
**Conexiones**

Los sensores se conectan por el bus I2C 1 de la raspberry y el LED en el GPIO 17 como se aprecia en la siguiente [imagen](https://github.com/carodriguezc87/Proyecto_final/blob/83a111a619e9d4bd4c97e752e8b0a4ea2f26aa75/Conexiones.jpg). Para mas detalles del pinado, consulte el siguiente [link](https://pinout.xyz/).

## Pruebas ⚙️

Antes de ejecutar las pruebas debera crear en la plataforma "Adafruit IO" el entorno gráfico para la recepción y envio de datos. Para esto debe crear un dashboard llamado "hidroponico" y los siguientes feeds asociadaos a dicho tablero de la sigueinte manera:
 - luminocidad
 - humedad
 - temperatura
 - led

De modo tal que los "Topic's" deben quedar nombrados de la siguiente manera:

 - hidroponico.luminocidad
 - hidroponico.humedad
 - hidroponico.temperatura
 - hidroponico.led

Para los feed luminocidad, humedad y temperatura seleccione el bloque de tipo indicador (Gauge) y el del led, seleccione el bloque de tipo conmutador (Toggle).

Adicional, debe reemplazar en los archivos "read_file.py" y "read_switch.py", que fueron copiados previamente a la Raspberry, las constantes IO_KEY e IO_USERNAME por los valores que le otorga la plataforma Adafruit IO.

>Para más detalles consulte la documentación en los siguientes enlaces:
>- [Crear Dashboard y feeds](https://learn.adafruit.com/welcome-to-adafruit-io/getting-started-with-adafruit-io)
>- [Consultar llave y usuario](https://learn.adafruit.com/welcome-to-adafruit-io/securing-your-io-account) 

### Prueba 1
Ejecute los siguientes comandos:

 - **$ sudo systemctl daemon-reload**
 - **$ sudo systemctl start dataloger.service**

Esta instrucción ejecuta el código para leer los datos de los sensores y crea un archivo llamado "variables.csv" en la ruta pi/Documents/ProyectoFinal/.
Verifique que se esten guardando datos cada 5 segundos.

### Prueba 2
Ejecute el siguiente comando:
 - **$ sudo systemctl start send_data.timer**

Esta instrucción permite que se lea el último dato del archivo "variable.csv" y lo envíe a la plataforma Adafruit IO cada minuto. Verifique en la plataforma que se estan recibiendo los datos.

### Prueba 3
Ejecute el siguiente comando:
 - **$ sudo systemctl start switch.timer**

Este permite que la raspberry este atenta al mensaje enviado por el feed "hidroponico.led" de la platafaorma Adafruit IO y dependiendo del mensaje encendará o apagara el led. El mensaje enviado debe ser On o Off.

### Prueba 4 
Si las anteriores pruebas fueron satisfactorias, se podra habilitar las tareas para que se ejecuten desde que el sistema se encienda, de la sigueinte manera:

- **$sudo systemctl enable dataloger.service**
- **$sudo systemctl enable send_data.timer**
- **$sudo systemctl enable switch.timer**

Reinice la Raspberry y verifique que las tareas se ejecuten como en las pruebas 1, 2 y 3 sin necesidad de volver a ejecutar los comandos.


## Autores✒️

- Ingrid Zulay Casallas Rodríguez
- Carlos Alberto Rodríguez Cucanchón
