```mermaid
	classDiagram

    
    class `Software` {
    
    }

    class `Service Module` {
    
    }

    class `Software Directory` {
    
    }

    class `Service Module Version` {
    
    }

    class `File` {
    
    }

    class `Auto Deploy Package` {
    
    }

    class `Auto Install Package` {
    
    }



`Auto Install Package`  --> `Auto Deploy Package`   :uses auto deploy package  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`Software`  --> `File`   :released as file  

`File`  --> `Software Directory`   :in software directory  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Software Directory`  --> `Software Directory`   :parent directory  

`Service Module`  --> `Service Module Version`   :has version  

`Service Module`  --> `Service Module Version`   :has version  

`Auto Install Package`  --> `Auto Deploy Package`   :uses auto deploy package  

`Software`  --> `Software Directory`   :in software directory  

`Software`  --> `File`   :released as file  

`Software`  --> `Software Directory`   :in software directory  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`Software`  --> `File`   :released as file  

`Auto Install Package`  --> `Auto Deploy Package`   :uses auto deploy package  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Service Module Version`  --> `Service Module`   :This property relates a Service Module Version with its corresponding Service Module  

`Auto Install Package`  --> `Service Module Version`   :This property identifies the Service Module Version that an Auto Install Package installs  

`Software Directory`  --> `Software Directory`   :parent directory  

`Software Directory`  --> `Software Directory`   :parent directory  

`Service Module`  --> `Service Module Version`   :has version  

```