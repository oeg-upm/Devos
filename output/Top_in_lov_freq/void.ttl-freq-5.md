```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class RDFSResource {
    
    }

    class TechnicalFeature {
    
    }

    class RDFProperty {
    
    }

    class Document {
    
    }



Linkset  --> Dataset   :target  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> Dataset   :classPartition  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> RDFSResource   :exampleResource  

Document  --> Dataset   :inDataset  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Dataset   :subset  

```