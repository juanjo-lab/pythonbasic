# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:44:22 2020

@author: Juanjo
"""

import os as os 
import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
#                                   MAIN
opc=0
while opc!=8:
    print('---------------MENU principal-------------')
    
    print('1. EX1 . PY')
    print('2. EX2 . PY')
    print('3. EX3 . PY')
    print('4. EX4 . PY')
    print('5. EX5 . PY')
    print('6. EX6 . PY')
    print('7. EX7 . PY')
    print('8. SALIR')
    
    print('--------------------------------------')
    print('')
    opcion=float(input('Que opción desea = '))
    if opcion==1:
       ex1.main()
    elif opcion==2:
       ex2.main()
    elif opcion==3:
       ex3.main()
    elif opcion==4:
       ex4.main()
    elif opcion==5:
       ex5.main()
    elif opcion==6:
       ex6.main()
    elif opcion==7:
       ex7.main()
    elif opcion==8:
      opc=8
    
