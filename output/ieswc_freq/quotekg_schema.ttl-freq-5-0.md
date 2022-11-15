```mermaid
	classDiagram

    
    class Mention {
    
    }

    class Context {
    
    }

    class Quotation {
    
    }



Mention  --> Context   :hasContext  

Quotation  --> Mention   :hasMention  

```