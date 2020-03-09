from lxml import etree


sbdhtree = etree.parse('data/sbdh.xml')


nsmap = sbdhtree.getroot().nsmap
nsmap['nn'] = nsmap.pop(None)

print( sbdhtree.getroot().tag )
#h=sbdhtree.getroot().find("/StandardBusinessDocument")
headerNode=sbdhtree.xpath("/nn:StandardBusinessDocument"
                          +"/nn:StandardBusinessDocumentHeader",
                          namespaces=nsmap)[0]

senderNode=headerNode.xpath("nn:Sender/nn:Identifier[@Authority='iso6523-actorid-upis']",
                            namespaces=nsmap)[0]
print( "sender: ", "".join(senderNode.text) )
print( "sender: ", senderNode.attrib.get('Authority') )
receiverNode=headerNode.xpath("nn:Receiver/nn:Identifier[@Authority='iso6523-actorid-upis']",
                              namespaces=nsmap)[0]
print( "receiver: ", "".join(receiverNode.text) )
print( "receiver: ", receiverNode.attrib.get('Authority') )
documentIdNode=headerNode.xpath("nn:BusinessScope/nn:Scope"
                                +"/nn:Type[text()='DOCUMENTID']"
                                +"/../nn:InstanceIdentifier",
                                namespaces=nsmap)[0]
print( "documentId: ", "".join(documentIdNode.text) )
processIdNode=headerNode.xpath("nn:BusinessScope/nn:Scope"
                               +"/nn:Type[text()='PROCESSID']"
                               +"/../nn:InstanceIdentifier",
                               namespaces=nsmap)[0]
print( "processId: ", "".join(processIdNode.text) )

payloadType=headerNode.xpath("nn:DocumentIdentification/nn:Type",
                             namespaces=nsmap)[0]
instanceId=headerNode.xpath("nn:DocumentIdentification/nn:InstanceIdentifier",
                            namespaces=nsmap)[0]
payloadTypeNS=headerNode.xpath("nn:DocumentIdentification/nn:Standard",
                               namespaces=nsmap)[0]
print( "payloadType: ", payloadTypeNS.text, payloadType.text)
print( "instanceID: ", instanceId.text)
nsmap['pp'] = payloadTypeNS.text

payloadNode=sbdhtree.xpath("/nn:StandardBusinessDocument"
                           +"/pp:"+payloadType.text,
                           namespaces=nsmap)[0]
print( "payload: ", etree.tostring(payloadNode, pretty_print=True) )

pass

