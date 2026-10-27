# GameTablesDocs
Documentation for GameTables Unity asset

## PDF Manual
`pdf/build_pdf.py` builds the site with Jekyll and turns it into a PDF manual for offline use. It needs macOS, Python 3.9+, Google Chrome and a running Docker Desktop. Save the PDF outside this repository:

```bash
python3 pdf/build_pdf.py "/tmp/Game Tables Manual.pdf"
```

The page layout is defined in `pdf/print.css`. To iterate on it, save the intermediate HTML with `--html /tmp/manual.html` and open it in Chrome.
