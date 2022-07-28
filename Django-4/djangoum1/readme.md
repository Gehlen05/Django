# **Ambiente de Desenvolvimento**


# Principais Informações do Projeto
- Curso: Django Framework
- Escola: Geek University
- Link: <a href="https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/"> Django Framework</a>
- Programador:
    - Alexsandro Gehlen
   

- Descrição:
    - Projeto para utilização de usuarios e models.



## Execução
```
- python manage.py runserver
```

# Ambiente de Desenvolvimento

## Requisitos
- Python 3.6
- VirtualEnv
- requirements.txt

# Execução
Efetuar o download do projeto:
```
git clone git@github.com:Gehlen05/Django.git
```
Criar venv
```
cd django3
virtualenv .venv
```
Ativar venv
```
source .venv/bin/activate
```
Instalar requirements
```
pip install -r requirements.txt
```
Executar projeto na maquina local
```
- python manage.py runserver
```

Executar testes(necessário instalar coverage)
```

- coverage run manage.py test
- coverage html

```
