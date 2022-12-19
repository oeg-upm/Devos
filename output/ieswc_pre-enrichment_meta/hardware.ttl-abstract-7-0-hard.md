```mermaid
	classDiagram

    
    class `F5 Hardware` {
    
    }

    class `Server Hardware` {
    
    }

    class `Hardware Batch` {
    
    }

    class `Hardware Item` {
    
    }

    class `Frame` {
    
    }

    class `Network Card` {
    
    }

    class `Concept` {
    
    }



`Server Hardware`  --> `Frame`   :hosted in frame  

`Server Hardware`  --> `Hardware Batch`   :batch  

`Hardware Item`  --> `Network Card`   :network card  

`Server Hardware`  --> `Concept`   :high availability status  

```