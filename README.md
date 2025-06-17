# What is this
Use this script to extract layers from a Mapbox Style JSON file based on source layer names. 

# How to use
To run the script run:

`./extract_layers_by_source_layer.py {input.json} {source_layers.txt} {output.json}`

For example, if you want to extract the source layers listed in `sample_source_layers.txt` from mapbox Style JSON file `sample_input.json` and create a new `sample_output.json`, you would run:

`./extract_layers_by_source_layer.py sample_input.json sample_source_layers.txt sample_outpu.json`