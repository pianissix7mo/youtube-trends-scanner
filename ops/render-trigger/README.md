# Render trigger for Scanner A + Scanner B

This folder contains a tiny external scheduler entrypoint for Render.

Render runs the cron at both 09:07 and 10:07 UTC. The script checks
America/Toronto and only dispatches when Toronto is in the 05:00 hour,
so EDT/EST changes do not require manual schedule edits.

It dispatches:
- youtube-trends-scanner / scan.yml
- youtube-catalyst-scanner / scanner_b.yml

Required Render environment variable:
- GITHUB_TOKEN: a fine-grained GitHub token with Actions: Read and write
  access to both repositories.

The existing GitHub Actions schedule is not modified by these files.
