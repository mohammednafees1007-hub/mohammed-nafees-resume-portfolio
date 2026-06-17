from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer


ROOT = Path(__file__).resolve().parent
TXT = ROOT / "Mohammed_Nafees_H_ATS_Resume.txt"
PDF = ROOT / "Mohammed_Nafees_H_ATS_Resume.pdf"


def para_style(name, size, leading, bold=False, after=0):
    return ParagraphStyle(
        name,
        fontName="Helvetica-Bold" if bold else "Helvetica",
        fontSize=size,
        leading=leading,
        spaceAfter=after,
    )


styles = {
    "name": para_style("name", 14.2, 15.2, True, 1.2),
    "contact": para_style("contact", 7.2, 8.2, False, 0.8),
    "section": para_style("section", 8.1, 9.1, True, 1.2),
    "body": para_style("body", 7.0, 8.0, False, 0.6),
    "bold": para_style("bold", 7.1, 8.0, True, 0.5),
}


sections = {
    "SUMMARY",
    "EDUCATION",
    "TECHNICAL SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "LINKEDIN PUBLIC PROOF",
    "LEADERSHIP",
    "ENGINEERING HIGHLIGHTS",
}


def p(text, style_name="body"):
    safe = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return Paragraph(safe, styles[style_name])


def build():
    doc = BaseDocTemplate(
        str(PDF),
        pagesize=letter,
        leftMargin=0.48 * inch,
        rightMargin=0.48 * inch,
        topMargin=0.4 * inch,
        bottomMargin=0.38 * inch,
        title="Mohammed Nafees H ATS Resume",
        author="Mohammed Nafees H",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="one", frames=[frame])])

    story = []
    lines = TXT.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        if index == 0:
            story.append(p(line, "name"))
        elif line in sections:
            story.append(Spacer(1, 1.6))
            story.append(p(line, "section"))
        elif line.startswith("- "):
            story.append(p(line, "body"))
        elif ":" in line and index < 6:
            story.append(p(line, "contact"))
        elif " - " in line and not line.startswith("GitHub"):
            story.append(p(line, "bold"))
        else:
            story.append(p(line, "body"))

    doc.build(story)
    print(PDF)


if __name__ == "__main__":
    build()

