#!/bin/bash
# Description: This script checks website status and logs results

readonly LOG_FILE="website_status.log"

check_site() {
  local url=$1
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" -L "$url")

  if [[ "$code" -eq 200 ]]; then
    echo "<$url> is UP" >> "$LOG_FILE"
  else
    echo "<$url> is DOWN" >> "$LOG_FILE"
  fi
}

array=(
  https://google.com
  https://facebook.com
  https://twitter.com
  https://giriwerwerwe.info
  https://example.org
  https://ietf.org
  https://w3.org
  https://mozilla.org
  https://opensuse.org
  https://ubuntu.com
  https://kernel.org
  https://golang.org
  https://python.org
  https://whyicannotfindit.com
  https://rust-lang.org
)

for url in "${array[@]}"; do
  check_site "$url"
done

echo "Availability website check logged to $LOG_FILE"