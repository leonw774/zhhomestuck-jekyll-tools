ruby -rubygems -e 'require "jekyll-import";JekyllImport::Importers::Blogger.run({"source"=^>"./blog.xml",})'
python give_layouts.py
call jekyll b
python p_tag_remover.py
for /r "./pages" %%f in (*.html) do copy pages\%%~nxf zhhomestuck.github.io\p
python make_raw_blog.py
echo done.
