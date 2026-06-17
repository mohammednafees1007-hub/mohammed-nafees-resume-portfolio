from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer


ROOT = Path(__file__).resolve().parent
TXT = ROOT / "Mohammed_Nafees_H_ATS_Resume.txt"
PDF = ROOT / "Mohammed_Nafees_H_ATS_Resume.pdf"


def para_style(name, size, leading, bold=False, after=0, color=colors.black):
    return ParagraphStyle(
        name,
        fontName="Helvetica-Bold" if bold else "Helvetica",
        fontSize=size,
        leading=leading,
        spaceAfter=after,
        textColor=color,
        wordWrap="LTR",
    )


styles = {
    "name": para_style("name", 16.4, 17.8, True, 1.6, colors.HexColor("#111827")),
    "headline": para_style("headline", 8.8, 9.8, True, 1.4, colors.HexColor("#111827")),
    "contact": para_style("contact", 7.6, 8.5, False, 0.8, colors.HexColor("#1f2937")),
    "section": para_style("section", 9.0, 10.0, True, 1.4, colors.HexColor("#0f766e")),
    "body": para_style("body", 7.85, 8.95, False, 0.8, colors.HexColor("#111827")),
    "bold": para_style("bold", 8.0, 9.0, True, 0.7, colors.HexColor("#111827")),
}


sections = {
    "SUMMARY",
    "EDUCATION",
    "TECHNICAL SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "LEADERSHIP",
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
        pagesize=A4,
        leftMargin=0.42 * inch,
        rightMargin=0.42 * inch,
        topMargin=0.35 * inch,
        bottomMargin=0.35 * inch,
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
        elif index == 1:
            story.append(p(line, "headline"))
        elif line in sections:
            story.append(Spacer(1, 2.0))
            story.append(p(line, "section"))
        elif line.startswith("- "):
            story.append(p(line, "body"))
        elif ":" in line and index < 7:
            story.append(p(line, "contact"))
        elif (" - " in line or " | " in line) and not line.startswith("GitHub"):
            story.append(p(line, "bold"))
        else:
            story.append(p(line, "body"))

    doc.build(story)
    pages = len(PdfReader(str(PDF)).pages)
    if pages != 1:
        raise SystemExit(f"Expected one-page resume, generated {pages} pages")
    print(PDF)


if __name__ == "__main__":
    build()
