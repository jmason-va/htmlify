from collections import OrderedDict
"""using an ordered ditionary to preserve order of replacements"""

replacements = (
    ('john', '<a class="john" href="./character.john.html">john</a>'),
    ('richard', '<a class="richard" href="./character.richard.html">richard</a>'),
    ('edward', '<a class="edward" href="./character.edward.html">edward</a>'),
    ('mason', '<a class="mason" href="./character.mason.html">mason</a>'),
    ('robert', '<a class="robert" href="./character.robert.html">robert</a>'),
    ('index', '<div class="index"><a class="index" href="./index.html">index</a></div>'),
    ('*--', '<div class="chapter-summary">'),
    ('*~-', '<div class="chapter-title">'),
    ('--*', '</div>'),
    ('\t', '&nbsp;&nbsp;&nbsp;&nbsp;')
)


replacements= OrderedDict(replacements)

