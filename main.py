"""
ATOS - Algorithmic Trading Operating System

Application entry point.
"""

from atos.app import ATOSApplication


def main() -> int:
    """Start the application."""
    app = ATOSApplication()
    return app.run()


if __name__ == "__main__":
    raise SystemExit(main())