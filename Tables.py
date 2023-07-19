from rich import box
from rich.table import Table


class Tables():
    def generate_table(columns: list):
        """Generate a table"""

        # table definition
        table = Table(
            box=box.SIMPLE,
            style="cyan"
        )

        # column for row numbers
        table.add_column(
            "#",
            style="cyan",
            header_style="cyan",
            justify="right"
        )

        # loop through the provided column names, add them to the table
        for title in columns:
            table.add_column(
                title,
                header_style="cyan"
            )

        return table

    def populate_table(table_to_populate, population: list):
        table = table_to_populate

        # loop through the items in population[], add them to the table
        for i, populant in enumerate(population):
            table.add_row(
                str(i+1),  # add row numbers to the table
                populant
            )

        return table
