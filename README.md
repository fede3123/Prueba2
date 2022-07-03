
# Prueba técnica punto 2
 
La empresa Stratton Oakmont necesita una nueva arquitectura para su backend ya que el framework está dando problemas. 
 
## Objetivos 
 - Búsqueda e implementación de una nueva arquitectura para el micro servicio
 - Optimizar la respuesta de los endpoints
 
## arquitectura
<img src="C:\Users\feder\Desktop\fastApitest\arquitectura.jpeg" alt="My cool logo"/>
 
### Porqué se escogió este framework
 
A comparación de otros frameworks como lo pueden ser flask django o node, fastapi es mucho más veloz en su tiempo de respuesta y desarrollo ya que no esta hecho para la respuesta rapida aplicando asincronia en sus procesos, en este caso se elige fastapi además de por la velocidad la poca complejidad para integrarlo con otras herramientas. 
 
Este proyecto se basa en un micro servicio haciendo que la robustez de django sea contraproducente y al tener un millon de datos para mostrar se deja de lado a flask ya que a pesar de ser más efectivo para microservicios decae mucho cuando las petición son demasiado complejas, dentro de la arquitectura se baraja la idea de usar node pero en caso de querer aplicar técnicas de ciencia de datos es mucho mejor usar python que javaScript.
 
### Ventajas de fastapi 
- Proceso asíncrono para la mejora de respuesta de los endpoints 
- Sencillo de desarrollar y llevar a deployment
- Cuenta con integración para jinja templates y otras herramientas 
 
## API endpoints
 
#### Obtener los datos
 
```http
  GET /api/request/${page_num}&${page_size}
```
 
| Parámetros  | Tipo      | Descripción                                   |
|:------------|:----------|:----------------------------------------------|
| `page_size` | `integer` | **Obligatorio** define la cantidad de objetos |
| `page_num`  | `integer` | **Obligatorio** define que pagina quiere      |
 
#### Buscar un id especifico
 
```http
  GET /api/find/${id}
```
 
| Parámetros | Tipo      | Descripción                                    |
|:-----------|:----------|:-----------------------------------------------|
| `id`       | `integer` | **Obligatorio** Define que id se quiere buscar |
 
