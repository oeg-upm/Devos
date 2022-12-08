```mermaid
	classDiagram

    
    class `Server Hardware` {
    
    }

    class `Network Card` {
    
    }

    class `Hardware Item` {
    
    }

    class `Hardware Batch` {
    
    }

    class `Concept` {
    
    }

    class `Frame` {
    
    }

    class `Switch` {
    
    }



`Server Hardware`  --> `Hardware Batch`   :batch  

`Hardware Item`  --> `Network Card`   :network card  

`Server Hardware`  --> `Frame`   :hosted in frame  

`Server Hardware`  --> `Concept`   :high availability status  

`Network Card`  --> `Switch`   :switch  

```