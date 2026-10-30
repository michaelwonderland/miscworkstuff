# Inlines the embedded fonts into the template to produce index.html
import pathlib
d = pathlib.Path(__file__).parent
t = (d / 'template.html').read_text()
(d / 'index.html').write_text(t.replace('<!--FONTS-->', (d / 'fonts.css.html').read_text()))
