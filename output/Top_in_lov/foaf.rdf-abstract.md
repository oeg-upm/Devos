```mermaid
	classDiagram

    
    class Image {
    
    }

    class OnlineEcommerceAccount {
    
    }

    class PersonalProfileDocument {
    
    }

    class OnlineGamingAccount {
    
    }

    class Agent {
    
    }

    class Person {
    
    }

    class OnlineAccount {
    
    }

    class OnlineChatAccount {
    
    }

    class LabelProperty {
    
    }

    class SpatialThing {
    
    }

    class Organization {
    
    }

    class Document {
    
    }



Document  --> Thing   :topic  

Document  --> Thing   :primaryTopic  

Agent  --> Thing   :mbox  

Agent  --> OnlineAccount   :account  

Thing  --> Agent   :maker  

SpatialThing  --> SpatialThing   :based_near  

Agent  --> Thing   :made  

Person  --> Image   :img  

Person  --> Document   :publications  

Agent  --> Document   :openid  

Thing  --> Document   :homepage  

Thing  --> Image   :depiction  

OnlineAccount  --> Document   :accountServiceHomepage  

Thing  --> Document   :page  

Group  --> Agent   :member  

Agent  --> Document   :tipjar  

Person  --> Thing   :pastProject  

Image  --> Image   :thumbnail  

Person  --> Person   :knows  

Agent  --> Document   :interest  

Agent  --> OnlineAccount   :holdsAccount  

Person  --> Document   :schoolHomepage  

Person  --> Document   :workplaceHomepage  

Image  --> Thing   :depicts  

Person  --> Thing   :currentProject  

Person  --> Document   :workInfoHomepage  

Agent  --> Document   :weblog  

Agent  --> Thing   :topic_interest  

```