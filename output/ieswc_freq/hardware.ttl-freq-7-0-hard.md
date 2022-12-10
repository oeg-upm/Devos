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



`Server Hardware`  --> `Frame`   :hosted in frame  

`Network Card`  --> `Switch`   :switch  

`Server Hardware`  --> `Concept`   :high availability status  

`Server Hardware`  --> `Hardware Batch`   :batch  

`Hardware Item`  --> `Network Card`   :network card  

```