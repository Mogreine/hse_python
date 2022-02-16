from typing import List


def create_table(table: List[List[str]]) -> str:
    centering_start = "\\begin{center}"
    centering_end = "\\end{center}"

    cols = " ".join("c" * len(table))
    table_start = "\\begin{tabular}{ " + cols + " }"
    table_end = "\\end{tabular}"

    table_body = "\\\\\n".join(map(lambda row: " & ".join(row), table))

    return "\n".join([centering_start, table_start, table_body, table_end, centering_end])


def create_document(body: str = "") -> str:
    document_class = "\\documentclass{article}"
    begin = "\\begin{document}"
    end = "\\end{document}"

    return "\n".join([document_class, begin, body, end])


if __name__ == "__main__":
    table = [["col1", "col2", "col3"], ["1", "2", "3"], ["word1", "word2", "word3"]]

    table_latex = create_table(table)
    latex_document = create_document(table_latex)

    with open("./artifacts/result.tex", "w") as f:
        f.write(latex_document)
