ruby -r rubygems -e 'require "jekyll-import"; JekyllImport::Importers::Blogger.run({"source"=^>"blog.xml","no-blogger-info"=^>true,"replace-internal-link"=^>false})'

python scripts\preprocess.py
copy blog-plain.txt ..\zhhomestuck.github.io\backups\blog-plain.txt
copy blog.xml ..\zhhomestuck.github.io\backups\blog.xml

call bundle exec jekyll build

move ..\zhhomestuck.github.io\p\tmps\* ..\zhhomestuck.github.io\

python scripts/postprocess.py
python scripts/index_updater.py
python scripts/write_flash_index.py

echo "finished updating site"
