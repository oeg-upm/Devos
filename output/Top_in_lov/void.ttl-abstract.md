```mermaid
	classDiagram

    
    class Linkset {
    
    }

    class Dataset {
    
    }

    class TechnicalFeature {
    
    }

    class DatasetDescription {
    
    }



Dataset  --> Document   :openSearchDescription  

Linkset  --> RDFProperty   :linkPredicate  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> Dataset   :target  

Dataset  --> Dataset   :subset  

Document  --> Dataset   :inDataset  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Dataset   :classPartition  

```