rem ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'
python give_layouts.py
call jekyll b
echo remove unwanted tags
python p_tag_remover.py
echo copy pages
for /r "./pages" %%f in (*.html) do copy pages\%%~nxf zhhomestuck.github.io\p
echo make blog_raw.txt
python make_raw_blog.py
echo done.
