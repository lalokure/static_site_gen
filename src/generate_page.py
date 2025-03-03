
def extract_title(markdown):
    if "# " in markdown.splitlines()[0]:
        return markdown.splitlines()[0][2:]
    raise Exception("The heading must have a single #")
