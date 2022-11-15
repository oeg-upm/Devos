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



List  --> List   :rest  

Publication  --> Chapter   :publicationInChapter  

Organization  --> GeocodedLocation   :geocodingOutput  

Contributor  --> Role   :contributorRole  

Isssue  --> Volume   :issueInVolume  

Chapter  --> Book   :chapterInBook  

Journal  --> Category   :category  

Book  --> Series   :bookInSeries  

GeocodedLocation  --> Geometry   :geometry  

Series  --> Category   :category  

```