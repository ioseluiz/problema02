import numpy as np 

class Problema02():
    def __init__(self, luces,opcion, lab, cargas_ab,dist_ab,lbc,cargas_bc,dist_bc, lcd=0,cargas_cd=[],dist_cd=0):
        self.luces = luces
        self.opcion = opcion
        self.lab = lab # longitud LAB
        self.lbc = lbc # Longitud LBC
        self.lcd = lcd # Longitud LCD -- opcional si hay 3 luces
        self.cargas_ab = cargas_ab # Arreglo con diccionarios dentro
        self.cargas_bc = cargas_bc # Arreglo con diccionarios dentro
        self.cargas_cd = cargas_cd # Arreglo con diccionarios dentro si hay 3 luces
        self.dist_ab = dist_ab # Carga distribuida en AB
        self.dist_bc = dist_bc # Carga distribuida en BC
        self.dist_cd = dist_cd # Carga distribuida en CD


    def procedimiento_principal(self):
        print('Hola desde el procedimiento principal')
        if(self.luces == 2):
            solucion = self.usar_caso_2_luces()
        elif(self.luces == 3):
            solucion = self.usar_caso_3_luces()

        return solucion

        
    
    def usar_caso_2_luces(self):
        print('Caso 2 Luces')
        if (self.opcion == 'simplemente apoyada'):
            print('Opcion A')
            resultado = self.ejecutar_opcion_a_2claros()
        elif (self.opcion == 'esquina A empotrada'):
            print('Opcion B')
            resultado = self.ejecutar_opcion_b_2claros()
        elif (self.opcion == 'esquina C empotrada'):
            print('Opcion C')
            resultado = self.ejecutar_opcion_c_2claros()

        return resultado




    def usar_caso_3_luces(self):
        print('Caso 3 Luces')
        if (self.opcion == 'simplemente apoyada'):
            resultado = self.ejecutar_opcion_a_3claros()
        elif (self.opcion == 'esquina A empotrada'):
            resultado = self.ejecutar_opcion_b_3claros()
        elif (self.opcion == 'esquina C empotrada'):
            resultado = self.ejecutar_opcion_c_3claros()

        return resultado
        
##############################################################################
# 2 CLAROS
    def ejecutar_opcion_a_2claros(self):
        print('Opcion A')
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)

        valor_L1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R1 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_M = (-valor_L1 - valor_R1)/(2*(self.lab + self.lbc))
        #print('Valor M')
        #print(valor_M)

        resultado = {'M': str(round(valor_M,2))}

        print(resultado)

        return resultado


        
    def ejecutar_opcion_b_2claros(self):
        print('Opcion B')
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)

        valor_R1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_L2 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R2 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4

        # Solucion de Matrices

        valor_a = 2 * self.lab
        valor_b = self.lab
        valor_c = self.lab
        valor_d = 2 * (self.lab  + self.lbc)

        valor_e = -valor_R1
        valor_f = -valor_L2 - valor_R2
        matriz = self.armar_matriz(valor_a,valor_b,valor_c,valor_d)
        vector = self.armar_vector(valor_e, valor_f)

        inversa_matriz = np.linalg.inv(matriz)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz,vector)

        # Imprimir Resultado
        resultado = {'MA': str(round(vector_resultado[0][0],2)),
                     'MB': str(round(vector_resultado[1][0],2))}

        print(resultado)

        return resultado


    def ejecutar_opcion_c_2claros(self):
        print('Opcion C')
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)

        valor_L1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R1 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_L2 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4

        # Solucion de Matrices

        valor_a = 2 * (self.lab + self.lbc)
        valor_b = self.lbc
        valor_c = self.lbc
        valor_d = 2 * (self.lbc)

        valor_e = -valor_R1 -valor_L1
        valor_f = -valor_L2
        matriz = self.armar_matriz(valor_a,valor_b,valor_c,valor_d)
        vector = self.armar_vector(valor_e, valor_f)

        inversa_matriz = np.linalg.inv(matriz)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz,vector)

        # Imprimir Resultado
        resultado = {'MB': str(round(vector_resultado[0][0],2)),
                     'MC': str(round(vector_resultado[1][0],2))}

        print(resultado)

        return resultado


####################################################################################
# 3 CLAROS

    def ejecutar_opcion_a_3claros(self):
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)
        suma_cargas_cd = self.sumatoria_cargas_puntuales(self.cargas_cd)

        valor_L1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R1 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_L2 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_R2 = suma_cargas_cd+ (self.dist_cd*self.lcd**3)/4

        # Solucion de Matrices

        valor_a = 2 * (self.lab + self.lbc)
        valor_b = self.lbc
        valor_c = self.lbc
        valor_d = 2 * (self.lbc + self.lcd)

        valor_e = -valor_L1 - valor_R1
        valor_f = -valor_L2 - valor_R2
        matriz = self.armar_matriz(valor_a,valor_b,valor_c,valor_d)
        vector = self.armar_vector(valor_e, valor_f)

        inversa_matriz = np.linalg.inv(matriz)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz,vector)

        # Imprimir Resultado
        resultado = {'MB': str(round(vector_resultado[0][0],2)),
                     'MC': str(round(vector_resultado[1][0],2))}

        print(resultado)

        return resultado


    def ejecutar_opcion_b_3claros(self):
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)
        suma_cargas_cd = self.sumatoria_cargas_puntuales(self.cargas_cd)

        valor_R1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_L2 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R2 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_L3 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_R3 = suma_cargas_cd + (self.dist_cd*self.lcd**3)/4

        # Solucion de Matrices
        valor_a = 2 * (self.lab)
        valor_b = self.lab
        valor_c = 0
        valor_d = self.lab
        valor_e =2 * (self.lab + self.lbc)
        valor_f = self.lbc
        valor_g =0
        valor_h =self.lbc
        valor_i =2 * (self.lbc + self.lcd)

        valor_j = -valor_R1
        valor_k = -valor_L2 - valor_R2
        valor_l = -valor_L3 - valor_R3

        matriz = self.armar_matriz_2(valor_a, valor_b, valor_c, valor_d, valor_e, valor_f, valor_g, valor_h, valor_i)
        vector = self.armar_vector_2(valor_j, valor_k, valor_l)

        inversa_matriz = np.linalg.inv(matriz)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz,vector)

        # Imprimir Resultado
        resultado = {'MA': str(round(vector_resultado[0][0],2)),
                     'MB': str(round(vector_resultado[1][0],2)),
                     'MC': str(round(vector_resultado[2][0],2))}

        print(resultado)

        return resultado


    def ejecutar_opcion_c_3claros(self):
        #sumatoria de cargas puntuales
        suma_cargas_ab = self.sumatoria_cargas_puntuales(self.cargas_ab)
        suma_cargas_bc = self.sumatoria_cargas_puntuales(self.cargas_bc)
        suma_cargas_cd = self.sumatoria_cargas_puntuales(self.cargas_cd)

        valor_L1 = suma_cargas_ab + (self.dist_ab*self.lab**3)/4
        valor_R1 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_L2 = suma_cargas_bc + (self.dist_bc*self.lbc**3)/4
        valor_R2 = suma_cargas_cd + (self.dist_bc*self.lcd**3)/4
        valor_L3 = suma_cargas_cd + (self.dist_cd*self.lcd**3)/4

        # Solucion de Matrices
        valor_a = 2 * (self.lab + self.lbc)
        valor_b = self.lbc
        valor_c = 0
        valor_d = self.lbc
        valor_e =2 * (self.lbc + self.lcd)
        valor_f = self.lbc
        valor_g =0
        valor_h =self.lcd
        valor_i =2 * (self.lcd)

        valor_j = -valor_L1 - valor_R1
        valorl_k = -valor_L2 - valor_R2
        valor_l = -valor_L3 

        matriz = self.armar_matriz_2(valor_a, valor_b, valor_c, valor_d, valor_e, valor_f, valor_g, valor_h, valor_i)
        vector = self.armar_vector_2(valor_j, valor_k, valor_l)

        inversa_matriz = np.linalg.inv(matriz)

        # Calcular valores incognitas
        vector_resultado = np.dot(inversa_matriz,vector)

        # Imprimir Resultado
        resultado = {'MB': str(round(vector_resultado[0][0],2)),
                     'MC': str(round(vector_resultado[1][0],2)),
                     'MD': str(round(vector_resultado[2][0],2))}

        print(resultado)

        return resultado


#####################################################################################
# FUNCIONES DE OPERACIONES MATEMATICAS
    def sumatoria_cargas_puntuales(self,cargas):
        sumatoria = 0
        for carga in cargas:
            sumatoria += float(carga['carga'])
        return sumatoria

    def armar_matriz(self, a, b, c, d):
        matriz = [[a,b],[b,c]]
        return np.array(matriz)

    def armar_matriz_2(self,a,b,c,d,e,f,g,h,i):
        matriz = [[a,b,c],[d,e,f],[g,h,i]]
        return np.array(matriz)

    def armar_vector(self,e,f):
        vector = [[e],[f]]
        return np.array(vector)

    def armar_vector_2(self,j,k,l):
        vector = [[j],[k],[l]]
        return np.array(vector)

    

