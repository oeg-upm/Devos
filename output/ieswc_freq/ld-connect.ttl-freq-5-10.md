```mermaid
	classDiagram

    
    class Publication {
    
    }

    class List {
    
    }

    class Journal {
    
    }

    class Series {
    
    }

    class Volume {
    
    }



List  --> List   :rest  

Volume  --> Journal   :volumeInJournal  

List  --> List   :first  

Isssue  --> Volume   :issueInVolume  

Series  --> Category   :category  

Publication  --> ContributorList   :publicationEditorList  

Publication  --> Issue   :publicationInIssue  

Book  --> Series   :bookInSeries  

Journal  --> Category   :category  

```