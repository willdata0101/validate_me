from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_report(results, overall_passed):
    console.print(
        Panel.fit(
            "[bold magenta]validate_me[/bold magenta]\n[cyan]Retro API Validation Report[/cyan]",
            border_style="bright_magenta"
        )
    )

    table = Table(title="Validation Results", border_style="cyan")

    table.add_column("Status", justify="center")
    table.add_column("Path", style="bold")
    table.add_column("Check")
    table.add_column("Details")

    for result in results:
        status = "[green]PASS[/green]" if result["passed"] else "[red]FAIL[/red]"
        path = result.get("path", "")
        check = result.get("check_type", "")
        reason = result.get("reason", "")

        expected = result.get("expected_type", "")
        actual = result.get("actual_type", "")

        details = reason
        if expected or actual:
            details = f"{reason} | expected: {expected}, got: {actual}"

        table.add_row(status, path, check, details)

    console.print(table)

    final_status = (
        "[bold green]VALIDATION PASSED[/bold green]"
        if overall_passed
        else "[bold red]VALIDATION FAILED[/bold red]"
    )

    console.print(Panel.fit(final_status, border_style="green" if overall_passed else "red"))

