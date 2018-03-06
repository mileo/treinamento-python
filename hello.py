#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import dos módulos
import sys

nome = 'Ana'

	def repetir(texto):
	    print "funcao repetir"
	    return texto + texto

def main():
    print "funcao main"
    if len(sys.argv) < 2:
       print "Se verdade"
       print 'Ola mundo', nome
       print repetir(nome)
    else:
       print "Se Falso"
       print 'Ola mundo', sys.argv[1]
       print repetiasdsadasdr(sys.argv[1])

print "Primeiro programa"
print nome
print __name__


if __name__ == '__main__':
    main()

