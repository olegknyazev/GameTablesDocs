# GameTablesDocs
Documentation for GameTables Unity asset

## PDF Manual
`pdf/build_pdf.py` turns the built site into a PDF manual for offline use. It needs macOS, Python 3.9+ and Google Chrome.

1. Build the site with Jekyll, or keep `docker compose up` running, which rebuilds `_site` on every change.
2. Build the PDF, saving it outside this repository:
   ```bash
   python3 pdf/build_pdf.py "/tmp/Game Tables Manual.pdf"
   ```

The page layout is defined in `pdf/print.css`. To iterate on it, save the intermediate HTML with `--html /tmp/manual.html` and open it in Chrome.
