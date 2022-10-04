properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/8288tom/WorldOfGames-Main-Project.git"
    }
    stage("show files"){
        bat "dir"
    }
    stage("build image"){
      bat "docker build --no-cache -t worldofgamesimg ." 
    }
  stage("run image"){
    bat "docker compose up"
  }
}
