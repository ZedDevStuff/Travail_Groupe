$admin = "http://localhost:8001"

curl.exe -s -X POST "$admin/services" `
  --data "name=bibliotheque-api" `
  --data "url=http://backend:8000"

curl.exe -s -X POST "$admin/services/bibliotheque-api/routes" `
  --data "name=api-route" `
  --data "paths[]=/api" `
  --data "strip_path=false"

curl.exe -s -X POST "$admin/services/bibliotheque-api/plugins" `
  --data "name=rate-limiting" `
  --data "config.minute=60"

curl.exe -s -X POST "$admin/services/bibliotheque-api/plugins" `
  --data "name=cors"