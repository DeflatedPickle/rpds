# rpds
Readable Python Data Storage

A multi-use Python based data storage format.

**Disclaimer:** Decoding and processing of the rpds format is only officially supported for .rpds and .rpd files, your mileage may vary when using other extensions and/or embedding of the rpds format into non-standard files.


## Proposed rpds interpreter (decoder) flow.
![rpds flow diagram](https://10.lithi.io/4GMGF9.png)

This image shows the structure of a multi-threaded interpreter, allowing for efficient handling of both wide and deep files. It will be subject to modification as the project moves forwards but gives a rought idea of how to read .rpd and .rpds files.
