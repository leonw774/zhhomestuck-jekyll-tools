# zhhomestuck-jekyll-tools  

dependency:
- python >=3.5 (for the pre-processing & post-processing scripts)
- ruby >=2.1
  - jekyll ~> 4.0.0
  - jekyll-import
  - jekyll-paginate

make sure to put this directory under the same directory the site repository is, like this: 

some_directory  
|- zhhomestuck.github.io  
|- zhhomestuck-jekyll-tools  
 
name the blogger XML backup file as "blog.xml", make sure it is up-to-date, and:  
- run `import_and_build.bat` in Windows (it worked in 7, 10)  
- run `. ./import_and_build.sh` in Ubuntu or other Linux distribution (it worked in Ubuntu 18.04)  

# collections

- _posts: numbered story pages
- _pages: non-numberd story pages & non-story pages
- _tmps: meta pages that should locate at roots