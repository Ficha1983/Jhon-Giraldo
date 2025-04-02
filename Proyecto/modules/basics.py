# Importación de módulos necesarios
from rich.console import Console  # Módulo para mejorar la presentación en consola
from rich.table import Table  # Módulo para crear tablas en consola
from rich.panel import Panel  # Módulo para crear paneles decorativos

# Creación de una instancia de Console para la interfaz
console = Console()

def run(db):
    """
    Módulo de conceptos básicos de MongoDB
    Args:
    db: Instancia de base de datos MongoDB
    Este módulo permite:
    - Explorar comandos básicos de MongoDB
    - Ver estadísticas de la base de datos
    - Gestionar bases de datos y colecciones
    - Aprender operaciones fundamentales
    """
    console.print(Panel.fit("📌[bold cyan]Conceptos Básicos de MongoDB[/bold cyan] 📌"))
    
    while True:
        # Mostrar menú de operaciones básicas
        table = Table(title="Operaciones Básicas", show_header=True)
        table.add_column("Opción", style="cyan")
        table.add_column("Comando", style="green")
        table.add_column("Descripción", style="white")
        
        # Agregar opciones al menú
        table.add_row("1", "db.help()", "Mostrar ayuda de comandos de base de datos")
        table.add_row("2", "db.stats()", "Mostrar estadísticas de la BD")
        table.add_row("3", "show dbs", "Listar todas las bases de datos")
        table.add_row("4", "use <db>", "Cambiar a una base de datos")
        table.add_row("5", "db.dropDatabase()", "Eliminar la base de datos actual")
        table.add_row("6", "db.createCollection()", "Crear una nueva colección")
        table.add_row("7", "show collections", "Listar colecciones en la BD actual")
        table.add_row("8", "db.<col>.drop()", "Eliminar una colección")
        table.add_row("0", "Volver", "Regresar al menú principal")
        console.print(table)
        
        choice = console.input("\n🔹Seleccione una operación para ejecutar (0-8): ")
        
        if choice == "0":
            break
        elif choice == "1":
            # help() - Mostrar información de ayuda sobre comandos de MongoDB
            console.print("\n[bold]Ejemplo de db.help():[/bold]")
            console.print("""
Este comando muestra todos los métodos disponibles para manipular la base de datos.
[yellow]Uso:[/yellow]
> db.help()
[yellow]Comandos comunes:[/yellow]
- db.adminCommand(nameOrDocument) - ejecuta comando en la BD admin
- db.aggregate([pipeline], {options}) - realiza operaciones de agregación
- db.auth(username, password) - autenticación en la BD
- db.createCollection(name, options) - crea una nueva colección
- db.createUser(user) - crea un nuevo usuario
- db.currentOp() - muestra operaciones en ejecución
- db.dropDatabase() - elimina la base de datos actual
- db.eval() - ejecuta código JavaScript
- db.fsyncLock() - bloquea la BD para backup
- db.fsyncUnlock() - desbloquea la BD
- db.getCollection(cname) - obtiene una colección
- db.getLogComponents() - obtiene niveles de log
- db.getMongo() - obtiene la conexión al servidor
- db.getName() - obtiene el nombre de la BD actual
- db.getPrevError() - obtiene errores previos
- db.getProfilingLevel() - obtiene nivel de profiling
- db.getProfilingStatus() - obtiene estado del profiling
- db.getReplicationInfo() - obtiene info de replicación
- db.getSiblingDB(name) - obtiene otra BD sin cambiar la actual
- db.help() - muestra esta ayuda
- db.hostInfo() - información del host
- db.isMaster() - verifica si es el nodo primario
- db.killOp(opid) - termina una operación
- db.listCommands() - lista todos los comandos
- db.logout() - cierra la sesión actual
- db.printCollectionStats() - estadísticas de colecciones
- db.printReplicationInfo() - información de replicación
- db.printShardingStatus() - estado del sharding
- db.printSlaveReplicationInfo() - info de replicación secundaria
- db.repairDatabase() - repara la BD actual
- db.resetError() - resetea errores
- db.runCommand(cmdObj) - ejecuta comando de BD
- db.serverStatus() - estado del servidor
- db.setLogLevel(level, component) - establece nivel de log
- db.setProfilingLevel(level, slowms) - establece nivel de profiling
- db.shutdownServer() - apaga el servidor
- db.stats() - estadísticas de la BD
- db.version() - versión de MongoDB
""")
        elif choice == "2":
            # stats() - Obtener estadísticas de la base de datos actual
            console.print("\n[bold]Ejemplo de db.stats():[/bold]")
            try:
                # command() - Método para ejecutar comandos de administración
                stats = db.command("dbstats")
                result_table = Table(title="Estadísticas de la Base de Datos")
                result_table.add_column("Métrica", style="cyan")
                result_table.add_column("Valor", style="green")
                
                # Agregar métricas importantes con descripciones
                metrics = {
                    "db": "Nombre de la base de datos",
                    "collections": "Número total de colecciones",
                    "views": "Número de vistas",
                    "objects": "Número total de documentos",
                    "avgObjSize": "Tamaño promedio de documentos (bytes)",
                    "dataSize": "Tamaño total de datos (bytes)",
                    "storageSize": "Tamaño en disco (bytes)",
                    "indexes": "Número total de índices",
                    "indexSize": "Tamaño total de índices (bytes)",
                    "totalSize": "Tamaño total (datos + índices)",
                    "scaleFactor": "Factor de escala para métricas",
                }
                for key, desc in metrics.items():
                    if key in stats:
                        value = stats[key]
                        if isinstance(value, (int, float)):
                            if key.endswith("Size"):
                                # Convertir bytes a formato legible
                                value = format_bytes(value)
                            result_table.add_row(f"{key} ({desc})", str(value))
                console.print(result_table)
            except Exception as e:
                console.print(f"\n❌[red]Error al obtener estadísticas: {e}[/red]")
        elif choice == "3":
            # list_database_names() - Listar todas las bases de datos
            console.print("\n[bold]Ejemplo de show dbs:[/bold]")
            try:
                dbs = db.client.list_database_names()
                db_table = Table(title="Bases de Datos Disponibles")
                db_table.add_column("Nombre", style="cyan")
                db_table.add_column("Tamaño", style="green")
                for db_name in dbs:
                    # Obtener estadísticas de cada base de datos
                    size = db.client[db_name].command("dbstats")["dataSize"]
                    db_table.add_row(db_name, format_bytes(size))
                console.print(db_table)
            except Exception as e:
                console.print(f"\n❌[red]Error al listar bases de datos: {e}[/red]")
        elif choice == "4":
            # Cambiar a otra base de datos
            console.print("\n[bold]Ejemplo de use <database>:[/bold]")
            db_name = console.input("Ingrese el nombre de la BD a cambiar: ")
            try:
                new_db = db.client[db_name]
                # Intentar una operación para verificar acceso
                new_db.command("ping")
                console.print(f"\n✅[green]Cambiado a la base de datos '{db_name}'[/green]")
                # Mostrar colecciones en la nueva BD
                cols = new_db.list_collection_names()
                if cols:
                    col_table = Table(title=f"Colecciones en '{db_name}'")
                    col_table.add_column("Nombre", style="cyan")
                    col_table.add_column("Documentos", style="green")
                    for col in cols:
                        count = new_db[col].count_documents({})
                        col_table.add_row(col, str(count))
                    console.print(col_table)
                else:
                    console.print(f"\ni️ La BD '{db_name}' no tiene colecciones")
            except Exception as e:
                console.print(f"\n❌[red]Error al cambiar de base de datos: {e}[/red]")
        elif choice == "5":
            # drop_database() - Eliminar la base de datos actual
            console.print("\n[bold]Ejemplo de db.dropDatabase():[/bold]")
            confirm = console.input(f"¿Está seguro de eliminar la base de datos '{db.name}'? (s/n): ")
            if confirm.lower() == 's':
                try:
                    db.client.drop_database(db.name)
                    console.print(f"\n✅[green]Base de datos '{db.name}' eliminada correctamente[/green]")
                except Exception as e:
                    console.print(f"\n❌[red]Error al eliminar la base de datos: {e}[/red]")
            else:
                console.print("\ni️ Operación cancelada")
        elif choice == "6":
            # create_collection() - Crear una nueva colección
            console.print("\n[bold]Ejemplo de db.createCollection():[/bold]")
            name = console.input("Nombre de la nueva colección: ")
            try:
                # Verificar si la colección ya existe
                if name in db.list_collection_names():
                    console.print(f"\n⚠️[yellow]La colección '{name}' ya existe[/yellow]")
                else:
                    db.create_collection(name)
                    console.print(f"\n✅[green]Colección '{name}' creada correctamente[/green]")
                # Mostrar opciones avanzadas disponibles
                console.print("""
[yellow]Opciones disponibles para createCollection:[/yellow]
- capped: Boolean - Colección de tamaño fijo
- size: Number - Tamaño máximo en bytes
- max: Number - Número máximo de documentos
- validator: Document - Reglas de validación
- validationLevel: String - Nivel de validación
- validationAction: String - Acción al validar
""")
            except Exception as e:
                console.print(f"\n❌[red]Error al crear la colección: {e}[/red]")
        elif choice == "7":
            # list_collection_names() - Listar colecciones
            console.print("\n[bold]Ejemplo de show collections:[/bold]")
            try:
                collections = db.list_collection_names()
                if collections:
                    col_table = Table(title="Colecciones en la Base de Datos")
                    col_table.add_column("Nombre", style="cyan")
                    col_table.add_column("Documentos", style="green")
                    col_table.add_column("Tamaño", style="yellow")
                    col_table.add_column("Índices", style="magenta")
                    for col_name in collections:
                        # Obtener estadísticas de la colección
                        stats = db.command("collstats", col_name)
                        col_table.add_row(
                            col_name,
                            str(stats["count"]),
                            format_bytes(stats["size"]),
                            str(len(stats["indexSizes"]))
                        )
                    console.print(col_table)
                else:
                    console.print("\ni️ No hay colecciones en esta base de datos")
            except Exception as e:
                console.print(f"\n❌[red]Error al listar colecciones: {e}[/red]")
        elif choice == "8":
            # drop() - Eliminar una colección
            console.print("\n[bold]Ejemplo de db.<collection>.drop():[/bold]")
            collections = db.list_collection_names()
            if not collections:
                console.print("\ni️ No hay colecciones para eliminar")
            else:
                # Mostrar colecciones disponibles
                col_table = Table(title="Colecciones Disponibles")
                col_table.add_column("#", style="cyan")
                col_table.add_column("Nombre", style="green")
                col_table.add_column("Documentos", style="yellow")
                for i, col_name in enumerate(collections, 1):
                    count = db[col_name].count_documents({})
                    col_table.add_row(str(i), col_name, str(count))
                console.print(col_table)
                
                # Solicitar colección a eliminar
                col_choice = console.input("\nSeleccione la colección a eliminar (número): ")
                try:
                    idx = int(col_choice) - 1
                    if 0 <= idx < len(collections):
                        col_name = collections[idx]
                        confirm = console.input(f"¿Está seguro de eliminar la colección '{col_name}'? (s/n): ")
                        if confirm.lower() == 's':
                            db[col_name].drop()
                            console.print(f"\n✅[green]Colección '{col_name}' eliminada correctamente[/green]")
                        else:
                            console.print("\ni️ Operación cancelada")
                    else:
                        console.print("\n❌[red]Opción inválida[/red]")
                except ValueError:
                    console.print("\n❌[red]Por favor, ingrese un número válido[/red]")
                except Exception as e:
                    console.print(f"\n❌[red]Error al eliminar la colección: {e}[/red]")
        else:
            console.print("\n❌[red]Opción inválida. Intente nuevamente.[/red]")
        
        console.input("\nPresione Enter para continuar...")
        console.clear()

def format_bytes(size):
    """
    Formatea un tamaño en bytes a una cadena legible
    Args:
    size: Tamaño en bytes
    Returns:
    str: Tamaño formateado (ej: '1.23 MB')
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"
