**Achived: As Docker does not build images automatically anymore, and some problems occured with the containers, this project is archived**

# forge-cli

**DISCLAIMER:** This is an inoffical docker container and is not associated with Atlassian. 

This Dockerfile is a thin wrapper around [@forge/cli](https://www.npmjs.com/package/@forge/cli) 
using the official [node](https://hub.docker.com/_/node) docker image.

You can find this image [on dockerhub here](https://hub.docker.com/r/craftamap/forge-cli).

Currently, the images on dockerhub are built by Dockerhub using the following 
`Automated Rules - Build configurations`:

| Source Type 	| Source      	| Docker Tag  	| Dockerfile location 	| Build Context 	| Autobuild 	| Build Caching 	| Description                                                  	|
| -------------	 | -------------	 | -------------	 | ---------------------	 | ---------------	 | -----------	 | ---------------	 | --------------------------------------------------------------	 |
| Tag            | /^[0-9.]+$/    | latest         | Dockerfile             | /                | ✔️            | ✔️                | This should only trigger on releases, but not on prereleases     |
| Tag            | /^[0-9.]+/     | {sourceref}    | Dockerfile             | /                | ✔️            | ✔️                | This should trigger on releases as well as prereleases           |

If the images on dockerhub are outdated, please create a new issue [here](https://github.com/craftamap/docker-forge-cli/issues).
