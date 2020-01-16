#!/bin/bash
ruby -r rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=>"./blog.xml",})'

python3 scripts/make_raw_blog.py
cp blog-raw.txt ../zhhomestuck.github.io/backups/blog-raw.txt
cp blog.xml ../zhhomestuck.github.io/backups/blog.xml

python3 scripts/give_layouts.py
python3 scripts/escape_markdowns.py
bundle exec jekyll build 

python3 scripts/string_replacer.py
python3 scripts/index_updater.py
python3 scripts/write_flash_index.py

cd ../zhhomestuck.github.io/p

mv ./copyright.html ..
mv ./translators.html ..
mv ./whatishomestuck.html ..
mv ./whatishomestuck-old.html ..
mv ./index.html ..
mv ./404.html ..

echo "finished updating site"


