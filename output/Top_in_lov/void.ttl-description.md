```mermaid
	classDiagram

    
    class DatasetDescription {
    
    }

    class Dataset {
    
    }



Dataset  --> RDFSResource   :dataDump  

Dataset  --> Dataset   :subset  

Dataset  --> RDFSResource   :exampleResource  

Linkset  --> Dataset   :target  

Dataset  --> Dataset   :propertyPartition  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Dataset   :classPartition  

Document  --> Dataset   :inDataset  

Document  --> Dataset   :inDataset  

Dataset  --> Document   :openSearchDescription  

```