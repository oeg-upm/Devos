```mermaid
	classDiagram

    
    class LegalDocument {
    
    }

    class Document {
    
    }

    class LegalCaseDocument {
    
    }

    class AudioDocument {
    
    }

    class AudioVisualDocument {
    
    }

    class PersonalCommunicationDocument {
    
    }

    class DocumentStatus {
    
    }

    class CollectedDocument {
    
    }

    class DocumentPart {
    
    }



Document  --> Document   :translationOf  

Document  --> Ne70264f4359543f494a63616738949e9   :authorList  

Event  --> Document   :presents  

Document  --> Ne98f9a08194741e8a74dc2c072db60f5   :editorList  

Document  --> Document   :cites  

Document  --> DocumentStatus   :status  

Document  --> RDFSResource   :transcriptOf  

Document  --> Event   :presentedAt  

LegalDocument  --> Organization   :court  

AudioVisualDocument  --> Agent   :director  

Document  --> Document   :reproducedIn  

Document  --> N7d5dc4881bc141839c7e3ddace919b07   :contributorList  

PersonalCommunicationDocument  --> Agent   :recipient  

D  --> T   :C  

Document  --> Document   :citedBy  

Document  --> RDFSResource   :reviewOf  

```