NS_LIST=$(kubectl get ns |  awk "{ print \$1 }" | grep -iv name | grep -v kube )

for ns in ${NS_LIST}; do
    kubectl get ns ${ns} -o yaml | grep labels
    if [[ "$?" == "1" ]]; then
        kubectl patch ns ${ns} --type=json -p='[{"op": "add", "path": "/metadata/labels", "value": {} }]'
    fi
    kubectl get ns ${ns} -o yaml | grep labels -A 10 | grep "monitoring: promethes" >/dev/null || kubectl patch ns ${ns} --type=json -p='[{"op": "add", "path": "/metadata/labels/monitoring", "value": "prometheus" }]'
done
