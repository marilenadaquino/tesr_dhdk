<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:template match="/">
    <html> 
      <head>
        <title><xsl:value-of select="tei:TEI/tei:text/tei:body/tei:div/tei:head/text()"/></title>
      </head>
      <body>
        <div>
            <xsl:for-each select="tei:TEI/tei:text/tei:body/tei:div">
                <xsl:for-each select="tei:head">
                    <h1><xsl:value-of select="."/></h1>
                </xsl:for-each>
                <xsl:for-each select="tei:div">
                    <div>
                        <xsl:for-each select="tei:head">
                            <h2><xsl:value-of select="."/></h2>
                        </xsl:for-each>
                        <xsl:for-each select="tei:lg">
                            <div>
                                <xsl:for-each select="tei:l">
                                    <p><xsl:value-of select="."/></p>
                                </xsl:for-each>
                            </div>
                        </xsl:for-each>
                    </div>
                </xsl:for-each>
            </xsl:for-each>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
