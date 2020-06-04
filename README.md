# Cornerapp

Prueba técnica para postulación a backend developer en Cornershop. Todo el desarrollo está realizado en base a apis, no cuenta con frontend. Se provee un proyecto de postman para facilitar las pruebas.

## **Tecnologías**:

- Python 3.8
- Mysql 5.7
- Celery
- Redis

## Conceptos

- Users
    - Admin: Usuario base, permite crear a los otros.
    - Chef: Encargado de los menús (este es el perfil de nora!).
    - Employee: Elige el menú que desea consumir.
- Menu:
    - Options: Listado de opciones para comer.
    - Choose: Elección de una opcion por parte del empleado.

## Técnicas y princípios aplicados

Se aplica principios de [12factor.net](https://12factor.net/):

- No se versionan parametros dependientes del ambiente.
- Manejo de dependencias para desarrollo y producción con pipenv.

Se aplican principios **SOLID** (se explican los principales aplicados):

- Se aplica en gran medida el principio "S**ingle responsibility principle"** pensando en un contexto donde la mantención de la aplicación es primordial. Por ello se dividen las vistas en archivos con una responsabilidad especifica y se evita el uso de recursos como ViewSets.
- Por la misma razón del punto anterior se respeta **OCP** evitando el uso de ViewSets. De esta forma si un caso de uso requiere ser modificado o extendido evitamos trastocar el resto de casos al no estar acoplados.
- Se aplica **DIP** (dentro de las posibilidades). Ejemplo de este principio es el notificador de slack, para este caso se intenta definir una interfaz con el modulo **abc** mediante una clase abstracta pensando en crear un contrato que permita la implementaciones de distintos notificadores (Slack, Twitter, Email, etc.) con la menor interferencia posible en el codigo.

## Deploy

- Debes tener instalado pipenv.
- Crear archivo .env utilizado como base el archivo .env.example:
    - Configura el nombre y url de la aplicación.
    - Ingresar key de aplicación.
    - Crear base de datos mysql y configurar credenciales.
    - Levantar servidor redis y configurar urls.
    - Crear una aplicación de Slack ([https://cornerappespacio.slack.com/apps/A0F7YS25R-bots?next_id=0](https://cornerappespacio.slack.com/apps/A0F7YS25R-bots?next_id=0)) y configurar token de api en enviroments. Ademas debes seleccionar el canal (previamente creado) al cual se enviaran los mensajes. Puedes leer mas al final.
- Instala las dependencias de la aplicación con **pipenv install —dev**
- Ejecuta las migraciónes con **pipenv run python [manage.py](http://manage.py) migrate.** Te recomiendo remplazar este paso por el dump que se encuentra en la raiz, contiene usuarios con todos los roles precargados.
- Ejecutar los test y verifica que todo funcione: **pipenv run python [manage.py](http://manage.py) test**
- Por ultimo ejecuta **pipenv run celery -A app worker -l info** y  **pipenv run celery -A app beat -l info** para correr el scheduler.

## Arquitectura

Se opta por una arquitectura lo mas acoplada al fraemwork posible por velocidad de desarrollo.

- La carpeta app contiene la configuración central del fraemwork.
- La carpeta cornerapps las aplicaciones de django.
- El modulo shared comparte codigo base para toda la aplicación. Tambien es una convención usada dentro de los modulos por lo que tambien se puede ver en carpetas de aplicaciones.

```
├── app
├── cornerapps
├── manage.py
├── shared
├── Pipfile
├── Pipfile.lock
└── tree.txt
```

Dentro de cada aplicación se agrupa el codigo por carpetas que hacen referencia a la herramienta del fraemwork utilizada por lo que no hay mucho que explicar sobre esto, es bastante intuitivo. 

Lo que sí cabe destacar son las carpetas interfaces e implementations. La carpeta interfaces contiene los contratos y la carpeta implementations corresponde (valga la redundancia) a la implementación concreta. En el caso de la app menu posee la implementación de slack_notifier.py.

```
├── __init__.py
├── apps.py
├── implementations
├── interfaces
├── migrations
├── models
├── serializers
├── tasks.py
├── tests
├── tree.txt
├── urls.py
└── views
```

## Dumps

Si cargas el [dump de la base de datos](https://github.com/esteban03/Backend-Test-Sanchez/blob/master/dump/dump.sql) debes saber que cuenta con los usuarios base precargados para que puedas probar:

**Admin**

```
User: admin
pass: admin_example
```

**Cheff**

```
User: example_chef
Pass: example_chef
```

**Employee**

```
User: example_employee
Pass: example_employee
```


## Postman

Se facilita un [proyecto de postman](https://github.com/esteban03/Backend-Test-Sanchez/blob/master/dump/rest.postman_collection.json) con las apis configuradas para ser testeadas y a modo de documentación.
