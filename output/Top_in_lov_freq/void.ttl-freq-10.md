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



Dataset  --> Dataset   :propertyPartition  

Dataset  --> RDFSResource   :dataDump  

Document  --> Dataset   :inDataset  

Dataset  --> Document   :openSearchDescription  

Dataset  --> Dataset   :classPartition  

Linkset  --> Dataset   :target  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Dataset   :subset  

```