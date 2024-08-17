
## COMANDOS PARA BUILD
- ### ATIVANDO VENV
      source venv/bin/activate

- ### EXECUTANDO EM PROD
      python manage.py runserver 0.0.0.0:8001 --settings=settings.prod-settings

- ### EXECUTANDO EM UAT
      python manage.py runserver 0.0.0.0:8001 --settings=settings.uat-settings

- ### EXECUTANDO EM DEV
      python manage.py runserver --settings=settings.dev-settings

- ### ACESSANDO APLICAÇÃO
      {{url-servidor}}:8001/admin/login/?next=/admin/

## COMANDOS AUXILIARES
- ### EXECUTANDO MIGRAÇÃO NO BANCO (ALTERA O BANCO)
      python manage.py makemigrations

- ### CRIANDO ARQUIVOS DE MIGRAÇÃO (VERIFICA O QUE EXISTE NO BANCO)
      python manage.py migrate

- ### CRIANDO SUPER ADMIN
      python manage.py createsuperuser

- ### CRIANDO PASTA DE ARQUIVOS ESTATICOS
      python manage.py collectstatic

