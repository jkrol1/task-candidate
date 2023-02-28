from app import create_app
from cli import create_cli_parser


def main():
    cli_parser = create_cli_parser()
    context = cli_parser.create_app_context()
    app = create_app(context)
    app.run()


if __name__ == "__main__":
    main()
