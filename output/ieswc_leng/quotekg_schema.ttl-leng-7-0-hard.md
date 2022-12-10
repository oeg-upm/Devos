```mermaid
	classDiagram

    
    class `context` {
    
    }

    class `quotation text` {
    
    }

    class `lang String` {
    
    }

    class `Quotation` {
    
    }



`quotation text`  --> `context`   :hasContext  

`Quotation`  --> `quotation text`   :hasMention  

```