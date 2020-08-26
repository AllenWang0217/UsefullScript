# UsefullScript
Some useful script in python

## `statistic.py` 

use to statistic total line, comment line and blank line in all .h/.cpp file in a folder.

```shell
usage: statistic.py [-h] [-r ROOT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -r ROOT_PATH, --root_path ROOT_PATH
```

## `decoder.py`

 use to decode protobuf stream, use protoc command.

```bash
usage: decoder.py [-h] [-i INPUT_FILE] [-m MSG_TYPE] [-p PROTO_FILE]
                  [-o OUTPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        The input file for the hex stream
  -m MSG_TYPE, --msg_type MSG_TYPE
                        The message type to be decoded
  -p PROTO_FILE, --proto_file PROTO_FILE
                        The message type must be defined in PROTO_FILE or
                        their imports.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The output file for the parsed pb message
```



