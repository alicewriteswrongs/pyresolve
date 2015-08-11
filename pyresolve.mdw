#Resolving DNS queries with Python

I read a nice [short cartoon](https://howdns.works/) about how DNS works,
and I wanted to understand it in more detail. I thought it would be a nice
learning exercise to write a DNS resolver in Python - we're not going to
performance here, but instead for clean readable code and clear
explanations.

##Literate Python stuff

Before we get into the code let's explain this whole literate Python thing
a bit. I decided to use the [Pweave](https://github.com/mpastell/Pweave)
module, since it has the most options for output formats (.md, .tex,
.html, .rst, etc) and also lets you write you document's markup in
a variety of languages.

If you clone the repo to your computer you can do a `pip install -r
requirements.txt` to get all the dependencies for this project (including
Pweave). Then if you want to actually run the program you can do:

```bash
Ptangle pyresolve.md
```

which will 'tangle' the code. This terminology comes from Knuth's original
literate programming setup, which was called WEB and consisted of LaTeX
markup and Pascal source code. 'Weaving' a WEB document is taking this
combined source and producing a cleanly typeset document, and 'tangling'
the WEB is extracting just the source code from it.

Running the above command should give you a `pyresolve.py` which you can
run to test it out. I did not make any attempts to test for Python
2 compatibility, so it may not work with that. I'm quite sure things are
working on Python 3, however!
   
A note: Vim will open the file in Markdown mode (because it has the .md
extension) but this may not be what you want - I would rather have syntax
highlighting and plugins for the Python code when editing Python. So I did
these two bindings in my `~/.vimrc`:

```
nnoremap <Leader>lp :setlocal ft=python<cr>
nnoremap <Leader>md :setlocal ft=markdown<cr>
```

which works really smoothly!

##DNS queries

Anyway, how does DNS work? Well, it turns out it's sort of complicated!
The DNS is mainly laid out in RFCs
[1034](https://www.ietf.org/rfc/rfc1034.txt) and
[1035](https://www.ietf.org/rfc/rfc1035.txt), which (although very
informative) are quite long. 

The first bit of information we need is in 1035, in section 4 (Messages).
This is how the packet we're going to build for our DNS query is laid out:

```
+---------------------+
|        Header       |
+---------------------+
|       Question      | the question for the name server
+---------------------+
|        Answer       | RRs answering the question
+---------------------+
|      Authority      | RRs pointing toward an authority
+---------------------+
|      Additional     | RRs holding additional information
+---------------------+
```

(the IETF's ASCII art skills are legendary!). Basically, I think we`re
going to try to do this as some sort of bytestring, which Python gives us
lots of tools to work with.

But first, some import statements!

<<>>=
import random
@

We`re going to write a class to generate a query string:

<<>>=
class Header(object):
    def __init__(self):
    max = 65535
        self.id = bytearray(bytes(2))
        self.qdcount = bytearray(bytes(2))
@



<<>>=
    def classmethod(self):
        return "foo"
@



    


/* vim: set ft=python : */ 
