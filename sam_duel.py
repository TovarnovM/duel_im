# Пример файла с результатами (с готовой функцией управления), 
# который нужно залить по ссылке https://www.dropbox.com/request/hCtzOaqvFZoTMYKpDf4P


__author__ = "Самойлов Степан Дмитриевич СМ6-62" # автор 
__email__ = "SamoilovStepan2017@yandex.ru"                  # email 
additional_info = \
"""
ссылка в вк https://vk.com/sobiraet_mama_syna_v_shkoly
"""

dependencies = {                           # Словарь (str->str) с необходимыми для функции зависимостями "имя пакета в pip"->"версия"
    "numpy": "1.18.1"
}

import math
import numpy as np

def brain_foo(input_dict):
    
    res = {}
    navernytii_ygli = 0
    if input_dict['time'] == 0:
        navernytii_ygli = float(input_dict['alpha'])
          
    lychi = input_dict['rays_intersected']

    
    
    if (input_dict['enemies'] == []):
        if (min (lychi)<=10) and (input_dict['hp']!=1) and (lychi[0]>1) and (lychi[9]>1) and (max(lychi)<20):
            
            if ((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2==(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2):
                if (input_dict['theta']<50):
                    res = { 'move' : 1, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2<(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2): 
                if (input_dict['theta']<50):
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2>(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2): 
                if (input_dict['theta']<50):
                    res = { 'move' : 1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' :1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }      
                    
                    
        elif (max(lychi)<10) and (min (lychi)>=1) and (input_dict['hp']!=1) and (lychi[0]>1) and (lychi[9]>1):
            
            if ((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2==(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2):
                if (input_dict['theta']<90):
                    res = { 'move' : 1, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1,  'fire' : np.random.uniform (0.9,1), 'vision': -0.5}
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2<(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2):
                if (input_dict['theta']<90):
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5}
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2>(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2): 
                if (input_dict['theta']<90):
                    res = { 'move' : 1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
                  
        
        elif ((max(lychi)<1) or (min(lychi)<1)) and (input_dict['hp']!=1):
            res = { 'rotate': np.random.uniform(-1,-0.7), 'fire' : np.random.uniform (0.9,1), 'vision': 0.2, 'move' : np.random.uniform (0.2,1)}
                 
                
        elif (min (lychi)<=10) and (input_dict['hp']!=1) and (lychi[0]>1) and (lychi[9]>1) and (max(lychi)>=20):
            if ((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2==(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2):
                if (input_dict['theta']<60):
                    res = { 'move' : 1, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2<(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2): 
                if (input_dict['theta']<60):
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'rotate': 0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
            elif((lychi[0]+lychi[1]+lychi[2]+lychi[3]+lychi[4])//2>(lychi[5]+lychi[6]+lychi[7]+lychi[8]+lychi[9])//2): 
                if (input_dict['theta']<60):
                    res = { 'move' : 1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
                else:
                    res = { 'move' : 1, 'rotate': -0.5, 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
        
        else:
            if (input_dict['theta']<10):
                res = {'rotate': np.random.uniform(-1,-0.5), 'move' :np.random.uniform (0.3,1), 'fire' : np.random.uniform (0.9,1), 'vision': 0.5}
            else:
                res = { 'rotate': np.random.uniform(-1,-0.5), 'move' : np.random.uniform (0.3,1), 'fire' : np.random.uniform (0.9,1), 'vision': -0.5 }
        

        
        
        
        
        
    elif (input_dict['enemies'] != []):
        res = {}
        n= input_dict['alpha'] // 360
        ygol = input_dict['alpha'] - n*360
        a = input_dict['enemies']
        res = {'fire':np.random.uniform (0.9,1)}
        velichina_povorota = a[0][0] - ygol    
        
        if (ygol != a[0][0]) and (abs(a[0][1])>7):
            if velichina_povorota<0:
                if (input_dict['theta']<20):
                    res = {'rotate': a[0][0]/50, 'fire' : 1, 'move':  0.2, 'vision': 1}
                else:
                    res = {'rotate': a[0][0]/50, 'fire' : 1, 'move': 0.2, 'vision': -1}
            else:
                if (input_dict['theta']<20):
                    res = {'rotate': -a[0][0]/50, 'fire' : 1, 'move': 0.2, 'vision': 1}
                else:
                    res = {'rotate': -a[0][0]/50, 'fire' : 1, 'move': 0.2, 'vision': -1}
        
        
        elif (ygol != a[0][0]) and (abs(a[0][1])<=7) and (abs(a[0][1])>=5):
            if velichina_povorota<0:
                if (input_dict['theta']<15):
                    res = {'rotate': a[0][0]/50,'fire' : 1, 'move':  0.1, 'vision': 1}
                else:
                    res = {'rotate': a[0][0]/50,'fire' : 1,  'move':  0.1,'vision': -1}
            else:
                if (input_dict['theta']<15):
                    res = {'rotate': -a[0][0]/50,'fire' : 1,  'move':  0.1,'vision': 1}
                else:
                    res = {'rotate': -a[0][0]/50,'fire' : 1,  'move':  0.1,'vision': -1}
                    
                    
        elif (ygol != a[0][0]) and (abs(a[0][1])<5):
            if velichina_povorota<0:
                if (input_dict['theta']<10):
                    res = {'rotate': a[0][0]/10, 'fire' : 1, 'vision': 1}
                else:
                    res = {'rotate': a[0][0]/10, 'fire' : 1, 'vision': -1}
            else:
                if (input_dict['theta']<10):
                    res = {'rotate': -a[0][0]/10, 'fire' : 1, 'vision': 1}
                else:
                    res = {'rotate': -a[0][0]/10, 'fire' : 1, 'vision': -1}
        
        else:
            if velichina_povorota<0:
                if (input_dict['theta']<10):
                    res = {'rotate': a[0][0]/10, 'fire' : 1, 'vision': 1}
                else:
                    res = {'rotate': a[0][0]/10, 'fire' : 1, 'vision': -1}
            else:
                if (input_dict['theta']<10):
                    res = {'rotate': -a[0][0]/10, 'fire' : 1, 'vision': 1}
                else:
                    res = {'rotate': -a[0][0]/10, 'fire' : 1, 'vision': -1}
    
    return res