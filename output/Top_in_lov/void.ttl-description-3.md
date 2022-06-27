```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class Document {
    
    }

    class Linkset {
    
    }



Dataset  --> Dataset   :subset  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :classPartition  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> Dataset   :target  

```