# Mohammed Nafees H — Resume, Latest 2026

_As of November 2026_

This repository maintains **exactly two résumé versions**: a comprehensive main résumé and a general one-page résumé. The one-page version is not specific to Google or any other employer.

## Download

| Version | PDF | Editable Word | Plain text |
| --- | --- | --- | --- |
| Main comprehensive · 2 pages | [PDF](Resume/PDF/Mohammed_Nafees_H_Resume_November_2026.pdf) | [DOCX](Resume/DOCX/Mohammed_Nafees_H_Resume_November_2026.docx) | [TXT](Resume/Text/Mohammed_Nafees_H_Resume_November_2026.txt) |
| General single page · 1 page | [PDF](Resume/PDF/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.pdf) | [DOCX](Resume/DOCX/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.docx) | [TXT](Resume/Text/Mohammed%20Nafees%20Resume%20November%202026%20Single%20Page.txt) |

Both versions link the industrial experience heading to the [LinkedIn experience post](https://www.linkedin.com/feed/update/urn:li:activity:7444209303684640768/). Industrial descriptions remain non-proprietary.

## Layout
- `Resume/PDF/`: two finished PDFs.
- `Resume/DOCX/`: two editable Word documents.
- `Resume/Text/`: matching text versions.
- `sources/generate_resume.py`: comprehensive Word-document source.
- `sources/generate_single_page_resume.py`: general one-page Word-document source.
- `requirements.txt`: Python dependency.
- `Tailored Resume/`: future company-specific versions, organized as `<Company>/<Role>/PDF/`, `DOCX/` and `sources/`. Currently contains guidance only; no tailored résumé has been created.

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
   Each generator writes its matching DOCX into `Resume/DOCX/`. The generators do **not** produce PDF or TXT.
3. Inspect each DOCX in Word or LibreOffice, then export PDF into `Resume/PDF/` with the matching base filename. Update its `Resume/Text/` copy to match. Direct Word edits must also be reflected in the generator, or a rebuild will overwrite them.
4. Check both rendered PDFs: main should remain two readable pages and single-page should remain one; verify every hyperlink, dates, text extraction and page breaks. Keep private repository links labeled, protect confidential information and distinguish prototypes or planned work from completed achievements.
5. Commit both affected document sets and their sources together. When changing the snapshot month, update visible dates, filenames, generator output names and README download links together.

For a new project, add verified evidence and a concise contribution to the comprehensive source. Include it in the one-page source only if it is stronger or more relevant than an existing project; keep that version selective rather than adding pages.

## Derive a future job-tailored copy
Use **both** maintained versions: the comprehensive résumé supplies the broader evidence and skills, while the general one-page résumé supplies the concise layout and strongest examples.

1. Read the job description and select only relevant, supported experience from the comprehensive version.
2. Work from a separate copy of the one-page source; change its output path and filename to the target company's `Tailored Resume/<Company>/<Role>/DOCX/` folder before running it so neither canonical DOCX is overwritten.
3. Adjust ordering, summary and project selection honestly. Do not invent experience, qualifications, results or skills to match keywords.
4. When a company-specific version is requested, save it under `Tailored Resume/<Company>/<Role>/`, with `PDF/`, `DOCX/` and `sources/` subfolders (and a short README describing the role and date). Export and verify it separately. Keep exactly these two canonical versions under `Resume/PDF/` and `Resume/DOCX/`; never overwrite them with a company-specific copy.

This guide describes a manual workflow. It does not schedule updates, create tailored copies automatically or submit applications.

## Evidence and profiles
- [Hadi Al Hajatron](https://github.com/mohammednafees1007-hub/Hadi-Al-Hajatron)
- [FruitVision AI](https://github.com/mohammednafees1007-hub/fruit-quality-detector-for-sms)
- [AI Image Analyzer](https://github.com/mohammednafees1007-hub/ai-image-analyzer)
- Quadruped RCS and Driver Fatigue AI links in the main résumé require authorized access to private repositories; no visibility changes are implied.
- [LinkedIn profile](https://www.linkedin.com/in/mohammed-nafees-h) · [GitHub profile](https://github.com/mohammednafees1007-hub)

## History
Superseded June documents, flat-folder November documents and the earlier Google-specific variant are removed from the current branch. They remain recoverable through Git history. No unrelated project repositories were removed. GitHub Pages is not used.
