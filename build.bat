rem ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'

python make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

python give_layouts.py
python escape_mardowns.py
call jekyll b

python string_replacer.py

rem echo copy pages...
rem for /r "./pages" %%f in (*.html) do copy pages\%%~nxf ..\zhhomestuck.github.io\p
move ..\zhhomestuck.github.io\p\copyright.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\translators.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\whatishomestuck.html ..\zhhomestuck.github.io
move ..\zhhomestuck.github.io\p\whatishomestuck-old.html ..\zhhomestuck.github.io


echo make index.html
python index_updater.py
copy index_updated.html ..\zhhomestuck.github.io\index.html
del index_updated.html

echo done.
