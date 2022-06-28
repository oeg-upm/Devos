```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class Linkset {
    
    }

    class Document {
    
    }

    class RDFSResource {
    
    }



Dataset  --> RDFSResource   :dataDump  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :classPartition  

Linkset  --> Dataset   :target  

Document  --> Dataset   :inDataset  

```