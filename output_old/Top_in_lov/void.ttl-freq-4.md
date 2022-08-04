```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class Document {
    
    }

    class Linkset {
    
    }

    class RDFSResource {
    
    }



Document  --> Dataset   :inDataset  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Document   :openSearchDescription  

Linkset  --> Dataset   :target  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :classPartition  

```