Various python scripts
========================

py2pdf
-------
• I needed to convert a bunch of online html tutorials to pdf
  so that I could read them on my transit. 
• It uses beautiful soup to parse the html to obtain hrefs, and 
  uses xhtml2pdf to convert them to pdf
• In addition, to merge the individual pdf files from each href link,
  I used pypdf2.
• I gave a shot at adding all html from the href links, and then 
  generate a pdf, but the generated pdf was not organized well.


