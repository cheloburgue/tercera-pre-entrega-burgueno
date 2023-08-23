# tercera-pre-entrega-burgueno
Description:

EL PROGRAMA MUESTRA UNA PAGINA DE INSTRUMENTOS MUSICALES, DONDE NOS PERMITE CARGAR INSTRUMENTOS, PRECIOS DE LOS MISMOS y LOCALES DE VENTA. 
TAMBIEN NOS DA LA OPCION DE BUSCAR TODOS LOS INSTRUMENTOS DISPONIBLES SEGUN LA MARCA.

------------------------------------------------------------------------------------------------------------------------------------------------------

1 - Clonar el repositorio de GitHub localmente mediante el comando:
      -> git clone https://github.com/cheloburgue/tercera-pre-entrega-burgueno
      
------------------------------------------------------------------------------------------------------------------------------------------------------
      
2 - Abrimos Visual Studio code y en la consolta en caso de no tenerlo instalado corremos el siguiente comando para instalar Django(en caso de ya tenerlo omitir el paso 2)
      -> pip install django
      
------------------------------------------------------------------------------------------------------------------------------------------------------

3 - Una vez instalado nos paramos sobre la carpeta raiz del proyecto importado '../tercera-pre-entrega-burgueno>' y ejecutamos el siguiente comando:
      -> python manage.py runserver
      
    Este comando levantara un servidor local para poder visualizar la pagina correctamente
------------------------------------------------------------------------------------------------------------------------------------------------------

4 - Una vez levantado el servidor deberemos ingresar a la siguiente ruta local (Vease en la consola el IP del servidor que acabamos de levantar) 
      
       http://127.0.0.1:8000/AppCoder/   (Agregarle el tag a la url  /AppCoder/ para poder visualizar correctamente la pagina web.

------------------------------------------------------------------------------------------------------------------------------------------------------

5 - Ya tenemos acceso a la Web! La misma cuanta con 5 secciones.

- boton Music Center  -> redirige a la pagina de inicio
- boton Instrumento -> Permite cargar instrumentos en mi base de datos atraves de un formulario ingresando tipo, marca y codigo de instrumento
- boton Precios -> Permite cargar precios en mi base de datos segun por codigo de instrumento
- boton Locales -> Permite agregar locales ingresando la direccion y localidad de los mismos
- boton buscar instrumento -> Busca todos los instrumentos que existan filtrando la busqueda por marca.

--------------------------------------------------------------------------------------------------------------------------------------------------

6 - Para poder validar las cargas a la base de datos se puede ingresar al Backoffice de administrador en el siguiente enlace:
      http://127.0.0.1:8000/admin

      usuario : admin
      pass: admin
