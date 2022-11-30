```mermaid
	classDiagram

    
    class Publication {
    
    }

    class List {
    
    }

    class Geocoded Location {
    
    }

    class Book {
    
    }

    class Journal {
    
    }

    class Series {
    
    }

    class Chapter {
    
    }



Volume  --> Journal   :Volume In Journal  

Publication  --> string   :Source File  

Publication  --> Contributor List   :Editor List  

Book  --> Series   :Book In Series  

Publication  --> Contributor List   :Author List  

Publication  --> Issue   :Publication In Issue  

Geocoded Location  --> Geometry   :Geometry  

Series  --> Category   :Category  

Publication  --> Chapter   :Publication In Chapter  

Journal  --> Category   :Category  

Organization  --> Geocoded Location   :Geocoding Output  

List  --> List   :rest  

Publication  --> Accessibility   :Accessibility  

Chapter  --> Book   :Chapter In Book  

List  --> List   :first  

```