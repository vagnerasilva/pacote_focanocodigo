# focanocodigo

**Calculadora** como próprio nome ja diz, é uma calculadora
capaz de somar, subtrair, multiplicar e dividir 2 valores em Python.

# Funções

* `calculadora.metodo(a, b)` - Recebe valor a e b e aplica aos métodos:
  - Somar
  - subtrair
  - dividir
  - multiplicar

* `help()` - Retorna um print de help da biblioteca.


### PUBLICACAO ### 

https://medium.com/@dev.daniel.amorim/como-criar-biblioteca-python-pypi-343219656838

https://stackoverflow.com/questions/46606692/cant-upload-to-pypi-with-twine


- # 00 Ativar venv
-  source ./venv/Scripts/activate
- # 1 build do pacote 
- python setup.py sdist
- # upload do pacote
- twine upload dist/*