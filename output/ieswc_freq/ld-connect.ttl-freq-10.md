```mermaid
	classDiagram

    
    class Issue {
    
    }

    class ContributorList {
    
    }

    class List {
    
    }

    class Category {
    
    }

    class Journal {
    
    }

    class Volume {
    
    }

    class Series {
    
    }

    class Book {
    
    }

    class Chapter {
    
    }

    class Accessibility {
    
    }



Publication  --> ContributorList   :publicationAuthorList  

Series  --> Category   :category  

Volume  --> Journal   :volumeInJournal  

Publication  --> Accessibility   :publicationAccessibility  

List  --> List   :rest  

Article  --> Issue   :articleInIssue  

Publication  --> Chapter   :publicationInChapter  

Isssue  --> Volume   :issueInVolume  

Chapter  --> Book   :chapterInBook  

Publication  --> Issue   :publicationInIssue  

Journal  --> Category   :category  

Publication  --> ContributorList   :publicationEditorList  

Book  --> Series   :bookInSeries  

List  --> List   :first  

```