```mermaid
	classDiagram

    
    class SpatialThing {
    
    }

    class LabelProperty {
    
    }

    class OnlineGamingAccount {
    
    }

    class Image {
    
    }

    class OnlineChatAccount {
    
    }

    class OnlineAccount {
    
    }

    class Agent {
    
    }

    class Organization {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class PersonalProfileDocument {
    
    }

    class SpatialThing {
    
    }

    class Image {
    
    }

    class OnlineAccount {
    
    }

    class Person {
    
    }

    class Agent {
    
    }

    class Document {
    
    }



SpatialThing  --> SpatialThing   :based_near  

Image  --> Thing   :depicts  

Image  --> Image   :thumbnail  

Person  --> Image   :img  

Thing  --> Image   :depiction  

OnlineAccount  --> Document   :accountServiceHomepage  

Agent  --> OnlineAccount   :account  

Agent  --> OnlineAccount   :holdsAccount  

Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Thing  --> Document   :homepage  

Agent  --> Document   :weblog  

Agent  --> Document   :openid  

Agent  --> Document   :tipjar  

Person  --> Document   :workplaceHomepage  

Person  --> Document   :workInfoHomepage  

Person  --> Document   :schoolHomepage  

Agent  --> Document   :interest  

Person  --> Document   :publications  

Thing  --> Document   :page  

Person  --> Person   :knows  

Person  --> Thing   :currentProject  

Person  --> Thing   :pastProject  

Agent  --> Thing   :mbox  

Agent  --> Thing   :made  

Agent  --> Thing   :topic_interest  

Thing  --> Agent   :maker  

Group  --> Agent   :member  

```