import os
import logging

def main():
  path = os.environ["PATH_INFO"]
  if qs := os.getenv("QUERY_STRING"):
    path += f"?{qs}"
  if referer := os.environ.get("HTTP_REFERER"):
    logging.info("Request %s from %s", path, referer)
  else:
    logging.info("Request %s", path)
  for key, value in sorted(os.environ.iteritems()):
    logging.debug("%s=%r", key, value)
  path = os.environ["PATH_INFO"]

if __name__ == '__main__':
  main()
