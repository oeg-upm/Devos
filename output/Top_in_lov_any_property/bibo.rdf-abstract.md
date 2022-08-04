```mermaid
	classDiagram

    
    class LegalDocument {
    
    }

    class Document {
    
    }

    class AudioDocument {
    
    }

    class DocumentPart {
    
    }

    class LegalCaseDocument {
    
    }

    class PersonalCommunicationDocument {
    
    }

    class DocumentStatus {
    
    }

    class CollectedDocument {
    
    }

    class AudioVisualDocument {
    
    }



D  --> T   :C  

Document  --> N0f11d3f8035c489281af025621fa7033   :contributorList  

Document  --> RDFSResource   :reviewOf  

PersonalCommunicationDocument  --> Agent   :recipient  

LegalDocument  --> Organization   :court  

AudioVisualDocument  --> Agent   :director  

Document  --> Document   :translationOf  

Document  --> DocumentStatus   :status  

Event  --> Document   :presents  

Document  --> Nb1b775eb0955444380334dd57d78e1b8   :editorList  

Document  --> Event   :presentedAt  

Document  --> Document   :reproducedIn  

Document  --> Document   :cites  

Document  --> Document   :citedBy  

Document  --> RDFSResource   :transcriptOf  

Document  --> Nc7d0e8bb4a38463b9cf02144147018c3   :authorList  

```