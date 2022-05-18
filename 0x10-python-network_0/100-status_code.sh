 3 lines (3 sloc)  69 Bytes
   
#!/bin/bash
# status code
curl -so /dev/null -sw '%{http_code}' "$1"
