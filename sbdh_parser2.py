from lxml import etree


sbdhtree = etree.parse('data/sbdh.xml')



class SBDH_Parser():
    xslt_simplify = etree.XML('''
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:sbdh="http://www.unece.org/cefact/namespaces/StandardBusinessDocumentHeader">
    <xsl:template match="/">
        <h>
            <s><xsl:apply-templates select="sbdh:StandardBusinessDocument/sbdh:StandardBusinessDocumentHeader/sbdh:Sender" /></s>
            <r><xsl:apply-templates select="sbdh:StandardBusinessDocument/sbdh:StandardBusinessDocumentHeader/sbdh:Receiver" /></r>
        </h>
    </xsl:template>
    <xsl:template match="sbdh:Identifier">
        <id><xsl:attribute name="A"><xsl:value-of select="./@Authority" /></xsl:attribute>
            <xsl:value-of select="normalize-space(./text())" /></id>
    </xsl:template>
 </xsl:stylesheet>'''
    )

    def _simplify(self, sbdh):
        transform = etree.XSLT(self.xslt_simplify)
        return transform(sbdh)

p = SBDH_Parser()
r = p._simplify(sbdhtree)
print( str(r) )

pass

