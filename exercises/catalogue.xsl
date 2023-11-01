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
            <section>
            	<xsl:apply-templates/>
            </section>
          </xsl:for-each>
      </body>
    </html>
  </xsl:template>
  
  <xsl:template match="title">
    <h3><xsl:value-of select="."/></h3>
  </xsl:template>
  
  <xsl:template match="artist">
    <p><xsl:value-of select="."/></p>
  </xsl:template>
  
  <xsl:template match="year | label | country"/>
</xsl:stylesheet>
