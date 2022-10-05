properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("Checkout"){
        git "https://github.com/8288tom/WorldOfGames-Main-Project.git"
    }
    stage("show files"){
        bat "dir"
    }
    stage("build"){
        bat "docker build --no-cache -t worldofgamesimg ." 
    }
    stage("run"){
        bat "docker run -p 8777:8777 -d worldofgamesimg"
    }
    stage("install package){
        bat "pip install webdriver-manager"
    } 
    stage("test"){
        bat "python e2e.py"
    }   
}
