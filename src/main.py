import os
import shutil
import sys

from copystatic import copy_files_recursive
from block_markdown import markdown_to_html_node, extract_title


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    dir_path_static = "./static"
    dir_path_docs = "./docs"
    dir_path_content = "./content"
    template_path = "template.html"

    print(f"Deleting {dir_path_docs} directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print(f"Copying static files to {dir_path_docs} directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating pages...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
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

    # Rewrite paths for sub-directory hosting
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "" and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(final_html)


if __name__ == "__main__":
    main()
