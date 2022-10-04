properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/8288tom/WorldOfGames-Main-Project.git"
    }
    stage("show files"){
        bat "dir"
    }
    stage("build image"){
      bat "docker build --no-cache -t WorldOfGamesImg" .
    }
  stage("run image"){
    bat "docker run -d WorldOfGamesImg"
  }
}
