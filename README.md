### Part 1 - Install And Use Docker
1. [Install Git Command Line Interface](https://curriculeon.github.io/Curriculeon/lectures/version-control-systems/git/installation/content.html)
2. [Install Python]()
4. [Install Docker](https://curriculeon.github.io/Curriculeon/lectures/containerization/docker/installation/content.html)
5. [Install Docker (Windows 7)](https://curriculeon.github.io/Curriculeon/lectures/containerization/docker/installation-windows7/content.html)
6. [Containerize a Python Application]()
7. [SSH Into Docker Container](https://curriculeon.github.io/Curriculeon/lectures/containerization/docker/ssh-into-container/content.html)


### Part 2 - Install And Configure Jenkins
1. [Install Jenkins](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/installation/content.html)
2. [Create Jenkins Command Line Registry](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/create-commandline-registry/content.html)
3. [Disable Jenkins Security Use](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/disabling-security-use/content.html)
4. [Install Jenkins Plugin - Convert To Pipeline](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-convert-to-pipeline/content.html)
5. [Install Jenkins Plugin - Docker](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-docker-dependencies/content.html)
6. [Install Jenkins Plugin - ShiningPanda](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-shiningpanda/content.html)
7. [Jenkins Environment Configuration - Docker Integration](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/docker-integration/content.html)

### Part 3 - Creating Pipeline
1. [My First Python Unittest Pipeline]()
	* Create a Jenkins pipeline which
		1. clones a [python repositoy]()
		2. containerizes the repository in a docker instance
		3. runs the unittest on the application
			* `mvn package -Dmaven.test.failure.ignore=true`
		4. ensure output of build is displayed by Jenkins


### Part 4 - Passing Test Cases
1. [Python Developer Notes](./README-pythondev.md)


### Part 5 - Triggering Pipeline With Passing Tests
