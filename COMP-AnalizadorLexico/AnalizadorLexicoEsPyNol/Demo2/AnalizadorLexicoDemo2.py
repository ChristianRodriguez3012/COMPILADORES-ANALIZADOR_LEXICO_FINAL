# Importar el módulo ply.lex para crear un analizador léxico
import ply.lex as lex
# Importar el módulo 'os' para acceder a funcionalidades relacionadas con el sistema operativo.
import os

# Definir los tokens que el analizador léxico reconocerá
tokens = (
    'NUMERO_ENTERO',     
    'NUMERO_DECIMAL',    
    'LITERAL_FLOTANTE',
    'LITERAL_COMPLEJO',
    'LITERAL_CADENA_TEXTO',
    'LITERAL_BOOLEANO',
    'OPERADOR_LOGICO',
    'OPERADOR_COMPARACION',
    'OPERADOR_ASIGNACION',
    'OPERADOR_ARITMETICO',
    'OPERADOR_BIT_A_BIT',
    'OPERADOR_DESPLIEGO',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'COMA',
    'PUNTO_Y_COMA',
    'DOS_PUNTOS',
    'ID',
    'COMENTARIO',
    'IMPRIMIR',
    'SI',
    'SINO_SI',
    'SINO',
    'PARA',
    'MIENTRAS',
    'PROBAR',
    'EXCEPTO',
    'FINALMENTE',
    'DEFINIR',  # Reemplazado 'def' por 'definir'
    'CLASE',
    'RETORNAR',
    'IMPORTAR',
    'COMO',
    'DESDE',
    'GLOBAL',
    'LAMBDA',
)

# Definir un diccionario de palabras reservadas y sus correspondientes tokens
reservadas = {
    'entero': 'NUMERO',
    'decimal': 'LITERAL_FLOTANTE',
    'complejo': 'LITERAL_COMPLEJO',
    'cadena': 'LITERAL_CADENA_TEXTO',
    'booleano': 'LITERAL_BOOLEANO',
    'y': 'OPERADOR_LOGICO',
    'o': 'OPERADOR_LOGICO',
    'igual': 'OPERADOR_COMPARACION',
    'diferente': 'OPERADOR_COMPARACION',
    'menor': 'OPERADOR_COMPARACION',
    'mayor': 'OPERADOR_COMPARACION',
    'menor_igual': 'OPERADOR_COMPARACION',
    'mayor_igual': 'OPERADOR_COMPARACION',
    'asignar': 'OPERADOR_ASIGNACION',
    'suma': 'OPERADOR_ARITMETICO',
    'resta': 'OPERADOR_ARITMETICO',
    'multiplicar': 'OPERADOR_ARITMETICO',
    'dividir': 'OPERADOR_ARITMETICO',
    'modulo': 'OPERADOR_ARITMETICO',
    'potencia': 'OPERADOR_ARITMETICO',
    'bitwise_and': 'OPERADOR_BIT_A_BIT',
    'bitwise_or': 'OPERADOR_BIT_A_BIT',
    'bitwise_xor': 'OPERADOR_BIT_A_BIT',
    'desplazar_izq': 'OPERADOR_DESPLIEGO',
    'desplazar_der': 'OPERADOR_DESPLIEGO',
    'si': 'SI',
    'sino_si': 'SINO_SI',
    'sino': 'SINO',
    'para': 'PARA',
    'mientras': 'MIENTRAS',
    'probar': 'PROBAR',
    'excepto': 'EXCEPTO',
    'finalmente': 'FINALMENTE',
    'definir': 'DEFINIR',  # Reemplazado 'def' por 'definir'
    'clase': 'CLASE',
    'retornar': 'RETORNAR',
    'importar': 'IMPORTAR',
    'como': 'COMO',
    'desde': 'DESDE',
    'global': 'GLOBAL',
    'lambda': 'LAMBDA',
    'imprimir': 'IMPRIMIR',
    'Verdad': 'LITERAL_BOOLEANO',
    'Falso': 'LITERAL_BOOLEANO',
}


# Definir una función para reconocer identificadores (tokens ID)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

# Definir funciones para reconocer diferentes tipos de literales
def t_LITERAL_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_LITERAL_COMPLEJO(t):
    r'\d+\.\d+j'
    t.value = complex(t.value)
    return t

def t_LITERAL_CADENA_TEXTO(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1]
    return t

def t_NUMERO_ENTERO(t):
    r'-?\d+'
    t.value = int(t.value)
    t.type = 'NUMERO_ENTERO'
    return t

def t_NUMERO_DECIMAL(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    t.type = 'NUMERO_DECIMAL'
    return t

def t_OPERADOR_LOGICO(t):
    r'y|o'
    return t

def t_OPERADOR_COMPARACION(t):
    r'==|!=|<|>|<=|>='
    return t

def t_OPERADOR_ASIGNACION(t):
    r'='
    return t

def t_OPERADOR_ARITMETICO(t):
    r'\+|-|\*|/|%|\*\*'
    return t

def t_OPERADOR_BIT_A_BIT(t):
    r'&|\||\^|~|>>|<<'
    return t

def t_OPERADOR_DESPLIEGO(t):
    r'>>|<<'
    return t

def t_PUNTO_Y_COMA(t):
    r';'
    return t

def t_COMA(t):
    r','
    return t

def t_DOS_PUNTOS(t):
    r':'
    return t

def t_PARENTESIS_IZQ(t):
    r'\('
    return t

def t_PARENTESIS_DER(t):
    r'\)'
    return t

def t_LLAVE_IZQ(t):
    r'\{'
    return t

def t_LLAVE_DER(t):
    r'\}'
    return t

def t_COMENTARIO(t):
    r'\#.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_IMPRIMIR(t):
    r'imprimir'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

# MAIN ----------------------------------------------------------------

def main():
    # Obtener el directorio actual del script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Nombre de la carpeta a buscar
    carpeta_a_buscar = 'ejercicios'

    # Construir la ruta completa a la carpeta
    carpeta_path = os.path.join(script_dir, carpeta_a_buscar)

    try:
        # Listar los archivos en la carpeta
        archivos_en_carpeta = os.listdir(carpeta_path)

        # Buscar el archivo 'archivo1.txt' dentro de la carpeta
        if 'ejercicio6.txt' in archivos_en_carpeta:
            # Construir la ruta completa al archivo 'archivo1.txt'
            archivo_path = os.path.join(carpeta_path, 'ejercicio6.txt')

            # Abrir el archivo en modo lectura
            with open(archivo_path, 'r') as file:
                text = file.read()

            lexer.input(text)

            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(tok.type, tok.value)
        else:
            print(f"El archivo no se encontró en la carpeta: {carpeta_path}")
    except FileNotFoundError:
        print(f"La carpeta '{carpeta_a_buscar}' no se encontró en el directorio: {script_dir}")

if __name__ == "__main__":
    main()

