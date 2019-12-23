ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'

python scripts/make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

python scripts/give_layouts.py
python scripts/escape_markdowns.py
call jekyll b

python scripts/string_replacer.py
python scripts/index_updater.py

cd ..\zhhomestuck.github.io\p

move copyright.html ..
move translators.html ..
move whatishomestuck.html ..
move whatishomestuck-old.html ..
move index.html
move 404.html ..

echo done.