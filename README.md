# homelab

This is my configuration for local k3s cluster.



<img src="https://mort.mkaciuba.com/images/transform/ZmlsZXMvc291cmNlcy9ubm5fZWM5MzZmY2Q3ZC5qcGc/photo_admin_big.jpg" width="500px"/>

# Blog posts

https://mkaciuba.com/blog/posts/homelab-2022-part-1/ 

https://mkaciuba.com/blog/posts/homelab-2022-part-2/

# Image gallery

https://imgur.com/a/QzCcYQ8

### Hardware

Compute:

* 4x RPi 4b 8GB RAM
* 2x RPi 4b 4GB RAM
* 2x AtomicPi
* 2x Cubieboard2
* 1x Lenovo T460

Network:

* Ubiquiti ER-10X EDGEMAX
* Ubiquiti UniFi US-8-60W


Network diagram:

<img src="https://mort.mkaciuba.com/images/transform/ZmlsZXMvc291cmNlcy9uZXR3b3JrX2RpYWdyYW1fYTE3ZjBlZDAwZi5wbmc/photo_network-diagram_big.jpg" width="500px"/>


Power supply:
* ATX ModeCom B88 500W


## Project structure

Project is divided by technology used for config.

### Ansible

Here you can find ansible playbook used for setup nodes and network. Folders:

* basic - here is basic configuration DNS, NFS client lib, script for controlling temperatur
* edgerouter - BGP configuration for ubiquiti edgerouter (adding nodes from cluster)
* k3s-ansible - copy-paste of ansible module to install k3s

### helmfile

Core infra that is installed to my cluster is managed by [helmfile](https://github.com/roboll/helmfile). Those components are:
- metallb - network loadbalancer for bare metal k8s
- prometheus, grafana, loki - for monitoring
- traefik for ingress
- nfs PVC provisioner
- cert-manager
- banzai vault-operator - for secret storage
- argocd - for apps deployment
- [mariadb-operator](https://github.com/aldor007/mariadb-operator) - for managment of MariaDB


### argo-apps

Helm charts for all of apps that are running inside of my cluster
