```mermaid
	classDiagram

    
    class Context {
    
    }

    class Mention {
    
    }



Quotation  --> Mention   :hasMention  

Mention  --> Context   :hasContext  

```