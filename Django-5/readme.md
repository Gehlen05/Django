# **Ambiente de Desenvolvimento**


# Principais Informações do Projeto
- Curso: Django Framework
- Escola: Geek University
- Link: <a href="https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/"> Django Framework</a>
- Programador:
    - Alexsandro Gehlen
   

- Descrição:
    - Projeto para relacionamento de models.
    - Necessario criar um super usuario.
    - Acessar a area admin para poder observar oque foi feito.



## Execução
```
- python manage.py runserver
- http://127.0.0.1:8000/admin/
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
