```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class Linkset {
    
    }

    class Document {
    
    }



Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :classPartition  

Linkset  --> Dataset   :target  

Document  --> Dataset   :inDataset  

```