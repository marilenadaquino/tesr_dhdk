# XML example

```
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
  <cd>
    <title>Resistance</title>
    <artist>Muse</artist>
    <label>Warner Records</label>
    <country>UK</country>
    <year>2009</year>
  </cd>
  <cd>
    <title>Master of Puppets</title>
    <artist>Metallica</artist>
    <label>Elektra Records</label>
    <country>Denmark</country>
    <year>1986</year>
  </cd>
  <cd>
    <title>A night at the Opera</title>
    <artist>Queen</artist>
    <label>EMI</label>
    <country>UK</country>
    <year>1975</year>
  </cd>
</catalog>
```

# XSLT example

```
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html> 
      <head>
        <title>My music</title>
      </head>
      <body>
        <h2>My music collection</h2>
        <table>
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Label</th>
            <th>Country</th>
            <th>Year</th>
          </tr>
          <xsl:for-each select="catalog/cd">
            <tr>
              <td><xsl:value-of select="title"/></td>
              <td><xsl:value-of select="artist"/></td>
              <td><xsl:value-of select="label"/></td>
              <td><xsl:value-of select="country"/></td>
              <td><xsl:value-of select="year"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

# Exercise 1

```
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html> 
      <head>
        <title>My music</title>
      </head>
      <body>
        <h2>My music collection</h2>
          <xsl:for-each select="catalog/cd">
            <h3><xsl:value-of select="title"/> (<xsl:value-of select="year"/>)</h3>
            <p>Artist: <xsl:value-of select="artist"/></p>
            <p>Label: <xsl:value-of select="label"/>. Country: <xsl:value-of select="country"/>.</p>
          </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

# Exercise 2


The title of songs that are not produced by Warner records

```
<xsl:if test='label/text() != "Warner Records"'>
    <p><xsl:value-of select="title"/></p>
</xsl:if>
```

The name of artists that wrote a song after 2000

```
<xsl:if test='year/text() &gt; 2000'>
    <p><xsl:value-of select="artist"/></p>
</xsl:if>
```

The name of labels that are active in UK

```
<xsl:if test='country/text() = "Denmark"'>
    <p><xsl:value-of select="label"/></p>
</xsl:if>
```

If produced by a UK-based label return “British!”, otherwise “Somewhere else”

```
<xsl:choose>
    <xsl:when test='country/text() = "UK"'>
        <p>British!</p>
    </xsl:when>
    <xsl:otherwise>
        <p>Somewhere else</p>
    </xsl:otherwise>
</xsl:choose>
```