import ply.lex as lex

tokens = (
    'NUMERO',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIR',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'COMENTARIO',
    'ID',
    'IF',
    'ELSE',
    'ELIF',
    'FOR',
    'WHILE',
    'TRY',
    'EXCEPT',
    'FINALLY',
    'DEF',
    'CLASS',
    'RETURN',
    'IMPORT',
    'AS',
    'FROM',
    'GLOBAL',
    'LAMBDA',
    'LITERAL_NUMERICO',
    'LITERAL_FLOTANTE',
    'LITERAL_COMPLEJO',
    'LITERAL_CADENA_TEXTO_COMILLAS_DOBLES',
    'LITERAL_CADENA_TEXTO_COMILLAS_SIMPLES',
    'LITERAL_BOOLEANO_VERDADERO',
    'LITERAL_BOOLEANO_FALSO',
    'OPERADOR_LOGICO',
    'OPERADOR_COMPARACION',
    'FIN_DE_LINEA',
    'ESPACIO_EN_BLANCO',
    'OPERADOR_ASIGNACION',
    'OPERADOR_AUMENTO',
    'OPERADOR_DISMINUCION',
    'OPERADOR_MULTIPLICACION',
    'OPERADOR_DIVISION',
    'OPERADOR_MODULO',
    'OPERADOR_POTENCIA',
    'OPERADOR_SUMA',
    'OPERADOR_RESTA',
    'OPERADOR_IGUALDAD',
    'OPERADOR_DESIGUALDAD',
    'OPERADOR_MENOR_QUE',
    'OPERADOR_MAYOR_QUE',
    'OPERADOR_MENOR_O_IGUAL_QUE',
    'OPERADOR_MAYOR_O_IGUAL_QUE',
    'OPERADOR_NEGACION',
    'OPERADOR_COMPLEMENTO_A_1',
    'OPERADOR_BIT_A_BIT_AND',
    'OPERADOR_BIT_A_BIT_OR',
    'OPERADOR_BIT_A_BIT_XOR',
    'OPERADOR_DESPLIEGO_A_LA_IZQUIERDA',
    'OPERADOR_DESPLIEGO_A_LA_DERECHA',
    'OPERADOR_IDENTIDAD',
    'OPERADOR_PERTENENCIA',
    'OPERADOR_IDENTIDAD_DE_TIPO',
)

reservadas = {
    'int': 'TYPE_INT',
    'bool': 'TYPE_BOOL',
    'si': 'SI',
    'sinosi': 'SINO_SI',
    'sino': 'SINO',
    'para': 'PARA',
    'mientras': 'MIENTRAS',
    'probar': 'PROBAR',
    'excepto': 'EXCEPTO',
    'finalmente': 'FINALMENTE',
    'definir': 'DEFINIR',
    'clase': 'CLASE',
    'retornar': 'RETORNAR',
    'importar': 'IMPORTAR',
    'como': 'COMO',
    'desde': 'DESDE',
    'global': 'GLOBAL',
    'lambda': 'LAMBDA',
}

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    t.type = 'NUMERO'
    return t

def t_ID(t):
    r'[a-z][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

def t_IF(t):
    r'si'
    t.type = 'IF'
    return t

def t_ELSE(t):
    r'sino'
    t.type = 'ELSE'
    return t

def t_ELIF(t):
    r'sinosi'
    t.type = 'ELIF'
    return t

def t_FOR(t):
    r'para'
    t.type = 'PARA'
    return t

def t_WHILE(t):
    r'mientras'
    t.type = 'MIENTRAS'
    return t

def t_TRY(t):
    r'probar'
    t.type = 'PROBAR'
    return t

def t_EXCEPT(t):
    r'excepto'
    t.type = 'EXCEPTO'
    return t

def t_FINALLY(t):
    r'finalmente'
    t.type = 'FINALMENTE'
    return t

def t_DEF(t):
    r'definir'
    t.type = 'DEF'
    return t

def t_CLASS(t):
    r'clase'
    t.type = 'CLASE'
    return t

def t_RETURN(t):
    r'retornar'
    t.type = 'RETORNAR'
    return t

def t_IMPORT(t):
    r'importar'
    t.type = 'IMPORTAR'
    return t

def t_AS(t):
    r'como'
    t.type = 'COMO'
    return t

def t_FROM(t):
    r'desde'
    t.type = 'DESDE'
    return t

def t_GLOBAL(t):
    r'global'
    t.type = 'GLOBAL'
    return t

def t_LAMBDA(t):
    r'lambda'
    t.type = 'LAMBDA'
    return t

def t_LITERAL_NUMERICO(t):
    r'\d+'
    t.value = int(t.value)
    t.type = 'LITERAL_NUMERICO'
    return t

def t_LITERAL_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    t.type = 'LITERAL_FLOTANTE'
    return t

def t_LITERAL_COMPLEJO(t):
    r'\d+\.\d+j'
    t.value = complex(t.value)
    t.type = 'LITERAL_COMPLEJO'
    return t

def t_LITERAL_CADENA_TEXTO_COMILLAS_DOBLES(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    t.type = 'LITERAL_CADENA_TEXTO_COMILLAS_DOBLES'
    return t

def t_LITERAL_CADENA_TEXTO_COMILLAS_SIMPLES(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    t.type = 'LITERAL_CADENA_TEXTO_COMILLAS_SIMPLES'
    return t

def t_LITERAL_BOOLEANO_VERDADERO(t):
    r'Verdad'
    t.value = True
    t.type = 'LITERAL_BOOLEANO_VERDADERO'
    return t

def t_LITERAL_BOOLEANO_FALSO(t):
    r'Falso'
    t.value = False
    t.type = 'LITERAL_BOOLEANO_FALSO'
    return t

def t_OPERADOR_LOGICO(t):
    r'y|o'
    t.type = t.value
    return t

def t_OPERADOR_COMPARACION(t):
    r'==|!=|<|>|<=|>='
    t.type = t.value
    return t

def t_COMENTARIO(t):
    r'\#.*'
    t.lexer.lineno += t.value.count('\n')
    t.type = 'COMENTARIO'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    t.type = 'FIN_DE_LINEA'
    return t

def t_ESPACIO_EN_BLANCO(t):
    r'\s+'
    pass

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    lexer = lex.lex()

    text = "print('Hola, mundo!')"

    lexer.input(text)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok.type, tok.value)

if __name__ == "__main__":
    main()
