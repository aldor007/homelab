OS=$(shell uname)
LOWER_OS= `echo $(OS) | tr A-Z a-z`


install:
	mkdir -p .bin
	cd .bin && wget https://github.com/roboll/helmfile/releases/download/v0.138.4/helmfile_${OS}_amd64 && chmod +x ./helmfile_${OS}_amd64  && mv helmfile_${OS}_amd64 helmfile
	cd .bin && curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"
	cd .bin && curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
	# ifeq ($(OS), Darwin)
	# 	brew install gnu-getopt
	# endif
	cd .bin && wget -O helm.tar.gz  https://get.helm.sh/helm-v3.5.2-${LOWER_OS}-amd64.tar.gz && tar zxvf helm.tar.gz && mv ${LOWER_OS}-amd64/helm helm && rm -rf ${LOWER_OS}-amd64 && rm -rf helm.tar.gz
	.bin/helm plugin install https://github.com/jkroepke/helm-secrets --version 3.4.1 || .bin/helm plugin update secrets
	.bin/helm plugin install https://github.com/databus23/helm-diff --version v3.1.3 || .bin/helm plugin update diff
	.bin/helm plugin install https://github.com/aslafy-z/helm-git --version v0.10.0 || .bin/helm plugin update helm-git
