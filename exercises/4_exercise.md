# Example XML document

```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title lang="en">Harry Potter</title>
  </book>
  <book>
    <title lang="it">Harry Potter</title>
  </book>
  <book>
    <title lang="en">James Bond</title>
  </book>
  <book>
    <title lang="en">Alice in Wonderland</title>
  </book>
</bookstore>
```

# Practice with XPath

The root element

```/bookstore```

The value of the attribute @lang of the second book title

```/bookstore/book[2]/title/@lang```

The first AND the last book title

```/bookstore/book[1]/title | /bookstore/book[last()]/title```

All children of the first book element

```/bookstore/book[1]/*```

The text of all the title elements

```//title/text()```

# Practice with XQuery

```
for $x in /bookstore/book/title
let $lang := $x/@lang
return $lang
```

# Example HTML documents

```
<!doctype html>
<html>
  <head>
    <title>The title of the webpage on the browser tab!</title>
  </head>
  <body>
    <h1>The main title on the web page</h1>
    <p>This is an example paragraph. Everything in the <strong>body</strong> element will appear on the page.</p>
  </body>
</html>
```

```
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hello world</title>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li><a href="about.html">About me</a></li>
          <li><a href="contact.html">Contact me</a></li>
        </ul>
      </nav>
      <h1>Hello world!</h1>
    </header>
    <main>
    	<p>This is my first <strong>website</strong>.</p>
    </main>
    <footer>
      <p>Check my profile on 
        the <a href="https://www.unibo.it/sitoweb/marilena.daquino2">Unibo website</a></p>
    </footer>
  </body>
</html>
```