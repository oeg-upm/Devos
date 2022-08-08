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



Dataset  --> Dataset   :classPartition  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> RDFSResource   :dataDump  

Document  --> Dataset   :inDataset  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> Document   :openSearchDescription  

Linkset  --> Dataset   :target  

```