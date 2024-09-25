# Dexter Documentation

## Development Environment

See https://squidfunk.github.io/mkdocs-material/getting-started/

Or use the docker image:

```bash
docker pull squidfunk/mkdocs-material
```

Then run commands:

```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

## Working on the documentation

Live preview of the website:

```bash
mkdocs serve
```

Building the website:

```bash
mkdocs build
```
