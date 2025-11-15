import sys
from pathlib import Path
import marshal
import dis

data = Path(sys.argv[1]).read_bytes()
co = marshal.loads(data[16:])
dis.dis(co)
print("hello world")