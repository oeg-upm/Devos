```mermaid
	classDiagram

    
    class PersonalProfileDocument {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class Agent {
    
    }

    class OnlineGamingAccount {
    
    }

    class OnlineAccount {
    
    }

    class Image {
    
    }

    class Organization {
    
    }

    class OnlineChatAccount {
    
    }

    class Person {
    
    }

    class Agent {
    
    }

    class SpatialThing {
    
    }

    class OnlineAccount {
    
    }

    class Document {
    
    }

    class Image {
    
    }



Person  --> Image   :img  

Person  --> Document   :interest  

Person  --> Person   :knows  

Person  --> Document   :publications  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workInfoHomepage  

Person  --> Document   :workplaceHomepage  

Agent  --> OnlineAccount   :holdsAccount  

Agent  --> Document   :tipjar  

Agent  --> Document   :weblog  

Group  --> Agent   :member  

OnlineAccount  --> Document   :accountServiceHomepage  

SpatialThing  --> SpatialThing   :based_near  

Image  --> Image   :thumbnail  

```