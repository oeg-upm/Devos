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

Dataset  --> RDFSResource   :exampleResource  

Document  --> Dataset   :inDataset  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :classPartition  

Dataset  --> Document   :openSearchDescription  

Linkset  --> RDFProperty   :linkPredicate  

Linkset  --> Dataset   :target  

Dataset  --> TechnicalFeature   :feature  

```