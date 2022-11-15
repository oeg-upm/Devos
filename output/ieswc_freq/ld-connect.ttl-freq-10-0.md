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

    class Book {
    
    }

    class Chapter {
    
    }

    class Contributor {
    
    }

    class Organization {
    
    }

    class GeocodedLocation {
    
    }



Publication  --> Chapter   :publicationInChapter  

Series  --> Category   :category  

Isssue  --> Volume   :issueInVolume  

Volume  --> Journal   :volumeInJournal  

Publication  --> Accessibility   :publicationAccessibility  

Publication  --> string   :sourceFile  

Publication  --> Issue   :publicationInIssue  

List  --> List   :rest  

Chapter  --> Book   :chapterInBook  

Contributor  --> Role   :contributorRole  

GeocodedLocation  --> Geometry   :geometry  

Contributor  --> Organization   :contributorAffiliation  

Organization  --> GeocodedLocation   :geocodingOutput  

Publication  --> ContributorList   :publicationAuthorList  

Journal  --> Category   :category  

Book  --> Series   :bookInSeries  

List  --> List   :first  

Publication  --> ContributorList   :publicationEditorList  

```