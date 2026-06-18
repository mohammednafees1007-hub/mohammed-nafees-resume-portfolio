from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
DOCX = ROOT / "Mohammed_Nafees_H_Styled_Resume.docx"

INK = RGBColor(17, 24, 39)
MUTED = RGBColor(75, 85, 99)
TEAL = RGBColor(15, 118, 110)


RESUME = {
    "name": "MOHAMMED NAFEES H",
    "headline": "Robotics & AI Engineering Student | Robotics Software | Embedded Systems | Computer Vision",
    "contact": [
        "Phone: +91 962-946-1267 | Email: mohammednafees1007@gmail.com",
        "Location: Kumbakonam, Tamil Nadu, India",
        "LinkedIn: https://www.linkedin.com/in/mohammed-nafees-h-7b3377306",
        "GitHub: https://github.com/mohammednafees1007-hub",
    ],
    "sections": [
        (
            "SUMMARY",
            [
                "B.Tech Robotics & Artificial Intelligence student at SASTRA University, Class of 2028, focused on robotics software, embedded systems, autonomous navigation, and AI/computer vision. Hands-on experience across ROS 2 workflows, Python/C++ robotics programming, Arduino and Raspberry Pi hardware, sensors, motor control, OpenCV, YOLOv8, Keras, and BLIP-based AI pipelines. Built public GitHub projects covering grid navigation, fruit quality detection, and image-analysis backends."
            ],
        ),
        (
            "EDUCATION",
            [
                ("SASTRA Deemed University - B.Tech, Robotics & Artificial Intelligence", True),
                "Aug 2024 - May 2028 | Tamil Nadu, India",
            ],
        ),
        (
            "TECHNICAL SKILLS",
            [
                ("Robotics Software: ", "ROS 2, Python, C/C++, Linux/Ubuntu, Git, robot integration, A* path planning, controls basics, sensor debugging"),
                ("Embedded Hardware: ", "Arduino, ESP32, STM32, Raspberry Pi 5, Raspberry Pi Zero 2 W, Pi Camera, GPIO, motor drivers, encoders, IR sensors"),
                ("Sensors and Communication: ", "I2C, UART, LiDAR, IMU, camera sensors, serial communication, sensor/actuator interfacing"),
                ("AI and Computer Vision: ", "OpenCV, YOLOv8, Ultralytics, TensorFlow/Keras, CLIP, BLIP, Hugging Face Transformers, image classification, object detection"),
                ("Hardware Lab and Tools: ", "soldering, schematic reading, hardware bring-up, wiring, component evaluation, procurement coordination, VS Code, CoppeliaSim, Fusion 360, EasyEDA/KiCad basics"),
            ],
        ),
        (
            "EXPERIENCE",
            [
                ("Hardware Software Specialist | Confidential Industrial Robotics Project | Part-time", True),
                ("Mar 2026 - Present | Thanjavur, Tamil Nadu, India | On-site", True),
                "Project details withheld due to signed confidentiality / NDA obligations.",
                [
                    "Contribute to an industry-level robotics project involving ROS 2-based workflows, controls-oriented development, embedded integration, and system-level coordination.",
                    "Support robotics software, hardware coordination, sensor/actuator evaluation, and practical deployment-focused engineering in a professional setting.",
                    "Coordinate component identification, evaluation, and procurement support for a project hardware budget of approximately six figures while maintaining strict confidentiality.",
                ],
            ],
        ),
        (
            "PROJECTS",
            [
                ("Hadi Al Hajatron - Arduino, Python, IR Sensors, Encoders, A* Path Planning", True),
                "GitHub: https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron",
                ["Engineered a 4x4 Arduino-Python autonomous grid-navigation robot with 3 IR obstacle sensors, 60 cm calibrated movement steps, live mapping, map export, frontier-based exploration, JSON map storage, and A* route planning."],
                ("FruitVision AI - Fruit Quality Detector for SMS - YOLOv8x, Keras, CLIP, OpenCV", True),
                "GitHub: https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms",
                ["Developed a quality-first fruit grading system with image input workflows, YOLOv8x fruit-region detection, a 3-class Keras quality model, A/B/C grade mapping, CLIP fruit naming support, and annotated result output."],
                ("AI Image Analyzer - Python, YOLOv8n, OpenCV, BLIP, Transformers", True),
                "GitHub: https://github.com/mohammednafees1007-hub/ai-image-analyzer",
                ["Created a backend image-analysis pipeline for a larger Visage project with YOLOv8n object detection, 13 allowed object classes, privacy-safe face tokens, BLIP captions, and structured app-ready output."],
                ("Quadruped Robot - Inverse Kinematics, Robotics Controls, Embedded Integration", True),
                ["Implemented inverse-kinematics motion logic for leg movement, connecting control theory with practical actuation for stable quadruped locomotion."],
                ("Schooling-Era Robotics Projects - Arduino, Sensors, Motor Drivers", True),
                ["Prototyped early Arduino robotics systems involving sensors, motor drivers, wiring, control experiments, and debugging."],
            ],
        ),
        (
            "LEADERSHIP",
            [
                ("Robotics Club Member - SASTRA Deemed University", True),
                ["Active in robotics learning, project building, experimentation, hardware bring-up, sensor debugging, and applied technical development."],
            ],
        ),
    ],
}


def set_run_font(run, size, color=INK, bold=False, name="Aptos"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:ascii"), name)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.bold = bold


def set_paragraph_spacing(paragraph, before=0, after=0, line=1.0):
    paragraph.paragraph_format.space_before = Pt(before)
    paragraph.paragraph_format.space_after = Pt(after)
    paragraph.paragraph_format.line_spacing = line


def add_bottom_border(paragraph, color="0F766E", size="8", space="4"):
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn("w:pBdr"))
    if p_bdr is None:
        p_bdr = OxmlElement("w:pBdr")
        p_pr.append(p_bdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), size)
    bottom.set(qn("w:space"), space)
    bottom.set(qn("w:color"), color)
    p_bdr.append(bottom)


def add_plain(doc, text, size=8.8, bold=False, color=INK, before=0, after=1.2):
    paragraph = doc.add_paragraph()
    set_paragraph_spacing(paragraph, before=before, after=after, line=1.0)
    run = paragraph.add_run(text)
    set_run_font(run, size=size, color=color, bold=bold)
    return paragraph


def add_label_value(doc, label, value):
    paragraph = doc.add_paragraph()
    set_paragraph_spacing(paragraph, after=1.0, line=1.0)
    label_run = paragraph.add_run(label)
    set_run_font(label_run, size=8.6, bold=True)
    value_run = paragraph.add_run(value)
    set_run_font(value_run, size=8.6)


def add_section(doc, title):
    paragraph = doc.add_paragraph()
    set_paragraph_spacing(paragraph, before=4.0, after=1.0, line=1.0)
    run = paragraph.add_run(title)
    set_run_font(run, size=9.4, color=TEAL, bold=True)
    add_bottom_border(paragraph, color="CCFBF1", size="6", space="2")


def add_bullet(doc, text):
    paragraph = doc.add_paragraph(style="List Bullet")
    set_paragraph_spacing(paragraph, after=1.0, line=1.0)
    paragraph.paragraph_format.left_indent = Inches(0.22)
    paragraph.paragraph_format.first_line_indent = Inches(-0.12)
    run = paragraph.add_run(text)
    set_run_font(run, size=8.45)


def configure_document(doc):
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.48)
    section.bottom_margin = Inches(0.48)
    section.left_margin = Inches(0.55)
    section.right_margin = Inches(0.55)
    section.header_distance = Inches(0.25)
    section.footer_distance = Inches(0.25)

    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
    normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
    normal.font.size = Pt(8.8)
    normal.font.color.rgb = INK

    bullet_style = doc.styles["List Bullet"]
    bullet_style.font.name = "Aptos"
    bullet_style._element.rPr.rFonts.set(qn("w:ascii"), "Aptos")
    bullet_style._element.rPr.rFonts.set(qn("w:hAnsi"), "Aptos")
    bullet_style.font.size = Pt(8.45)


def build():
    doc = Document()
    configure_document(doc)

    name = doc.add_paragraph()
    name.alignment = WD_ALIGN_PARAGRAPH.LEFT
    set_paragraph_spacing(name, after=0.6, line=1.0)
    name_run = name.add_run(RESUME["name"])
    set_run_font(name_run, size=19, color=INK, bold=True)

    headline = doc.add_paragraph()
    set_paragraph_spacing(headline, after=1.4, line=1.0)
    headline_run = headline.add_run(RESUME["headline"])
    set_run_font(headline_run, size=9.5, color=INK, bold=True)
    add_bottom_border(headline, color="0F766E", size="8", space="3")

    for line in RESUME["contact"]:
        add_plain(doc, line, size=8.4, color=MUTED, after=0.2)

    for title, items in RESUME["sections"]:
        add_section(doc, title)
        for item in items:
            if isinstance(item, list):
                for bullet in item:
                    add_bullet(doc, bullet)
            elif isinstance(item, tuple):
                if len(item) == 2 and isinstance(item[1], bool):
                    add_plain(doc, item[0], size=8.7, bold=item[1], after=0.8)
                else:
                    add_label_value(doc, item[0], item[1])
            else:
                add_plain(doc, item, size=8.6, after=1.0)

    doc.core_properties.title = "Mohammed Nafees H Styled Resume"
    doc.core_properties.author = "Mohammed Nafees H"
    doc.core_properties.subject = "Robotics and AI resume"
    doc.core_properties.keywords = "Robotics, AI, ROS 2, Embedded Systems, Computer Vision, OpenCV, YOLOv8"
    doc.save(DOCX)
    print(DOCX)


if __name__ == "__main__":
    build()
