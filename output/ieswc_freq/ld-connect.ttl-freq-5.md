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



Series  --> Category   :category  

Publication  --> ContributorList   :publicationEditorList  

List  --> List   :first  

Volume  --> Journal   :volumeInJournal  

List  --> List   :rest  

Journal  --> Category   :category  

Publication  --> ContributorList   :publicationAuthorList  

Article  --> Issue   :articleInIssue  

Publication  --> Issue   :publicationInIssue  

```