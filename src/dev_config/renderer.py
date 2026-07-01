from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def render_templates(config, template_dir, output_dir, templates):
    env = Environment(loader=FileSystemLoader(template_dir))

    for tname in templates:
        template = env.get_template(tname)
        rendered = template.render(**config)

        out_name = tname.replace(".j2", "")
        out_path = Path(output_dir) / out_name
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            f.write(rendered)
