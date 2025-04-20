from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run(db):
    console.print(Panel.fit("📈 [bold cyan]Estadísticas del Sistema[/bold cyan] 📈"))
    with db.get_cursor() as cur:
        cur.execute("""
            SELECT current_database() AS base, pg_size_pretty(pg_database_size(current_database())) 
            AS tamaño;
        """)
        row = cur.fetchone()
        table = Table(title="Uso de Base de Datos")
        for k, v in row.items():
            table.add_column("Métrica")
            table.add_column("Valor")
            table.add_row(k, v)
        console.print(table)
