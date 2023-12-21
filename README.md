# athena_mind_body_sync
Sync process for MindBody and Athena

## Development

### Build
- Rustc version 1.74.1 (docker image rust@sha256:fd45a543ed41160eae2ce9e749e5b3c972625b0778104e8962e9bfb113535301)

### Run (using docker)
```bash
docker run -it --rm -v ${PWD}:/project -w /project -u ${UID} rust@sha256:fd45a543ed41160eae2ce9e749e5b3c972625b0778104e8962e9bfb113535301 cargo run
```
