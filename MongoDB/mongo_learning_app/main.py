import os
from dotenv import load_dotenv
from pymongo import MongoClient
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print
# Importar módulos
from modules import (
basics,
crud,
indexes,
aggregation,
transactions,
validation,
administration
)
console = Console()
def show_menu():"""Muestra el menú principal de la aplicación"""
console.print(Panel.fit("📖 [bold cyan]MongoDB Learning App[/bold cyan] 📖"))
menu = Table(title="Módulos Disponibles", show_header=True, header_style="bold magenta")
menu.add_column("Opción", style="cyan")
menu.add_column("Módulo", style="green")
menu.add_column("Descripción", style="white")
menu.add_row("1", "Conceptos Básicos", "Operaciones fundamentales con DBs y colecciones")
menu.add_row("2", "CRUD", "Creación, lectura, actualización y eliminación de documentos")
menu.add_row("3", "Índices", "Creación y manejo de índices")
menu.add_row("4", "Agregación", "Pipeline de agregación")
menu.add_row("5", "Transacciones", "Operaciones transaccionales")
menu.add_row("6", "Validación", "Validación de esquemas")
menu.add_row("7", "Administración", "Usuarios, roles y mantenimiento")
menu.add_row("0", "Salir", "Terminar la aplicación")
console.print(menu)
def main():load_dotenv()
# Conexión a MongoDB

try:
    Client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("DB_NAME", "learning_mongo")]
    console.print("✅[green]Conexión exitosa a MongoDB[/green]")
except Exception as e:
    console.print(f"❌[red]Error al conectar a MongoDB: {e}[/red]") 
    
    return

modules = {
"1": basics.run,
"2": crud.run,
"3": indexes.run,
"4": aggregation.run,
"5": transactions.run,
"6": validation.run,
"7": administration.run
}
while True:
    show_menu()
    choice = console.input("\n🔹Seleccione un módulo (0-7): ")
    if choice == "0":
        console.print("\n👋[yellow]Saliendo de la aplicación...[/yellow]")
    break
if choice in modules:
    console.clear()
    modules[choice](db)
else:
    console.print("\n❌[red]Opción inválida. Intente nuevamente.[/red]")
if __name__ == "__main__":
    main()