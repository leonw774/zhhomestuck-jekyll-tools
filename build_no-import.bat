python scripts\preprocess.py
copy blog-plain.txt ..\zhhomestuck.github.io\backups\blog-plain.txt

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
