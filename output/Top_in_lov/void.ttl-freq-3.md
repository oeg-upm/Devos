```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class Document {
    
    }

    class Linkset {
    
    }



Document  --> Dataset   :inDataset  

Dataset  --> Document   :openSearchDescription  

Linkset  --> Dataset   :target  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :classPartition  

```