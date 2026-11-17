# Mohammed Nafees H — Resume, Latest 2026

_As of November 2026_

Canonical résumé repository for Mohammed Nafees H, a Robotics and Artificial Intelligence undergraduate at SASTRA Deemed University.

## Résumé versions

### Version 1: Google Student Researcher
Focused one-page version featuring Hadi Al Hajatron, FruitVision AI and AI Image Analyzer.
- [Download targeted PDF](resume/Mohammed_Nafees_H_Google_Student_Researcher_Resume.pdf)
- [Download editable targeted Word document](resume/Mohammed_Nafees_H_Google_Student_Researcher_Resume.docx)
- [Read targeted plain-text version](resume/Mohammed_Nafees_H_Google_Student_Researcher_Resume.txt)
- [Targeted Word-document generator](resume/generate_gsr_resume.py)
- The experience heading links to this [LinkedIn experience post](https://www.linkedin.com/feed/update/urn:li:activity:7444209303684640768/).

This is a tailored résumé document, not a submitted application. A second targeted version has not been specified or created.

### Comprehensive November 2026 résumé
Preserved as the broader project and experience version.
- [Download PDF](resume/Mohammed_Nafees_H_Resume_November_2026.pdf)
- [Download editable Word document](resume/Mohammed_Nafees_H_Resume_November_2026.docx)
- [Read plain-text version](resume/Mohammed_Nafees_H_Resume_November_2026.txt)

The résumé highlights robotics software, embedded systems, computer vision, **Robotics Club involvement at SASTRA**, and confidential industrial experience described without proprietary details.

## Project evidence
- [Hadi Al Hajatron](https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron)
- [FruitVision AI](https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms)
- [AI Image Analyzer](https://github.com/mohammednafees1007-hub/ai-image-analyzer)
- Quadruped RCS and Driver Fatigue AI: private repositories; résumé links require authorized access.
- Cyber Lift V1 and Autonomous Plowing Robot: background on [LinkedIn](https://www.linkedin.com/in/mohammed-nafees-h).

[GitHub profile](https://github.com/mohammednafees1007-hub) · [LinkedIn profile](https://www.linkedin.com/in/mohammed-nafees-h)

## Updating this résumé
Updates are **manual and reviewed**, not automatically synchronized from GitHub or LinkedIn.

1. Edit the content and formatting in the source for the version you want to update: [resume/generate_resume.py](resume/generate_resume.py) for the comprehensive résumé or [resume/generate_gsr_resume.py](resume/generate_gsr_resume.py) for Version 1 (Google Student Researcher). These are the reproducible Word-document sources. Keep project names, dates, accomplishments, evidence links and status accurate. Do not turn planned work into completed achievements or disclose confidential details.
2. Set up Python and generate the DOCX:
   ```sh
   python -m venv .venv
   # Linux/macOS:
   . .venv/bin/activate
   # Windows PowerShell instead: .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python resume/generate_resume.py
   # Or build the focused Google Student Researcher version:
   python resume/generate_gsr_resume.py
   ```
3. Open the generated DOCX in Word or LibreOffice, inspect every page and export it as PDF using the matching filename. Each Python script generates its own **DOCX only**, not PDF or TXT.
4. Update the plain-text version to match the final résumé. Editing DOCX directly is supported, but also reflect those edits in the generator or the next build will overwrite them.
5. Verify PDF layout, text, page breaks and clickable links. Check that private links are labeled and that no confidential information has been added.
6. Commit the relevant generator, DOCX, PDF and TXT together. Review shared facts across both versions when updating education, contact details or experience; the two generators do not synchronize automatically. When the snapshot month changes, update the visible date, filenames, generator output filename and these download links together.

For a new project, add a concise evidence-backed entry and its public repository URL to the generator and this README, then rebuild and check all versions. Do not make private repositories public merely to enable a résumé link.

## Repository history
The June 2026 résumé files and older generators have been removed from the current branch and replaced by this November 2026 version. Earlier versions remain recoverable through Git commit history. GitHub Pages is not used.
