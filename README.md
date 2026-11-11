# dev-infra-core
Shared development standards and repository bootstrap templates used across all projects.

To use this repo, run ./install.sh to install it as tool. Then, create the files .devcfg.yaml and .dev_templates_list.yaml

Valid options for .devcfg.yaml:
- repo_owner:
- repo_name:
- repo_contents:
    - List of code types present in the repo. Current code supported is
        - Python
            

.dev_templates_list.yaml works slightly differently. Every templated listed give you a different tool. Currently supported tools are:
- ".pre-commit-config.yaml.j2"
- "sonar-project.properties.j2"
- ".snyk.j2"
- ".coderabbit.yaml.j2"
- ".github/dependabot.yaml.j2"
- ".github/workflows/ci-on_push.yaml.j2"
