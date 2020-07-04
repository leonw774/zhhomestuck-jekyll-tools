ruby -r rubygems -e 'require "jekyll-import"; JekyllImport::Importers::Blogger.run({"source"=^>"blog.xml","no-blogger-info"=^>true,"replace-internal-link"=^>false})'

python scripts\preprocess.py
copy blog-raw.txt ..\zhhomestuck.github.io\backups\blog-raw.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

call bundle exec jekyll build

python scripts/postprocess.py
python scripts/index_updater.py
python scripts/write_flash_index.py

cd ..\zhhomestuck.github.io\p

move copyright.html ..
move translators.html ..
move whatishomestuck.html ..
move whatishomestuck-old.html ..
move index.html ..
move 404.html ..

cd ..\..\zhhomestuck-jekyll-tools
echo "finished updating site"
