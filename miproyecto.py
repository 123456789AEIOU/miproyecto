
 start = print ("estas en la selva y estas desidratado y tienes tres opciones beber: agua de rio o agua de cactus ")
 opcion_1 = input ("cual escojes : rio, cactus ").lower()
 if opcion_1 == "rio":
  print ("al beber el agua del rio notas que esta contaminada ")
 opcion_1_1 = input (" \n que haces bomitas el agua  o buscas una planta curativa \n :").lower()
 if opcion_1_1 == "corres":
   print ("bomitas el agua y te salvas")
   print ("al hacerlo vez una mata de manzana en el otro extremo de selva que haras")
 otra = input(" \n ir alla, quedarte de este lado de la selva :  ").lower()
 if otra == "ir alla": 
  print("al llegar al otro lado de la selva y comes de la mata de manzanas, pero sientes que deberias regresar al otro lado ganstes")
 elif otra == "quedarte en este lado de la selva":
  print("al quedarte de este lado y reflexionas sobre la vida en la selva y aprendes a sobrevivir, has ganado")
 else: print ("no hagas eso has perdido")
 elif opcion_1_1 == "esconderse":
 print ("te escondes pero en horas te puedes desidratar, fin del juego")
 else: ("no te escondas, has perdido")

 if opcion_1 =="cactus":
 print("\n al beber el agua del cactus notas dos caminos uno te lleva a un oasis en la selva y el otro te lleva a la ciudad : \n")
  opcion_1_2 = input ("cual tomas el de el oasis o la ciudad ?:" ).lower()
 if opcion_1_2 =="oasis":
  print("al ir al oasis te topas con un tigre que haces")
  otra_2 =input ("\n consigues un arma o sales corriendo: \n").lower()
 if otra_2 =="consigues un arma ":
  print("consigues un tronco afilado y logras ahuyentar al tigre.")
 elif otra_2 == "sales corriendo":
 print("al salir corriendo logras safarte del tigre y quedas a salvo")
 else: 
 print("ahora has perdido por no responder correctamente")
 else: 
 print("\n no elegistes ninguna opcion perdistes \n")








          
