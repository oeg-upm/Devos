```mermaid
	classDiagram

    
    class `File` {
    
    }

    class `Software` {
    
    }

    class `Software Directory` {
    
    }

    class `Service Module Version` {
    
    }

    class `Service Module` {
    
    }

    class `Auto Install Package` {
    
    }

    class `n62ac7628cfc64648bbf0e5a0a65a56d6b1` {
    
    }



`Software`  --> `File`   :released as file  

`Software Directory`  --> `Software Directory`   :parent directory  

`Software`  --> `Software Directory`   :in software directory  

`Service Module`  --> `Service Module Version`   :has version  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`File`  --> `Software Directory`   :in software directory  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`File`  --> `n62ac7628cfc64648bbf0e5a0a65a56d6b1`   :file type  

```