# Python-Palindrome-Program-with-Dockerfile

DOCKER BUILD COMMAND:
  docker build -t <give_image_name> .
  
Give any image name in the build command, and you see the python script building and downloading all the dependencies. After that, a docker image with given name will be created and you can run that image using the following command to obtain the docker container of the palindrome program.

Note : Don't ignore dot(.) which is mentioned in the build command, because that tells the deamon to start it's execution from Dockerfile.

DOCKER RUN COMMAND:
  docker run -it <image_name>
  
 This palindrome program works for both numbers as well as text/string.
