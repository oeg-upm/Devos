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



Journal  --> Category   :category  

Publication  --> ContributorList   :publicationAuthorList  

Book  --> Series   :bookInSeries  

Publication  --> ContributorList   :publicationEditorList  

Publication  --> Issue   :publicationInIssue  

List  --> List   :first  

List  --> List   :rest  

Publication  --> Accessibility   :publicationAccessibility  

Publication  --> Chapter   :publicationInChapter  

Series  --> Category   :category  

Isssue  --> Volume   :issueInVolume  

Volume  --> Journal   :volumeInJournal  

Publication  --> string   :sourceFile  

```