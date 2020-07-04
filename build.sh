#!/bin/bash
ruby -r rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=>"./blog.xml","no-blogger-info"=>true,"replace-internal-link"=>false})'

python3 ./scripts/preprocess.py
cp blog-raw.txt ../zhhomestuck.github.io/backups/blog-raw.txt
cp blog.xml ../zhhomestuck.github.io/backups/blog.xml

jekyll build

python3 ./scripts/postprocess.py
python3 ./scripts/index_updater.py
python3 ./scripts/write_flash_index.py

cd ../zhhomestuck.github.io/p

mv ./copyright.html ..
mv ./translators.html ..
mv ./whatishomestuck.html ..
mv ./whatishomestuck-old.html ..
mv ./index.html ..
mv ./404.html ..

cd ../../zhhomestuck-jekyll-tools
echo "finished updating site"


