from typing import List, Optional

from app import Context, create_app
from cli import create_cli_parser


def main(args: Optional[List[str]] = None) -> None:
    cli_parser = create_cli_parser()
    parsed_args = cli_parser.parse_args(args)
    context = Context.from_parsed_cli_args(parsed_args)
    app = create_app(context)
    app.run()


if __name__ == "__main__":
    main()
