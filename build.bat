rem ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'
python give_layouts.py
call jekyll b

echo removing unwanted tags
python p_tag_remover.py

echo copy pages...
for /r "./pages" %%f in (*.html) do copy pages\%%~nxf ..\zhhomestuck.github.io\p

echo make blog_raw.txt
python make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\blog-backup\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\blog-backup\blog.xml

echo make index.html
python index_updater.py
copy index_updated.html ..\zhhomestuck.github.io\index.html
del index_updated.html

echo done.
