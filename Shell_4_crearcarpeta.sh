#!/bin/bash

DIRECTORIO=data

if [ -d "$DIRECTORIO" ]
then
   echo "El directorio ${DIRECTORIO} existe"
else
   mkdir data
   echo "Se creó la carpeta"
fi
