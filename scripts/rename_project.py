import os
from pathlib import Path


def rename_project():
    # 1. Get inputs
    print("--- Project Renaming Tool ---")
    new_name = input("Enter new project name (e.g., 'Super Tool'): ").strip()
    if not new_name:
        print("Project name cannot be empty.")
        return

    # 2. Derive variants
    # "Super Tool" -> "Super Tool"
    name_title = new_name
    # "Super Tool" -> "super_tool"
    name_snake = new_name.lower().replace(" ", "_").replace("-", "_")
    # "Super Tool" -> "super-tool"
    name_kebab = new_name.lower().replace(" ", "-").replace("_", "-")
    # "Super Tool" -> "SuperTool"
    name_pascal = new_name.title().replace(" ", "").replace("-", "").replace("_", "")

    # Old values to replace
    OLD_SNAKE = "my_app"
    OLD_KEBAB = "my-app"
    OLD_TITLE = "My App"
    OLD_PASCAL = "MyApp"

    # 3. Define root
    root_dir = Path(__file__).resolve().parents[1]  # scripts/../
    src_dir = root_dir / "src"
    old_pkg_dir = src_dir / OLD_SNAKE

    print(f"\nRenaming '{OLD_TITLE}' to '{name_title}'...")

    # 4. Rename directories first
    if old_pkg_dir.exists():
        new_pkg_dir = src_dir / name_snake
        print(f"Renaming directory: {old_pkg_dir.name} -> {new_pkg_dir.name}")
        old_pkg_dir.rename(new_pkg_dir)

    # 5. Rename specific files (spec file)
    old_spec = root_dir / f"{OLD_KEBAB}.spec"
    if old_spec.exists():
        new_spec = root_dir / f"{name_kebab}.spec"
        print(f"Renaming file: {old_spec.name} -> {new_spec.name}")
        old_spec.rename(new_spec)

    # 6. Replace content in files
    extensions = {".py", ".toml", ".spec", ".md", ".json", ".yaml", ".yml"}
    exclude_dirs = {
        ".git",
        ".venv",
        "__pycache__",
        "build",
        "dist",
        ".pytest_cache",
        ".ruff_cache",
    }

    for current_path, dirs, files in os.walk(root_dir):
        # Skip excluded dirs
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if Path(file).suffix not in extensions:
                continue

            # Skip this script itself
            if file == "rename_project.py":
                continue

            file_path = Path(current_path) / file

            try:
                content = file_path.read_text(encoding="utf-8")

                # Check if replacement needed
                if any(
                    x in content for x in [OLD_SNAKE, OLD_KEBAB, OLD_TITLE, OLD_PASCAL]
                ):
                    new_content = content.replace(OLD_SNAKE, name_snake)
                    new_content = new_content.replace(OLD_KEBAB, name_kebab)
                    new_content = new_content.replace(OLD_TITLE, name_title)
                    new_content = new_content.replace(OLD_PASCAL, name_pascal)

                    file_path.write_text(new_content, encoding="utf-8")
                    print(f"Updated content in: {file_path.relative_to(root_dir)}")
            except Exception as e:
                print(f"Skipping {file}: {e}")

    print("\nDone! You may need to re-install dependencies if package name changed.")
    print("Run: uv pip install -e .[dev]")


if __name__ == "__main__":
    rename_project()
