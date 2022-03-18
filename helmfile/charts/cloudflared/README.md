# Cloudflare Tunnel

This chart will connect to an existing tunnel, it will not create any resource on Cloudflare.
You can use [`cloudflare_argo_tunnel` Terraform resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/argo_tunnel) to create a new tunnel.

## Usage

Example values:

```yaml
replicaCount: 3

tunnel: example-tunnel
ingress:
  - hostname: mytunnel.example.com
    service: myservice.mynamespace.svc.cluster.local
```
