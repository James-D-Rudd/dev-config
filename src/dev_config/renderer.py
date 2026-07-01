from jinja2 import Environment, FileSystemLoader

def render_templates(config, template_dir, output_dir, templates):
    env = Environment(loader=FileSystemLoader(template_dir))

    for tname in templates:
        template = env.get_template(tname)
        rendered = template.render(**config)

        out_name = tname.replace(".j2", "")
        with open(f"{output_dir}/{out_name}", "w") as f:
            f.write(rendered)
