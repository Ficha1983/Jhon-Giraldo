from rich.table import Table
from rich.panel import Panel
    
console = Console()

def run(db):
    """Módulo de conceptos básicos de MongoDB"""
console.print(Panel.fit("📌 [bold cyan]Conceptos Básicos de MongoDB[/bold cyan] 📌"))

while True:
# Mostrar submenú

    table = Table(title="Operaciones Básicas", show_header=True)
    table.add_column("Opción", style="cyan")
    table.add_column("Comando", style="green")
    table.add_column("Descripción", style="white")
    table.add_row("1", "db.help()", "Mostrar ayuda de comandos de base de datos")
    table.add_row("2", "db.stats()", "Mostrar estadísticas de la BD")
    table.add_row("3", "show dbs", "Listar todas las bases de datos")
    table.add_row("4", "use <db>", "Cambiar a una base de datos")
    table.add_row("5", "db.dropDatabase()", "Eliminar la base de datos actual")
    table.add_row("6", "db.createCollection()", "Crear una nueva colección")
    table.add_row("7", "show collections", "Listar colecciones en la BD actual")
    table.add_row("8", "db.<col>.drop()", "Eliminar una colección")
    table.add_row("0", "Volver","Regresar al menú principal")
    console.print(table)
    choice = console.input("\n🔹Seleccione una operación para ejecutar (0-8): ")
    if choice == "0":
        break
    elif choice == "1":
        console.print("\n[bold]Ejemplo de db.help():[/bold]")
        console.print("""
Este comando muestra todos los métodos disponibles para manipular la base de datos.
[yellow]Uso:[/yellow]
> db.help()
[yellow]Salida típica:[/yellow]
DB methods:
db.adminCommand(nameOrDocument) - switches to 'admin' db
db.aggregate([pipeline], {options}) - performs aggregation
db.createCollection(name, options) - creates new collection
... (más métodos)
""")
    elif choice == "2":
        console.print("\n[bold]Ejemplo de db.stats():[/bold]")
        stats = db.command("dbstats")
        from rich.table import Table
from rich.panel import Panel
console = Console()
def run(db):
    """Módulo de conceptos básicos de MongoDB"""
console.print(Panel.fit("📌 [bold cyan]Conceptos Básicos de MongoDB[/bold cyan] 📌"))
while True:
# Mostrar submenú
    table = Table(title="Operaciones Básicas", show_header=True)
    table.add_column("Opción", style="cyan")
    table.add_column("Comando", style="green")
    table.add_column("Descripción", style="white")
    table.add_row("1", "db.help()", "Mostrar ayuda de comandos de base de datos")
    table.add_row("2", "db.stats()", "Mostrar estadísticas de la BD")
    table.add_row("3", "show dbs", "Listar todas las bases de datos")
    table.add_row("4", "use <db>", "Cambiar a una base de datos")
    table.add_row("5", "db.dropDatabase()", "Eliminar la base de datos actual")
    table.add_row("6", "db.createCollection()", "Crear una nueva colección")
    table.add_row("7", "show collections", "Listar colecciones en la BD actual")
    table.add_row("8", "db.<col>.drop()", "Eliminar una colección")
    table.add_row("0", "Volver","Regresar al menú principal")
    console.print(table)
    choice = console.input("\n🔹Seleccione una operación para ejecutar (0-8): ")
    if choice == "0":
        break
    elif choice == "1":
        console.print("\n[bold]Ejemplo de db.help():[/bold]")
        console.print("""
Este comando muestra todos los métodos disponibles para manipular la base de datos.
[yellow]Uso:[/yellow]
> db.help()
[yellow]Salida típica:[/yellow]
DB methods:
db.adminCommand(nameOrDocument) - switches to 'admin' db
db.aggregate([pipeline], {options}) - performs aggregation
db.createCollection(name, options) - creates new collection
... (más métodos)
""")
    elif choice == "2":
        console.print("\n[bold]Ejemplo de db.stats():[/bold]")
        stats = db.command("dbstats")