ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'

python scripts/make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

python scripts/give_layouts.py
python scripts/escape_markdowns.py
call jekyll b

python scripts/string_replacer.py

move ..\zhhomestuck.github.io\p\copyright.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\translators.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\whatishomestuck.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\whatishomestuck-old.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\index.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\404.html ..\zhhomestuck.github.io

echo update index.html
python scripts/index_updater.py

echo done.