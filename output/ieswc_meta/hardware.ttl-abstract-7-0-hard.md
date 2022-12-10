```mermaid
	classDiagram

    
    class `Hardware Batch` {
    
    }

    class `Hardware Item` {
    
    }

    class `F5 Hardware` {
    
    }

    class `Server Hardware` {
    
    }

    class `Frame` {
    
    }

    class `Concept` {
    
    }

    class `Network Card` {
    
    }



`Server Hardware`  --> `Hardware Batch`   :batch  

`Server Hardware`  --> `Frame`   :hosted in frame  

`Server Hardware`  --> `Concept`   :high availability status  

`Hardware Item`  --> `Network Card`   :network card  

```