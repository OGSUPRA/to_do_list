from db.models import init_db
from cli.menu import run_cli

def main():
    init_db()
    run_cli()

if __name__ == "__main__":
    main()
