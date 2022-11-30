```mermaid
	classDiagram

    
    class quotation text {
    
    }

    class context {
    
    }

    class Quotation {
    
    }



quotation text  --> context   :hasContext  

Quotation  --> quotation text   :hasMention  

```