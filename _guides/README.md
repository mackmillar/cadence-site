# Guides source

The guide pages, `guides.html` and `sitemap.xml` are generated from `content.py`.
Edit the content there, then rebuild from the repo root:

    python3 _guides/build.py .

Voice follows the app's tone-of-voice rules: plain, British, no exclamation
marks, no guilt. Topics were picked from OpenSEO keyword data (UK), favouring
low difficulty and questions about turning up rather than what to lift.
This folder is excluded from deploys by `.vercelignore`.
