POST /ingest
Body: { repo_url, branch, commit_sha, file_path, content }
Response: { chunk_ids: [...], status: "ok" }

POST /query  
Body: { query, top_k?, namespace? }
Response: SSE stream of text tokens
