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



Isssue  --> Volume   :issueInVolume  

Publication  --> ContributorList   :publicationEditorList  

Publication  --> Accessibility   :publicationAccessibility  

Publication  --> Chapter   :publicationInChapter  

Publication  --> XSDstring   :sourceFile  

List  --> List   :rest  

Series  --> Category   :category  

Book  --> Series   :bookInSeries  

List  --> List   :first  

Publication  --> Issue   :publicationInIssue  

Journal  --> Category   :category  

Volume  --> Journal   :volumeInJournal  

Publication  --> ContributorList   :publicationAuthorList  

```