
#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
  echo "Usage: ./scripts/load-test.sh <service-url>"
  echo "Example: ./scripts/load-test.sh http://127.0.0.1:51234"
  exit 1
fi

echo "Starting load test on $URL/cpu"
echo "This will generate CPU load for HPA scaling."
echo "Press Ctrl+C to stop."

while true
do
  curl -s "$URL/cpu" > /dev/null &
  curl -s "$URL/cpu" > /dev/null &
  curl -s "$URL/cpu" > /dev/null &
  curl -s "$URL/cpu" > /dev/null &
  sleep 0.2
done
