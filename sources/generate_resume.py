from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
D=Document(); sec=D.sections[0];sec.page_width=Inches(8.27);sec.page_height=Inches(11.69)
sec.top_margin=sec.bottom_margin=Inches(.58);sec.left_margin=sec.right_margin=Inches(.65)
N=D.styles['Normal'];N.font.name='Calibri';N.font.size=Pt(11);N.paragraph_format.space_after=Pt(4);N.paragraph_format.line_spacing=1.0
for st in D.styles:
 for el in list(st.element.iter(qn('w:pBdr'))):el.getparent().remove(el)
for name in ['Title','Heading 1']:
 D.styles[name].font.name='Calibri';D.styles[name].font.color.rgb=RGBColor(0,0,0)
D.styles['Title'].font.size=Pt(25);D.styles['Title'].paragraph_format.space_after=Pt(4)
H=D.styles['Heading 1'];H.font.size=Pt(11);H.font.bold=True;H.paragraph_format.space_before=Pt(9);H.paragraph_format.space_after=Pt(4)
def p(t='',bold=False):
 x=D.add_paragraph();r=x.add_run(t);r.bold=bold;return x
def link(x,t,url):
 h=OxmlElement('w:hyperlink');h.set(qn('r:id'),x.part.relate_to(url,RT.HYPERLINK,is_external=True));r=OxmlElement('w:r');pr=OxmlElement('w:rPr');c=OxmlElement('w:color');c.set(qn('w:val'),'245B76');pr.append(c);u=OxmlElement('w:u');u.set(qn('w:val'),'single');pr.append(u);r.append(pr);tt=OxmlElement('w:t');tt.text=t;r.append(tt);h.append(r);x._p.append(h)
def head(t):
 x=D.add_paragraph(t,'Heading 1');pr=x._p.get_or_add_pPr();b=OxmlElement('w:pBdr');line=OxmlElement('w:bottom');line.set(qn('w:val'),'single');line.set(qn('w:sz'),'4');line.set(qn('w:color'),'AAB7C2');line.set(qn('w:space'),'4');b.append(line);pr.append(b)
def bullet(t):
 x=p('• '+t);x.paragraph_format.left_indent=Inches(.12);x.paragraph_format.first_line_indent=Inches(-.12)
def project(title,stack,url=None):
 x=p();x.paragraph_format.space_before=Pt(7);x.paragraph_format.keep_with_next=True
 x.add_run(title).bold=True
 if url:x.add_run('  |  ');link(x,'View project',url)
 y=p(stack);y.paragraph_format.space_after=Pt(3);y.paragraph_format.keep_with_next=True;y.runs[0].italic=True;y.runs[0].font.size=Pt(10);y.runs[0].font.color.rgb=RGBColor.from_string('245B76')
x=D.add_paragraph('MOHAMMED NAFEES H','Title');x.alignment=WD_ALIGN_PARAGRAPH.CENTER
x=p('Robotics and AI Engineering Student | Robot Software | Embedded Systems | Computer Vision',True);x.alignment=WD_ALIGN_PARAGRAPH.CENTER;x.runs[0].font.size=Pt(10)
x=p('Kumbakonam, Tamil Nadu, India  |  +91 9629461267  |  ');link(x,'mohammednafees1007@gmail.com','mailto:mohammednafees1007@gmail.com');x.alignment=WD_ALIGN_PARAGRAPH.CENTER
x=p();link(x,'GitHub portfolio','https://github.com/mohammednafees1007-hub');x.add_run('  |  ');link(x,'LinkedIn profile','https://www.linkedin.com/in/mohammed-nafees-h');x.add_run('  |  As of November 2026');x.alignment=WD_ALIGN_PARAGRAPH.CENTER
for r in x.runs:r.font.size=Pt(9);r.font.color.rgb=RGBColor.from_string('52616D')
head('PROFILE')
p('Robotics and Artificial Intelligence undergraduate building physical robots and computer-vision systems across Python/C++, ROS 2 workflows, embedded hardware, perception, and controls. Experience spans autonomous grid navigation, visual quality grading, image-analysis backends, and confidential industrial integration. Interested in research that connects algorithms with reliable real-world robot behavior.')
head('EDUCATION')
p('SASTRA Deemed University | B.Tech in Robotics and Artificial Intelligence',True)
p('August 2024 - May 2028 (expected) | Tamil Nadu, India')
p('Relevant coursework: Introduction to Artificial Intelligence; Computational Methods for AI & Automation; Sensors & Actuators for Robotics; Machine Learning Systems; Robotics Actuation & Power Drive Technologies; Systems Design; Introduction to Robotics.')
head('TECHNICAL SKILLS')
for label,body in [
 ('Programming and development','Python, C/C++, Linux shell scripting, Git, VS Code, Linux/Ubuntu 24.04.'),
 ('Robotics and controls','ROS 2 workflows, A* path planning, frontier exploration, inverse kinematics, motor control, robot integration, CoppeliaSim.'),
 ('Computer vision and ML','OpenCV, PyTorch, TensorFlow/Keras, YOLOv8/Ultralytics, MobileNetV2, CLIP, BLIP, Hugging Face Transformers, FastAPI.'),
 ('Embedded platforms','Arduino, ESP32, STM32, Raspberry Pi 5, Raspberry Pi Zero 2 W, Pi Camera, GPIO, motor drivers, wheel encoders, IR sensors.'),
 ('Sensors and interfaces','UART/serial communication, I2C, camera sensors, sensor/actuator interfacing; familiarity with LiDAR and IMU hardware.'),
 ('Engineering tools and lab','Fusion 360, EasyEDA/KiCad basics, schematic reading, soldering, wiring, hardware bring-up, component evaluation and procurement coordination.')]:
 x=p();x.add_run(label+': ').bold=True;x.add_run(body)
head('ENGINEERING EXPERIENCE')
x=p(); link(x,'Hardware Software Specialist | Confidential Industrial Robotics Project','https://www.linkedin.com/feed/update/urn:li:activity:7444209303684640768/')
p('March 2026 - Present | Part-time | Thanjavur, Tamil Nadu')
bullet('Contribute to ROS 2 workflows, controls-oriented development, embedded integration, and hardware-software coordination under NDA constraints.')
bullet('Support sensor and actuator identification, component evaluation, procurement planning, and integration debugging across software, electronics, and mechanical constraints.')
head('LEADERSHIP AND INVOLVEMENT')
x=p('ROBOTICS CLUB MEMBER | SASTRA DEEMED UNIVERSITY',True);x.runs[0].font.color.rgb=RGBColor.from_string('245B76')
bullet('Participate in robotics learning, project building, experimentation, and applied technical development.')
head('EXPERIENCE HIGHLIGHTS')
bullet('Build and test across software, electronics, and mechanical integration, not only simulation.')
bullet('Debug from observed failure states through hardware bring-up, sensor checks, and rapid prototype iteration in Linux-based robotics environments.')
D.add_page_break()
x=p('MOHAMMED NAFEES H  |  PROJECT PORTFOLIO',True);x.runs[0].font.size=Pt(14)
head('ROBOTICS AND COMPUTER VISION PROJECTS')
project('Hadi Al Hajatron','Python, Arduino, Tkinter, pyserial | January - May 2026','https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron')
bullet('Designed and developed a physical 4×4 grid-navigation robot with three directional IR sensors, wheel-encoder feedback, calibrated 60 cm movement steps, and 90° turns.')
bullet('Implemented frontier exploration, A* route planning, live mapping, JSON map export, and serial commands linking the Python interface to motor-control firmware.')
project('FruitVision AI','YOLOv8x, MobileNetV2, TensorFlow/Keras, CLIP, FastAPI','https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms')
bullet('Built a visual fruit-quality grading prototype combining fruit-region detection, three-class classification, fruit naming, annotated results, and A/B/C grade output.')
bullet('Recorded 76.8% test accuracy and 0.765 macro-F1 on 336 held-out images; implemented augmentation, checkpoint selection, and per-class evaluation. Evaluates visual freshness and damage.')
project('AI Image Analyzer','Python, YOLOv8n, OpenCV, BLIP | December 2025 - January 2026','https://github.com/mohammednafees1007-hub/ai-image-analyzer')
bullet('Built the Visage image-analysis backend combining 13-class object filtering, face localization with non-identifying per-image tokens, scene captions, and structured JSON output.')
project('Quadruped Kinematics and Gait Development','Python, forward and inverse kinematics | Team software prototype | Private repository','https://github.com/mohammednafees1007-hub/quadruped_RCS')
bullet('Contributed to inverse-kinematics and leg-motion development. The current prototype includes 3-DOF FK/IK, five gait patterns, reachability checks, 3-D visualization, and CSV trajectory export.')
bullet('Software supports geometric testing; physical gait validation remains in development.')
project('Driver Fatigue AI','PyTorch, temporal video inference | Experimental | Private repository','https://github.com/mohammednafees1007-hub/driver-fatigue-ai')
bullet('Developed an inference and evaluation pipeline with rolling frame buffers, score smoothing, and subject-disjoint checks; investigating generalization before deployment.')
head('ADDITIONAL HARDWARE PROJECTS')
project('Cyber Lift V1','Raspberry Pi 5, Pi Camera 3, OpenCV, Python | August - September 2025','https://www.linkedin.com/in/mohammed-nafees-h')
bullet('Built a vision-only carton-handling prototype with a four-motor chassis, close-range ultrasonic stopping, and a dual-servo gripper; focused on camera perception and lightweight handling.')
project('Autonomous Plowing Robot','Arduino Uno, Arduino C/C++, ultrasonic sensing | April - May 2025','https://www.linkedin.com/in/mohammed-nafees-h')
bullet('Developed a plowing-simulation prototype with ultrasonic obstacle detection, motor control, and a servo-mounted blade. Demonstrated obstacle avoidance and simulated plowing motion.')
p('Earlier work: Arduino-based school robotics prototypes involving sensors, motor drivers, wiring, control experiments, and debugging.')
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.RIGHT
r=footer.add_run('Mohammed Nafees H  |  November 2026  |  ');r.font.size=Pt(8);r.font.color.rgb=RGBColor.from_string('6B7780')
f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'PAGE');footer._p.append(f)
D.core_properties.title='Mohammed Nafees H Robotics and AI Resume';D.core_properties.author='Mohammed Nafees H'
from pathlib import Path
OUTPUT_DIR = Path(__file__).resolve().parent.parent / 'Resume' / 'DOCX'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
D.save(OUTPUT_DIR / 'Mohammed_Nafees_H_Resume_November_2026.docx')
