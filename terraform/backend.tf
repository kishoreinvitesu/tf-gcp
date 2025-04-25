terraform { 
  cloud { 
    
    organization = "kichiOne" 

    workspaces { 
      name = "learning-workspace" 
    } 
  } 
}