```mermaid
	classDiagram

    
    class LegalDocument {
    
    }

    class AudioVisualDocument {
    
    }

    class Document {
    
    }

    class DocumentStatus {
    
    }

    class DocumentPart {
    
    }

    class LegalCaseDocument {
    
    }

    class AudioDocument {
    
    }

    class CollectedDocument {
    
    }

    class PersonalCommunicationDocument {
    
    }



AudioVisualDocument  --> Agent   :director  

Document  --> Ndae9d35a90cf40a79cd79986a88b9b10   :authorList  

Document  --> Document   :citedBy  

Document  --> N6949a558a0e245709e74beedac56be0b   :editorList  

Event  --> Document   :presents  

Document  --> Document   :cites  

LegalDocument  --> Organization   :court  

Document  --> RDFSResource   :transcriptOf  

Document  --> N1cdd25ff99664edd8061b7a26ac3c97b   :contributorList  

D  --> T   :C  

Document  --> RDFSResource   :reviewOf  

Document  --> DocumentStatus   :status  

PersonalCommunicationDocument  --> Agent   :recipient  

Document  --> Document   :translationOf  

Document  --> Document   :reproducedIn  

Document  --> Event   :presentedAt  

```