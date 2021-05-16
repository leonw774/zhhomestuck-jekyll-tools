call bundle exec jekyll build

move ..\zhhomestuck.github.io\p\tmps\* ..\zhhomestuck.github.io\

python scripts/postprocess.py
python scripts/index_updater.py
python scripts/write_flash_index.py

echo "finished updating site"
