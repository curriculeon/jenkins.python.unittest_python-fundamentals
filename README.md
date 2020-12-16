### Part 1 - Install And Use Docker
1. [Install Git Command Line Interface](https://curriculeon.github.io/Curriculeon/lectures/version-control-systems/git/installation/content.html)
2. [Install Python](https://curriculeon.github.io/Curriculeon/lectures/python/installation/content.html)

### Part 2 - Install And Configure Jenkins

1. [Install Jenkins](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/installation/content.html)
2. [Create Jenkins Command Line Registry](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/create-commandline-registry/content.html)
3. [Disable Jenkins Security Use](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/disabling-security-use/content.html)
4. [Install Jenkins Plugin - `Python` plugin](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-python/content.html)
5. [Install Jenkins Plugin - `ShiningPanda` for Python](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-shiningpanda/content.html)
6. [Install Jenkins Plugin - `Convert To Pipeline`](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/install-plugin-convert-to-pipeline/content.html)

### Part 3 - Creating Pipeline
1. [My First Python Unittest Pipeline](https://curriculeon.github.io/Curriculeon/lectures/ci-cd/jenkins/my-first-python-pipeline/content.html)
	* Create a Jenkins pipeline which
		1. clones a [python repositoy](https://github.com/curriculeon/jenkins.python.unittest_python-fundamentals)
		2. containerizes the repository in a docker instance
		3. runs the [`unittest`](https://docs.python.org/3/library/unittest.html) on the application
			* `python -m unittest discover -s ./src/test/ -p '*_test.py'`
		4. ensure output of build is displayed by Jenkins


### Part 4 - Passing Test Cases
1. [Python Developer Notes](./README-pythondev.md)


### Part 5 - Triggering Pipeline With Passing Tests


    
