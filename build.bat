ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'

echo make blog_raw.txt
python make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

python give_layouts.py
python escape_mardowns.py
call jekyll b

echo replaceing unwanted strings
python string_replacer.py

echo copy pages...
for /r "./pages" %%f in (*.html) do copy pages\%%~nxf ..\zhhomestuck.github.io\p

echo make index.html
python index_updater.py
copy index_updated.html ..\zhhomestuck.github.io\index.html
del index_updated.html

echo done.
