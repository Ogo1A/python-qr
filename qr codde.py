# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1teHl_GD-NWR4pnpS5IRCWHGklsN1eYgQ
"""

!pip install wifi-qrcode-generator

from wifi_qrcode_generator import wifi_qrcode
from IPython.display import Image

qr_code = wifi_qrcode("ODHIAMBO'S",hidden=False,
                      authentication_type="WPA",password="Chech2030##$$")

qr_code_img=qr_code.make_image()

qr_code_img.save("wifi_qr_code.png")

display(Image("wifi_qr_code.png"))

!git init

!git add .

!git commit -m "Initial commit"

!git config --global user.email "darren.sunday@strathmore.edu"
!git config --global user.name "Ogo1A"

!git commit -m "Initial commit"

!git remote add origin <https://github.com/Ogo1A/python-qr.git>

!git push -u origin main

!git pull origin main

!echo "# python-qr" >> README.md
!git init
!git add README.md
!git commit -m "first commit"
!git branch -M main
!git remote add origin https://github.com/Ogo1A/python-qr.git
!git push -u origin main

!git config --global user.name "Ogo1A"
!git config --global user.email "darren.sunday@strathmore.edu"
!git push -u origin main