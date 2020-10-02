#!/bin/bash

#install libraries not in pip
if [ "$(uname)" == "Win32" ]
then
 pip install pygame
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]
then
  yay -S python-pygame
elif [ -n "$COMSPEC" -a -x "$COMSPEC" ]
then 
  echo $0: this script does not support MacOSX \:\(
fi

#install libraries from pip
pip install numpy pyganim