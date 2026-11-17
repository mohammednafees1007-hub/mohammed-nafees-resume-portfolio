# Mohammed Nafees H — Resume, Latest 2026

_As of November 2026_

This repository maintains **exactly two résumé versions**: a comprehensive main résumé and a general one-page résumé. The one-page version is not specific to Google or any other employer.

## Download

| Version | PDF | Editable Word | Plain text |
| --- | --- | --- | --- |
| Main comprehensive · 2 pages | [PDF](pdf/Mohammed_Nafees_H_Resume_November_2026.pdf) | [DOCX](docx/Mohammed_Nafees_H_Resume_November_2026.docx) | [TXT](text/Mohammed_Nafees_H_Resume_November_2026.txt) |
| General single page · 1 page | [PDF](pdf/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.pdf) | [DOCX](docx/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.docx) | [TXT](text/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.txt) |

Both versions link the industrial experience heading to the [LinkedIn experience post](https://www.linkedin.com/feed/update/urn:li:activity:7444209303684640768/). Industrial descriptions remain non-proprietary.

## Layout
- `pdf/`: two finished PDFs.
- `docx/`: two editable Word documents.
- `text/`: matching text versions.
- `sources/generate_resume.py`: comprehensive Word-document source.
- `sources/generate_single_page_resume.py`: general one-page Word-document source.
- `requirements.txt`: Python dependency.

## Update both versions
Changes are **manual and reviewed**, not automatically synchronized from GitHub, LinkedIn or one résumé to the other.

1. Update the relevant Python source under `sources/`. Its content and formatting generate the corresponding Word document. Review shared facts in **both** sources when contact information, education, coursework, experience, dates or accomplishments change.
2. Install dependencies and rebuild:
   ```sh
   python -m venv .venv
   # Linux/macOS:
   . .venv/bin/activate
   # Windows PowerShell instead: .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   python sources/generate_resume.py
   python sources/generate_single_page_resume.py
   ```
   Each generator writes its matching DOCX into `docx/`. The generators do **not** produce PDF or TXT.
3. Inspect each DOCX in Word or LibreOffice, then export PDF into `pdf/` with the matching base filename. Update its `text/` copy to match. Direct Word edits must also be reflected in the generator, or a rebuild will overwrite them.
4. Check both rendered PDFs: main should remain two readable pages and single-page should remain one; verify every hyperlink, dates, text extraction and page breaks. Keep private repository links labeled, protect confidential information and distinguish prototypes or planned work from completed achievements.
5. Commit both affected document sets and their sources together. When changing the snapshot month, update visible dates, filenames, generator output names and README download links together.

For a new project, add verified evidence and a concise contribution to the comprehensive source. Include it in the one-page source only if it is stronger or more relevant than an existing project; keep that version selective rather than adding pages.

## Derive a future job-tailored copy
Use **both** maintained versions: the comprehensive résumé supplies the broader evidence and skills, while the general one-page résumé supplies the concise layout and strongest examples.

1. Read the job description and select only relevant, supported experience from the comprehensive version.
2. Work from a separate local copy of the one-page source; choose a distinct output filename before running it so neither canonical DOCX is overwritten.
3. Adjust ordering, summary and project selection honestly. Do not invent experience, qualifications, results or skills to match keywords.
4. Export and verify that application-specific copy separately. Keep these two canonical versions intact; do not commit extra résumé versions here unless explicitly requested.

This guide describes a manual workflow. It does not schedule updates, create tailored copies automatically or submit applications.

## Evidence and profiles
- [Hadi Al Hajatron](https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron)
- [FruitVision AI](https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms)
- [AI Image Analyzer](https://github.com/mohammednafees1007-hub/ai-image-analyzer)
- Quadruped RCS and Driver Fatigue AI links in the main résumé require authorized access to private repositories; no visibility changes are implied.
- [LinkedIn profile](https://www.linkedin.com/in/mohammed-nafees-h) · [GitHub profile](https://github.com/mohammednafees1007-hub)

## History
Superseded June documents, flat-folder November documents and the earlier Google-specific variant are removed from the current branch. They remain recoverable through Git history. No unrelated project repositories were removed. GitHub Pages is not used.
