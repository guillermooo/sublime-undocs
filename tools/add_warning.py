import os

warning_text = """\
.. warning::

   Development of Sublime Text has moved on to version 3.

   As a result,
   **this branch for Sublime Text 2
   will not be updated any more**.
   Please select the ``latest`` branch
   in the panel on the bottom left
   and consider updating Sublime Text.
"""


def prepend_warning(content, fpath):
    lines = content.splitlines()

    # Find where our heading ends
    heading_start = None
    heading_end = None
    for i, l in enumerate(lines[:min(len(lines), 10)]):
        if l.startswith("="):
            if heading_start is None:
                heading_start = i
            elif heading_start == i - 2:
                # Legit =h= heading
                heading_end = i
                break
        elif l.strip() == "":
            if heading_start is not None:
                # Just h= heading
                heading_end = heading_start
                break
        elif heading_start is not None and i == heading_start + 2:
            break

    if heading_end is None:
        raise RuntimeError("shit just got real '%s'" % fpath)

    insert_lines = warning_text.splitlines()
    insert_lines.insert(0, "")
    insert_lines.append("")

    lines[heading_end + 1:heading_end + 1] = insert_lines

    return "\n".join(lines)


def main():
    source_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "source"))
    print(source_dir)
    for root, dirs, files in os.walk(source_dir):
        print(dirs, files)
        for fname in files:
            if not fname.endswith(".rst"):
                continue

            fpath = os.path.join(root, fname)
            with open(fpath, 'r') as f:
                content = f.read()

            content = prepend_warning(content, fpath)

            with open(fpath, 'w') as f:
                f.write(content)

            print(fpath)


if __name__ == '__main__':
    main()
