from django.shortcuts import render, HttpResponse

# Create your views here.
layaut="""
<h1> Sitio web con Esteban Ferreiro</h1>
<hr>
<ul>
<li> 
<a href="/inicio">Inicio</a>
</li>
<li> 
<a href="/hola-mundo">Hola Mundo</a>
</li>
<li> 
<a href="/pagina-pruebas">pagina de pruebas</a>
</li>
</ul>
"""
def index(request):
    return HttpResponse("""
     <h1> Inicio</h1>
     """)
def hola_mundo(request):
    return HttpResponse ("""
    <h1>Hola mundo con Django!!"</h1>
    <h3> Soy Esteban Ferreiro web</h3>
    """)
def pagina(request):
        return HttpResponse ("""
        <h1> pagina de mi web</1>
        <p>Creada por Esteban Ferreiro</p>
        """)
   