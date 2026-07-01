import argparse
from dev_config.loader import load_config
from dev_config.renderer import render_templates
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(prog="devcfg")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync = subparsers.add_parser("sync")
    sync.add_argument("path", help="Project path (e.g. .)")

    args = parser.parse_args()

    if args.command == "sync":
        config = load_config(f"{args.path}/.devcfg.yaml")
        templates_to_render = load_config(f"{args.path}/.dev_templates_list.yaml")

        base_dir = Path(__file__).resolve().parent.parent.parent
        template_dir = base_dir / "templates"

        render_templates(
            config=config,
            template_dir=str(template_dir),
            output_dir=args.path,
            templates=templates_to_render
        )

if __name__ == "__main__":
    main()

