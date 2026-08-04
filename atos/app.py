"""
ATOS Application.

Main application lifecycle.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from atos import __version__


class ATOSApplication:
    """Main ATOS application."""

    def __init__(self) -> None:
        self.project_root = Path(__file__).resolve().parent.parent

    def build_parser(self) -> argparse.ArgumentParser:
        """Build CLI parser."""

        parser = argparse.ArgumentParser(
            prog="ATOS",
            description="Algorithmic Trading Operating System",
        )

        parser.add_argument(
            "command",
            nargs="?",
            default="help",
            choices=[
                "help",
                "version",
                "backtest",
                "paper",
                "live",
                "report",
                "doctor",
            ],
        )

        return parser

    def run(self) -> int:
        """Run the application."""

        parser = self.build_parser()

        args = parser.parse_args()

        match args.command:

            case "version":
                self.show_version()

            case "doctor":
                self.doctor()

            case "paper":
                print("Paper trading engine coming in Sprint 8.")

            case "live":
                print("Live Saxo trading coming in Sprint 10.")

            case "backtest":
                print("Backtest engine coming in Sprint 8.")

            case "report":
                print("Reporting engine coming in Sprint 11.")

            case _:
                parser.print_help()

        return 0

    def show_version(self) -> None:
        """Display version."""

        print("=" * 50)
        print("ATOS")
        print("Algorithmic Trading Operating System")
        print("=" * 50)
        print(f"Version : {__version__}")
        print("Environment : Development")
        print()

    def doctor(self) -> None:
        """Basic project health check."""

        print("Running diagnostics...\n")

        checks = {
            "Project Root": self.project_root.exists(),
            "README.md": (self.project_root / "README.md").exists(),
            "requirements.txt": (self.project_root / "requirements.txt").exists(),
            "atos Package": (self.project_root / "atos").exists(),
            "tests": (self.project_root / "tests").exists(),
            "logs": (self.project_root / "logs").exists(),
            "reports": (self.project_root / "reports").exists(),
            "data": (self.project_root / "data").exists(),
        }

        ok = True

        for name, result in checks.items():

            status = "✓" if result else "✗"

            print(f"{status} {name}")

            if not result:
                ok = False

        print()

        if ok:
            print("ATOS environment is healthy.")
        else:
            print("One or more checks failed.")