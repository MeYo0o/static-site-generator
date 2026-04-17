import os
import shutil

from copystatic import copy_files_recursive
from block_markdown import markdown_to_html_node, extract_title


def main():
    dir_path_static = "./static"
    dir_path_public = "./public"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join("content", "index.md"),
        "template.html",
        os.path.join("public", "index.html"),
    )


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise Exception(f"Markdown file not found: {from_path}")
    if not os.path.exists(template_path):
        raise Exception(f"Template file not found: {template_path}")

    with open(from_path, "r") as f:
        md_content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(md_content)
    html_content = html_node.to_html()

    title = extract_title(md_content)

    final_html = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "" and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(final_html)


if __name__ == "__main__":
    main()
