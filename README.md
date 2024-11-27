Introducción al CTF: "Desafíos de Seguridad Web"
¡Bienvenidos al Capture The Flag (CTF) "Desafíos de Seguridad Web"! Este CTF ha sido diseñado para poner a prueba tus habilidades en ciberseguridad web mediante la exploración de vulnerabilidades reales que afectan a aplicaciones web. Utilizarás técnicas de pentesting ético para descubrir y explotar fallos de seguridad, con el objetivo de capturar las banderas ocultas en cada uno de los retos.

Objetivo del CTF
Identificar las vulnerabilidades en cada desafío, explotarlas de manera controlada y recuperar las banderas (FLAG{}) ocultas. Cada bandera representa la solución a un reto específico. Los retos están diseñados para simular escenarios reales que podrías encontrar en auditorías de seguridad web.

Características del CTF
Tecnología empleada:

Aplicación desarrollada con Flask.
Contenedores Docker para un entorno controlado.
Base de datos SQLite para la autenticación y almacenamiento de datos.
Retos y Temas abordados: Este CTF incluye siete retos, cada uno enfocado en una vulnerabilidad específica que es común en aplicaciones web:

SQL Injection: Explora la inyección de código SQL para acceder a datos no autorizados.
Cross-Site Scripting (XSS): Descubre cómo insertar código malicioso en una aplicación web.
Cross-Site Request Forgery (CSRF): Simula cómo un atacante puede realizar acciones maliciosas en nombre de un usuario legítimo.
Local File Inclusion (LFI): Explota la inclusión de archivos locales para obtener acceso a información sensible.
Broken Authentication: Encuentra fallos en la autenticación y accede a recursos restringidos.
Insecure Direct Object References (IDOR): Accede a datos de otros usuarios manipulando identificadores.
Misconfiguraciones de Seguridad: Identifica configuraciones débiles que pueden ser explotadas.
Entorno controlado: Todo el entorno del CTF está contenido dentro de Docker, garantizando un espacio seguro para que puedas probar tus habilidades sin riesgos para tu sistema.

Reglas del CTF
Ética: Este CTF es un ejercicio de aprendizaje. No uses las técnicas aprendidas aquí para actividades maliciosas o ilegales fuera de este entorno.
Entorno: No realices pruebas fuera del entorno configurado en Docker.
Colaboración: Aunque se permite el trabajo en equipo, evita compartir las soluciones directamente. Ayuda a tus compañeros guiándolos sin revelar las banderas.
Reportes: Si encuentras errores inesperados en los retos, repórtalos a los organizadores.

Requisitos para Participar

Tener conocimientos básicos en:
Análisis de vulnerabilidades web.
Uso de herramientas como Burp Suite, OWASP ZAP, o navegadores con extensiones para pruebas de seguridad.
Entender conceptos de vulnerabilidades como las listadas en OWASP Top 10.
Contar con Docker instalado en tu máquina local para desplegar el entorno.

Cómo Iniciar el CTF
Configuración del entorno:

Descarga los archivos del CTF desde el repositorio proporcionado.

Construye el contenedor Docker usando el comando:
docker build -t web-ctf .
Ejecuta el contenedor:
docker run -p 5000:5000 web-ctf
Accede a la aplicación web a través de tu navegador en http://localhost:5000.

Estrategia:

Inspecciona las páginas y funcionalidades disponibles.
Identifica posibles puntos de entrada para explotar vulnerabilidades.
Usa herramientas y tus conocimientos para capturar cada bandera.

Puntos por Reto
Cada reto tiene un nivel de dificultad asignado y otorga puntos según la complejidad. Los retos más difíciles otorgan mayores recompensas. La tabla de puntos es la siguiente:

Reto	Puntos
SQL Injection	100
Cross-Site Scripting (XSS)	150
Cross-Site Request Forgery	200
Local File Inclusion (LFI)	250
Broken Authentication	200
Insecure Direct Object Reference	150
Misconfiguración de Seguridad	100
