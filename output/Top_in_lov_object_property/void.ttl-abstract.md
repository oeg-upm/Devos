```mermaid
	classDiagram

    
    class Dataset {
    
    }

    class DatasetDescription {
    
    }



Dataset  --> Document   :openSearchDescription  

Dataset  --> TechnicalFeature   :feature  

Dataset  --> Dataset   :classPartition  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :subset  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> RDFSResource   :dataDump  

Dataset  --> RDFSResource   :exampleResource  

Dataset  --> RDFSResource   :dataDump  

Document  --> Dataset   :inDataset  

Dataset  --> Dataset   :propertyPartition  

Linkset  --> Dataset   :target  

```