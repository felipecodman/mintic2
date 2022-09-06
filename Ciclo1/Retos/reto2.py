def cliente (informacion:dict) -> dict:
  
  cliente = informacion['id_cliente']
  name = informacion['nombre']
  años = informacion['edad']
  ingreso = informacion['primer_ingreso']

  if años > 18 :
    atraccion = 'X-Treme'
    apto = True
    if ingreso == True:
      total_boleta = 20000-(20000*0.05)
    else:
      total_boleta = 20000
  elif años >= 15 and años <=18:
    atraccion = 'Carros chocones'
    apto = True
    if ingreso == True:
      total_boleta = 5000-(5000*0.07)
    else:
      total_boleta = 5000
  elif años >=7 and años <15:
    atraccion = 'Sillas voladoras'
    apto = True
    if ingreso  == True:
      total_boleta= 10000 - (10000*0.05)
    else:
      total_boleta = 10000
  else:
    atraccion = 'N/A'
    apto = False
    total_boleta ='N/A'
  diccionario_rta ={
    'nombre': name,
    'edad': años,
    'atraccion': atraccion,
    'apto': apto,
    'primer_ingreso': ingreso,
    'total_boleta': total_boleta
  }
  return diccionario_rta


