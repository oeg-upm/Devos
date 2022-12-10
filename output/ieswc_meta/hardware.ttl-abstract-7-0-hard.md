```mermaid
	classDiagram

    
    class `F5 Hardware` {
    
    }

    class `Hardware Item` {
    
    }

    class `Server Hardware` {
    
    }

    class `Hardware Batch` {
    
    }

    class `Network Card` {
    
    }

    class `Concept` {
    
    }

    class `Frame` {
    
    }



`Hardware Item`  --> `Network Card`   :network card  

`Server Hardware`  --> `Hardware Batch`   :batch  

`Server Hardware`  --> `Concept`   :high availability status  

`Server Hardware`  --> `Frame`   :hosted in frame  

```