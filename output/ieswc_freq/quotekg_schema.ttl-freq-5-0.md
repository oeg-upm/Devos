```mermaid
	classDiagram

    
    class Mention {
    
    }

    class Context {
    
    }

    class Quotation {
    
    }



Quotation  --> Mention   :hasMention  

Mention  --> Context   :hasContext  

```