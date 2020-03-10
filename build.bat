ruby -r rubygems -e 'require "jekyll-import"; JekyllImport::Importers::Blogger.run({"source"=^>"blog.xml","no-blogger-info"=^>true,"replace-internal-link"=^>false})'

python scripts/make_raw_blog.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

python scripts/give_layouts.py
python scripts/escape_markdowns.py
call bundle exec jekyll build

python scripts/string_replacer.py
python scripts/index_updater.py
python scripts/write_flash_index.py

cd ..\zhhomestuck.github.io\p

move copyright.html ..
move translators.html ..
move whatishomestuck.html ..
move whatishomestuck-old.html ..
move index.html ..
move 404.html ..

echo "finished updating site"
