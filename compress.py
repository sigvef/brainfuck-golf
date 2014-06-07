import sys
import zlib
print zlib.compress(''.join([l for l in sys.stdin]), 9)
