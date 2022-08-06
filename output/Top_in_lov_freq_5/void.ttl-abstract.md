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



Dataset  --> RDFSResource   :dataDump  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> Document   :openSearchDescription  

Dataset  --> TechnicalFeature   :feature  

Document  --> Dataset   :inDataset  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> Dataset   :classPartition  

Dataset  --> Dataset   :subset  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> Dataset   :target  

```