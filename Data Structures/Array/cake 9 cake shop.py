# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:14:48 2020

@author: nandini.ananthan
"""

take_out_orders = [1, 5]
dine_in_orders = [2, 3, 6]
served_orders = [1, 2, 3, 5, 6, 8]

def is_f(take_out_orders, dine_in_orders,served_orders):
    tk_min = 0
    tk_max = len(take_out_orders) - 1
    dn_min = 0
    dn_max = len(dine_in_orders) - 1
    
    for order in served_orders:
        if tk_min <= tk_max and order == take_out_orders[tk_min]:
            tk_min += 1
        
        elif dn_min <= dn_max and order == dine_in_orders[dn_max]:
            dn_min += 1
        
    else:
        return False
    
    if tk_min != len(take_out_orders) or dn_min != len(dine_in_orders):
        return False
    return True    
    
print(is_f(take_out_orders, dine_in_orders, served_orders))
   