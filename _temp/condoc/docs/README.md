- [pandoc](https://github.com/jgm/pandoc)
- [pandoc python](https://github.com/boisgera/pandoc)

- [pandoc - markdown 을 다양한 포맷으로 변환해 주는 변환기](https://www.lesstif.com/software-architect/pandoc-markdown-26083394.html)

## mathjax

### html to markdown
- https://stackoverflow.com/questions/11338049/how-to-convert-html-with-mathjax-into-latex-using-pandoc


```
# \(<mathjax>\) 형태
pandoc -f html+tex_math_dollars+tex_math_single_backslash <input.html>  -o <output.md>

# $<mathjax>$ 형태?
pandoc -f html+tex_math_dollars -t latex <input.html>  -o <output.md>
```




### markdown to html 
```
pandoc --standalone --mathjax -f markdown -t html <output.md> -o <input.html>

pandoc --standalone --mathjax -f markdown -t html  baekjun1.md -o  baekjun1_.html
```

#### align left

```css
body { 
    text-align: left !important;
    display: inline !important;
}

.MathJax_Display { 
    text-align: left !important;
    display: inline !important;
}
```

```js
MathJax.Hub.Config({
    jax: ["input/TeX","output/HTML-CSS"],
    displayAlign: "left"
});

```

## code block

### markdown to html


### html to markdown
https://github.com/jgm/pandoc/issues/5333

https://github.com/jgm/pandoc/issues/221


https://stackoverflow.com/questions/54214754/can-pandoc-mark-text-inside-a-code-block

```
function CodeBlock(elem)
  html = "<pre>" .. elem.text .. "</pre>"
  return pandoc.RawBlock("html", html)
```


$ pandoc -f html -t markdown t.html
$ pandoc -f html -t markdown+hard_line_breaks t.html 
$ pandoc -f html -t markdown+raw_html+hard_line_breaks t.html
$ pandoc -f html -t markdown+raw_html+hard_line_breaks-inline_code_attributes t.html




## pdf to docx

pip install pdf2docx

https://dothinking.github.io/pdf2docx/quickstart.convert.html


replace
{
    '\.': '.',
    '�': '='
}

regex
{
    r'^>$': '',
    r'([a-zA-Z])\n([a-zA-Z])': '\1 \2'
}





## docs to md
pandoc Problem-Solving_Strategies_Engel.docx -o Problem-Solving_Strategies_Engel.md